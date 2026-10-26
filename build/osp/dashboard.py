"""Assemble the N.O.M.A.D. dashboard image context in dist/dashboard/.

Layout produced:
    dist/dashboard/Dockerfile, default.conf.template, 40-osp-config.sh   (from dashboard/docker/)
    dist/dashboard/www/            the dashboard (dashboard/*.html|css|js|svg)
    dist/dashboard/www/pack/       the static pack site, same pages as the ZIM
    dist/dashboard/www/sections.json   section tiles with page counts
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from . import DIST, ROOT
from . import config
from .pages import Page

SRC = ROOT / "dashboard"
OUT = DIST / "dashboard"
WEB_FILES = ("index.html", "dashboard.css", "dashboard.js", "config.js", "favicon.svg")


def _shelves() -> list[dict]:
    """The curated Wikipedia lists, for the dashboard's Local Wikipedia section."""
    import yaml

    folder = ROOT / "wikipedia"
    meta_file = folder / "shelves.yaml"
    meta = yaml.safe_load(meta_file.read_text(encoding="utf-8")) if meta_file.exists() else {}
    out = []
    for lst in sorted(folder.glob("*/*.txt")):
        lang, shelf = lst.parent.name, lst.stem
        info = meta.get(f"{lang}/{shelf}.txt") or {}
        out.append({
            "key": f"{lang}/{shelf}", "lang": lang,
            "title": info.get("title", shelf), "description": info.get("description", ""),
            "zim_name": f"open-seamanship-wiki_{lang}_{shelf}",
            "titles": [t for t in lst.read_text(encoding="utf-8").splitlines() if t.strip()],
        })
    return out


def _skip_library_files(site_dir: Path):
    files_dir = (site_dir / "library" / "files").resolve()

    def ignore(folder, names):
        return ["files"] if Path(folder).resolve() == files_dir.parent else []
    return ignore


def assemble(lang: str, pages: list[Page], site_dir: Path, preview: bool) -> Path:
    if OUT.exists():
        shutil.rmtree(OUT)
    www = OUT / "www"
    www.mkdir(parents=True)
    for f in sorted((SRC / "docker").iterdir()):
        shutil.copy2(f, OUT / f.name)
    for name in WEB_FILES:
        shutil.copyfile(SRC / name, www / name)
    # Library files stay in the ZIM only; nginx serves /pack/library/files/ from Kiwix.
    shutil.copytree(site_dir, www / "pack", ignore=_skip_library_files(site_dir))
    info = config.build_info()
    book = f"open-seamanship_{lang}_{info.version}{'_preview' if preview else ''}"
    with (OUT / "Dockerfile").open("a", encoding="utf-8") as f:
        f.write(f"\n# Kiwix path name of the matching pack ZIM (its file name without .zim)\nENV OSP_PACK_BOOK={book}\n")

    from . import library

    included = [p for p in pages if (preview or p.releasable) and p.section != "home"]
    counts: dict[str, int] = {}
    for p in included:
        counts[p.section] = counts.get(p.section, 0) + 1
    counts["library"] = sum(1 for e in library.entries() if e.shipped)
    data = {
        "version": info.version + (" (preview, unreviewed drafts included)" if preview else ""),
        "lang": lang,
        "sections": [
            {
                "slug": s["slug"],
                "title": s["title"],
                "blurb": s["blurb"],
                "accent": bool(s.get("accent")),
                "count": counts.get(s["slug"], 0),
            }
            for s in config.sections()[lang]
        ],
    }
    (www / "shelves.json").write_text(json.dumps({"shelves": _shelves()}, indent=1, ensure_ascii=False) + "\n",
                                      encoding="utf-8")
    (www / "sections.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return OUT
