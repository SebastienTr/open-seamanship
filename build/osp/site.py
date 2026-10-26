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


NESTED_ITEM = __import__("re").compile(r"^( +)(?=(?:[-*+]|\d+\.) )", __import__("re").M)


def _nest(text: str) -> str:
    """Python-Markdown nests a list only at 4-space steps; accept 2- or 3-space indents too."""
    def fix(m):
        n = len(m.group(1))
        return " " * (4 * -(-n // 4)) if n % 4 else m.group(1)
    return NESTED_ITEM.sub(fix, text)


def _md(text: str) -> str:
    return markdown.markdown(_nest(text), extensions=MD_EXTENSIONS, output_format="html")


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

    # Library: one page per citable source, the files themselves, and the section index.
    from html import escape

    from . import library

    cited_by: dict[str, list[Page]] = {}
    for p in included:
        for ref in p.meta.get("sources") or []:
            if isinstance(ref, dict) and ref.get("id"):
                cited_by.setdefault(ref["id"], []).append(p)
    lic_all = config.licences()
    lib_rows = []
    for e in library.entries():
        src = e.source
        lic = lic_all.get(src.get("licence"), {})
        links = library.publish_files(e, out_dir)
        parts = [f"<p class=\"summary\">{escape(str(src.get('publisher') or ''))}</p>"]
        if links:
            parts.append("<h2>In this pack</h2><ul class=\"listing\">")
            for ln in links:
                parts.append(f"<li><a href=\"{escape(ln['href'])}\">{escape(ln['label'])}</a> "
                             f"<span class=\"meta\">{escape(ln['size'])}</span></li>")
            parts.append("</ul>")
        elif src.get("third_party"):
            parts.append("<p>Not included in this pack: the file contains material owned by others ("
                         + escape(str(src["third_party"])) + "). Its text is cited where it is ours to use.</p>")
        elif src.get("status") == "cleared":
            parts.append("<p>Not included in this pack: cited for reference. "
                         "The original is at the address below.</p>")
        else:
            parts.append("<p>Not included: its licence is still being checked.</p>")
        parts.append("<h2>Licence and origin</h2><dl class=\"facts\">")
        parts.append(f"<dt>Licence</dt><dd>{escape(str(lic.get('name', src.get('licence'))))}</dd>")
        parts.append(f"<dt>Evidence</dt><dd>{escape(str(src.get('evidence') or ''))}</dd>")
        parts.append(f"<dt>Original</dt><dd>{escape(str(src.get('url') or ''))}</dd>")
        if src.get("retrieved"):
            parts.append(f"<dt>Retrieved</dt><dd>{escape(str(src['retrieved']))}</dd>")
        for f in e.files:
            if f in e.shipped:
                parts.append(f"<dt>{escape(f.path)}</dt><dd>SHA-256 {escape(f.sha256)}<br>{escape(f.url)}</dd>")
        parts.append("</dl>")
        citing = sorted(cited_by.get(e.id, []), key=lambda p: p.title.lower())
        if citing:
            parts.append("<h2>Pages that cite it</h2><ul class=\"listing\">")
            for p in citing:
                parts.append(f"<li><a href=\"../{p.out_path}\">{escape(p.title)}</a></li>")
            parts.append("</ul>")
        write(f"library/{e.id}.html", page=None, title=str(src.get("title", e.id)),
              section=section_by_slug.get("library"), body="".join(parts))
        lib_rows.append((e, bool(links)))

    # Section index pages.
    for s in sections:
        if s["slug"] == "library":
            items = []
            for e, has_files in lib_rows:
                if not has_files and e.id not in cited_by:
                    continue
                lic = lic_all.get(e.source.get("licence"), {}).get("name", e.source.get("licence"))
                note = "" if has_files else " · reference only"
                items.append(f"<li><a href=\"{escape(e.id)}.html\">{escape(str(e.source.get('title', e.id)))}</a>"
                             f"<span class=\"meta\">{escape(str(lic))}{note}</span><br>"
                             f"<span class=\"sub\">{escape(str(e.source.get('publisher') or ''))}</span></li>")
            body = ("<p class=\"summary\">" + escape(s["blurb"]) + "</p>"
                    + (f"<ul class=\"listing\">{''.join(items)}</ul>" if items
                       else "<p class=\"empty\">No documents downloaded yet. Run <code>make fetch-library</code>.</p>"))
            write("library/index.html", page=None, title=s["title"], section=s, body=body)
            continue
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
    counts["library"] = sum(1 for _, has in lib_rows if has)
    write(
        "index.html",
        page=home,
        title=home.title if home else "Open Seamanship",
        body=_md(home.body) if home else "",
        home=True,
        counts=counts,
        section=None,
    )
    broken = check_links(out_dir, written)
    if broken:
        raise SystemExit("broken internal links:\n  " + "\n  ".join(broken))
    return written


HREF = __import__("re").compile(r'(?:href|src)="([^"#?]+)(?:[#?][^"]*)?"')


def check_links(out_dir: Path, written: list[str]) -> list[str]:
    """Every relative link in a page we wrote must point at a file in the site."""
    broken = []
    for rel in written:
        page = out_dir / rel
        for target in HREF.findall(page.read_text(encoding="utf-8")):
            if "://" in target or target.startswith(("mailto:", "data:", "/")):
                continue
            if not (page.parent / target).resolve().exists():
                broken.append(f"{rel} -> {target}")
    return sorted(set(broken))

