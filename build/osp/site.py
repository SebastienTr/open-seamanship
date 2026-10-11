"""Render validated pages to a static HTML site (no JavaScript)."""

from __future__ import annotations

import shutil
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from . import BUILD, CONTENT
from . import config
from .pages import Page

KIND_ORDER = {"card": 0, "guide": 1, "explainer": 2, "history": 3, "structural": 4}
KIND_LABEL = {"card": "Card", "guide": "Guide", "explainer": "Explainer", "history": "History"}
STATUS_LABEL = {"draft": "Unreviewed", "reviewed": "Reviewed", "verified": "Verified"}

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list", "smarty"]


def _env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(BUILD / "templates"),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return env


def _md(text: str) -> str:
    return markdown.markdown(text, extensions=MD_EXTENSIONS, output_format="html")


def _root(out_path: str) -> str:
    """Relative prefix from a page back to the site root."""
    depth = out_path.count("/")
    return "../" * depth if depth else ""


def _sort_key(p: Page):
    return (KIND_ORDER.get(p.kind, 9), p.title.lower())


def _footer_sources(page: Page) -> list[dict]:
    out = []
    by_id = config.sources_by_id()
    for s in page.meta.get("sources") or []:
        src = by_id.get(s.get("id"), {})
        lic = config.licences().get(src.get("licence"), {})
        out.append({
            "title": src.get("title", s.get("id")),
            "locator": s.get("locator"),
            "licence": lic.get("name", src.get("licence")),
        })
    return out


def build(lang: str, pages: list[Page], out_dir: Path, preview: bool) -> list[str]:
    """Write the site for one language. Returns the list of written page paths."""
    info = config.build_info()
    env = _env()
    tpl = env.get_template("page.html")
    sections = config.sections()[lang]
    section_by_slug = {s["slug"]: s for s in sections}

    included = [p for p in pages if preview or p.releasable]
    by_section: dict[str, list[Page]] = {}
    for p in included:
        by_section.setdefault(p.section, []).append(p)
    for lst in by_section.values():
        lst.sort(key=_sort_key)

    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "static").mkdir(parents=True)
    for f in sorted((BUILD / "static").iterdir()):
        shutil.copyfile(f, out_dir / "static" / f.name)

    # Copy licensed assets (validated by `make check`) next to their pages.
    for key in sorted(config.assets()):
        if not key.startswith(f"{lang}/"):
            continue
        src = CONTENT / key
        dst = out_dir / Path(key).relative_to(lang)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)

    common = {
        "info": info,
        "preview": preview,
        "lang": lang,
        "sections": sections,
        "licences": config.licences(),
        "regions": config.regions(),
        "kind_label": KIND_LABEL,
        "status_label": STATUS_LABEL,
    }
    written = []

    def write(out_path: str, **ctx):
        html = tpl.render(root=_root(out_path), out_path=out_path, **common, **ctx)
        target = out_dir / out_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html, encoding="utf-8")
        written.append(out_path)

    # Content pages.
    for p in included:
        if p.section == "home":
            continue
        write(
            p.out_path,
            page=p,
            title=p.title,
            body=_md(p.body),
            section=section_by_slug.get(p.section),
            footer_sources=_footer_sources(p),
        )

    # Section index pages.
    for s in sections:
        members = [p for p in by_section.get(s["slug"], [])]
        write(
            f"{s['slug']}/index.html",
            page=None,
            title=s["title"],
            section=s,
            listing=members,
            body=None,
        )

    # A-Z index of every page: the symptom index.
    everything = sorted((p for p in included if p.section != "home"), key=lambda p: p.title.lower())
    write("a-z.html", page=None, title="All pages A-Z", section=None, listing=everything, az=True, body=None)

    # Home page.
    home = next((p for p in included if p.section == "home"), None)
    counts = {s["slug"]: len(by_section.get(s["slug"], [])) for s in sections}
    write(
        "index.html",
        page=home,
        title=home.title if home else "Open Seamanship",
        body=_md(home.body) if home else "",
        home=True,
        counts=counts,
        section=None,
    )
    return written
