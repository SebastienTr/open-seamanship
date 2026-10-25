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


def assemble(lang: str, pages: list[Page], site_dir: Path, preview: bool) -> Path:
    if OUT.exists():
        shutil.rmtree(OUT)
    www = OUT / "www"
    www.mkdir(parents=True)
    for f in sorted((SRC / "docker").iterdir()):
        shutil.copy2(f, OUT / f.name)
    for name in WEB_FILES:
        shutil.copyfile(SRC / name, www / name)
    shutil.copytree(site_dir, www / "pack")

    included = [p for p in pages if (preview or p.releasable) and p.section != "home"]
    counts: dict[str, int] = {}
    for p in included:
        counts[p.section] = counts.get(p.section, 0) + 1
    info = config.build_info()
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
    (www / "sections.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return OUT
