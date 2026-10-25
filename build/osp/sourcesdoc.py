"""Render docs/SOURCES.md from sources.yaml, so the human-readable list never drifts.

`python -m osp sources` rewrites the file; `python -m osp check` fails if it is stale.
"""

from __future__ import annotations

from . import ROOT
from . import config

OUT = ROOT / "docs" / "SOURCES.md"

SECTIONS = [
    ("cleared", "Cleared", "Licence verified; may be redistributed in the public pack."),
    ("check", "To check", "Promising, but the licence, edition or third-party material still needs checking."),
    ("excluded", "Excluded", "Looked at and rejected, with the reason, so nobody checks them again."),
]


def _cell(text) -> str:
    return str(text or "").replace("|", "\\|").replace("\n", " ").strip()


def render() -> str:
    sources = [s for s in config.sources() if isinstance(s, dict)]
    lic = config.licences()
    lines = [
        "# Sources",
        "",
        "<!-- Generated from sources.yaml by `python -m osp sources`. Do not edit by hand. -->",
        "",
        f"{len(sources)} sources tracked. The licence rules are in [CONTENT_POLICY.md](../CONTENT_POLICY.md).",
        "",
    ]
    for status, title, blurb in SECTIONS:
        rows = [s for s in sources if s.get("status") == status]
        lines += [f"## {title} ({len(rows)})", "", blurb, ""]
        if not rows:
            lines += ["None yet.", ""]
            continue
        lines += ["| Source | Publisher | Licence | Evidence |", "| --- | --- | --- | --- |"]
        for s in rows:
            name = f"[{_cell(s.get('title'))}]({s.get('url')})" if s.get("url") else _cell(s.get("title"))
            licence = lic.get(s.get("licence"), {}).get("name", "none") if s.get("licence") else "none"
            lines.append(f"| {name} | {_cell(s.get('publisher'))} | {licence} | {_cell(s.get('evidence'))} |")
        lines.append("")
    return "\n".join(lines)


def write() -> None:
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(render(), encoding="utf-8")


def is_current() -> bool:
    return OUT.exists() and OUT.read_text(encoding="utf-8") == render()
