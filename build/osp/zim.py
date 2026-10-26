"""Pack the built site into a ZIM file with python-libzim."""

from __future__ import annotations

import io
import mimetypes
import re
from pathlib import Path

from libzim.writer import Creator, FileProvider, Hint, Item, StringProvider

from . import config

ZIM_LANG = {"en": "eng", "fr": "fra"}
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)

METADATA = {
    "en": {
        "Title": "Open Seamanship",  # 30 characters max
        "Description": "Offline seamanship, boat repair, navigation and safety for sailors",  # 80 max
        "LongDescription": (
            "A free, open knowledge pack for people on boats with no internet: emergency cards, "
            "troubleshooting guides for engines and boat systems, seamanship, navigation, weather, "
            "health at sea, maritime history, and a library of public-domain manuals."
        ),
        "Tags": "_category:other;sailing;seamanship;boats;maritime;navigation;survival;offline",
    },
}


class PageItem(Item):
    def __init__(self, path: str, title: str, file: Path, mimetype: str, front: bool):
        super().__init__()
        self._path, self._title, self._file, self._mime, self._front = path, title, file, mimetype, front

    def get_path(self):
        return self._path

    def get_title(self):
        return self._title

    def get_mimetype(self):
        return self._mime

    def get_contentprovider(self):
        return FileProvider(str(self._file))

    def get_hints(self):
        return {Hint.FRONT_ARTICLE: self._front, Hint.COMPRESS: not self._mime.startswith("image/")}


def illustration_png() -> bytes:
    """48x48 icon required by Kiwix: a navy square with a white wave and horizon."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (48, 48), (14, 58, 91))
    d = ImageDraw.Draw(img)
    d.ellipse((14, 6, 34, 26), outline=(255, 255, 255), width=3)       # compass ring
    d.line((24, 9, 24, 23), fill=(255, 255, 255), width=2)             # north line
    for y in (32, 39):                                                  # two waves
        d.arc((2, y - 4, 18, y + 4), 180, 360, fill=(255, 255, 255), width=2)
        d.arc((16, y - 4, 32, y + 4), 0, 180, fill=(255, 255, 255), width=2)
        d.arc((30, y - 4, 46, y + 4), 180, 360, fill=(255, 255, 255), width=2)
    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=False)
    return buf.getvalue()


def _mimetype(path: Path) -> str:
    if path.suffix == ".html":
        return "text/html"
    return mimetypes.guess_type(path.name)[0] or "application/octet-stream"


def pack(lang: str, site_dir: Path, out_file: Path, flavour: str = "all") -> Path:
    info = config.build_info()
    meta = METADATA[lang]
    out_file.parent.mkdir(parents=True, exist_ok=True)
    if out_file.exists():
        out_file.unlink()

    with Creator(str(out_file)).config_indexing(True, ZIM_LANG[lang]) as creator:
        creator.set_mainpath("index.html")
        for f in sorted(p for p in site_dir.rglob("*") if p.is_file()):
            rel = f.relative_to(site_dir).as_posix()
            mime = _mimetype(f)
            title = rel
            front = False
            from .library import zim_title

            lib_title = zim_title(rel)
            if lib_title:
                title, front = lib_title, True
            elif mime == "text/html":
                m = TITLE_RE.search(f.read_text(encoding="utf-8", errors="replace"))
                title = (m.group(1).replace(" · Open Seamanship", "") if m else rel).strip()
                front = True
            creator.add_item(PageItem(rel, title, f, mime, front))

        creator.add_metadata("Name", f"open-seamanship_{lang}_{flavour}")
        creator.add_metadata("Title", meta["Title"])
        creator.add_metadata("Description", meta["Description"])
        creator.add_metadata("LongDescription", meta["LongDescription"])
        creator.add_metadata("Language", ZIM_LANG[lang])
        creator.add_metadata("Creator", "Open Seamanship contributors")
        creator.add_metadata("Publisher", "Open Seamanship")
        creator.add_metadata("Date", info.date.isoformat())
        creator.add_metadata("Flavour", flavour)
        creator.add_metadata("Tags", meta["Tags"])
        creator.add_metadata("License", "CC BY-SA 4.0 for original text; library documents keep their own licences")
        if info.source_url:
            creator.add_metadata("Source", info.source_url)
        creator.add_metadata("Version", info.version)
        creator.add_metadata("Illustration_48x48@1", illustration_png())
    return out_file
