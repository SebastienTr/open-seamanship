"""Private shelf: pack your own documents into a personal ZIM that is never published.

Put manuals you own (for example a Volvo Penta owner's or workshop manual you
bought) and your own notes in private/. `make private` packs them into
dist/private/. The public build never reads private/, git ignores it, and CI
never sees it.
"""

from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

import markdown
from libzim.writer import Creator, FileProvider, Hint, Item, StringProvider

from . import DIST, ROOT
from . import config
from .zim import illustration_png

PRIVATE = ROOT / "private"
KINDS = {".pdf": "application/pdf", ".md": "text/html", ".html": "text/html", ".txt": "text/plain",
         ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}


class _Item(Item):
    def __init__(self, path, title, mime, provider, front):
        super().__init__()
        self.p, self.t, self.m, self.prov, self.front = path, title, mime, provider, front

    def get_path(self):
        return self.p

    def get_title(self):
        return self.t

    def get_mimetype(self):
        return self.m

    def get_contentprovider(self):
        return self.prov()

    def get_hints(self):
        return {Hint.FRONT_ARTICLE: self.front, Hint.COMPRESS: self.m.startswith("text/")}


def _title(path: Path) -> str:
    name = re.sub(r"[_-]+", " ", path.stem).strip()
    return name[:1].upper() + name[1:]


def _page(title: str, body: str) -> str:
    return (
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        f"<title>{html.escape(title)}</title><link rel=\"stylesheet\" href=\"static/style.css\"></head>"
        "<body><header class=\"top\"><a class=\"brand\" href=\"index.html\">My private shelf</a></header>"
        f"<p class=\"banner draft\">Private: personal documents. Do not share this file.</p><main><h1>{html.escape(title)}</h1>"
        f"{body}</main></body></html>"
    )


def files() -> list[Path]:
    if not PRIVATE.exists():
        return []
    return sorted(
        p for p in PRIVATE.rglob("*")
        if p.is_file() and p.name != "README.md" and not p.name.startswith(".") and p.suffix.lower() in KINDS
    )


def pack(out_dir: Path | None = None) -> Path | None:
    docs = files()
    if not docs:
        return None
    info = config.build_info()
    out_dir = out_dir or DIST / "private"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    out = out_dir / f"open-seamanship-private_{info.date.isoformat()}.zim"
    css = (ROOT / "build" / "static" / "style.css").read_text(encoding="utf-8")

    rows = []
    with Creator(str(out)).config_indexing(True, "eng") as c:
        c.set_mainpath("index.html")
        c.add_item(_Item("static/style.css", "style", "text/css", lambda: StringProvider(css), False))
        for f in docs:
            rel = f.relative_to(PRIVATE).as_posix()
            title = _title(f)
            mime = KINDS[f.suffix.lower()]
            if f.suffix.lower() == ".md":
                path = "notes/" + rel[:-3].replace("/", "-") + ".html"
                body = markdown.markdown(f.read_text(encoding="utf-8"), extensions=["tables", "sane_lists"])
                page = _page(title, body).replace("static/style.css", "../static/style.css").replace(
                    'href="index.html"', 'href="../index.html"')
                c.add_item(_Item(path, title, "text/html", lambda page=page: StringProvider(page), True))
            else:
                path = "files/" + rel
                c.add_item(_Item(path, title, mime, lambda f=f: FileProvider(str(f)), mime == "text/html"))
            folder = rel.split("/")[0] if "/" in rel else ""
            rows.append((folder, title, path, f.suffix.lower().lstrip(".").upper()))

        groups: dict[str, list] = {}
        for folder, title, path, kind in rows:
            groups.setdefault(folder, []).append((title, path, kind))
        body = ["<p class=\"summary\">Your own documents, packed for offline use. "
                "PDFs open in your browser or PDF reader.</p>"]
        for folder in sorted(groups):
            if folder:
                body.append(f"<h2>{html.escape(_title(Path(folder)))}</h2>")
            body.append("<ul class=\"listing\">")
            for title, path, kind in groups[folder]:
                body.append(f"<li><a href=\"{html.escape(path)}\">{html.escape(title)}</a> "
                            f"<span class=\"meta\">{kind}</span></li>")
            body.append("</ul>")
        index = _page("My private shelf", "".join(body))
        c.add_item(_Item("index.html", "My private shelf", "text/html", lambda: StringProvider(index), True))

        c.add_metadata("Name", "open-seamanship-private")
        c.add_metadata("Title", "My private shelf")
        c.add_metadata("Description", "Personal documents packed with Open Seamanship. Not for sharing.")
        c.add_metadata("Language", "eng")
        c.add_metadata("Creator", "Owner of this copy")
        c.add_metadata("Publisher", "Owner of this copy")
        c.add_metadata("Date", info.date.isoformat())
        c.add_metadata("Flavour", "private")
        c.add_metadata("Tags", "_category:other;private")
        c.add_metadata("Illustration_48x48@1", illustration_png())
    return out
