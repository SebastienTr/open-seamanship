"""The library: openly licensed documents listed in sources.yaml / sources.d, cached in library/.

`scripts/fetch_library.py` downloads each source's `files` into library/<source-id>/<path>
and checks their SHA-256. The build publishes:

    library/index.html               every citable source, with its licence
    library/<source-id>.html         one page per source: licence, evidence, files, pages citing it
    library/files/<source-id>/...    the files themselves (cleared sources only)

A ZIP file (Project Gutenberg HTML books) is unpacked into a folder; its main HTML file is linked.
"""

from __future__ import annotations

import os
import shutil
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

from . import ROOT
from . import config

CACHE = Path(os.environ.get("OSP_LIBRARY_DIR", ROOT / "library"))


@dataclass
class LibFile:
    path: str            # as declared in sources.yaml
    url: str
    size: int | None
    sha256: str
    local: Path          # where fetch_library.py puts it
    skip: str | None = None

    @property
    def present(self) -> bool:
        if self.skip or not self.local.is_file():
            return False
        return self.size is None or self.local.stat().st_size == self.size


@dataclass
class Entry:
    source: dict
    files: list[LibFile] = field(default_factory=list)

    @property
    def id(self) -> str:
        return self.source["id"]

    @property
    def shipped(self) -> list[LibFile]:
        """Files that go into the pack: cleared sources only, and only if downloaded."""
        if self.source.get("status") != "cleared" or self.source.get("third_party"):
            return []   # third-party figures inside: cite the text, never ship the file as is
        return [f for f in self.files if f.present]


def entries() -> list[Entry]:
    out = []
    for s in config.sources():
        if not isinstance(s, dict) or s.get("status") == "excluded":
            continue
        e = Entry(source=s)
        for f in s.get("files") or []:
            if not isinstance(f, dict) or not f.get("path"):
                continue
            e.files.append(LibFile(
                path=str(f["path"]), url=str(f.get("url") or ""), size=f.get("size"),
                sha256=str(f.get("sha256") or ""), local=CACHE / s["id"] / str(f["path"]),
                skip=f.get("skip"),
            ))
        out.append(e)
    out.sort(key=lambda e: str(e.source.get("title", e.id)).lower())
    return out


def human_size(n: int | None) -> str:
    if not n:
        return ""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return ""


def _link_or_copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        os.link(src, dst)
    except OSError:
        shutil.copyfile(src, dst)


def publish_files(entry: Entry, out_dir: Path) -> list[dict]:
    """Place an entry's shipped files under out_dir/library/files/<id>/. Returns link records."""
    links = []
    base = out_dir / "library" / "files" / entry.id
    for f in entry.shipped:
        if f.path.lower().endswith(".zip"):
            folder = base / Path(f.path).stem
            with zipfile.ZipFile(f.local) as z:
                for info in z.infolist():
                    name = Path(info.filename)
                    if info.is_dir() or name.is_absolute() or ".." in name.parts:
                        continue
                    target = folder / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with z.open(info) as src, target.open("wb") as dst:
                        shutil.copyfileobj(src, dst)
            htmls = sorted(folder.rglob("*.htm*"), key=lambda p: (len(p.relative_to(folder).parts), -p.stat().st_size))
            if htmls:
                rel = htmls[0].relative_to(out_dir / "library").as_posix()
                links.append({"href": rel, "label": f"{Path(f.path).stem} (HTML book)", "size": human_size(f.size)})
        else:
            _link_or_copy(f.local, base / f.path)
            links.append({"href": f"files/{entry.id}/{f.path}", "label": f.path, "size": human_size(f.size)})
    return links


def zim_title(rel: str) -> str | None:
    """Title for a library file inside the ZIM, so title search finds it by its book name."""
    parts = rel.split("/")
    if len(parts) < 4 or parts[:2] != ["library", "files"]:
        return None
    src = config.sources_by_id().get(parts[2])
    if not src:
        return None
    name = parts[-1]
    if not name.lower().endswith((".pdf", ".epub")):
        return None
    return f"{src.get('title', parts[2])} ({name})"
