"""Load pages from content/ and validate them against CONTENT_POLICY.md."""

from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from . import CONTENT, ROOT
from . import config

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

KINDS = {"card", "guide", "explainer", "history", "structural"}
STATUSES = {"draft", "reviewed", "verified"}
SAFETY = {"critical", "normal"}
RELEASE_STATUSES = {"reviewed", "verified"}
SOURCE_STATUSES = {"cleared", "check", "excluded"}

STRUCTURAL_KEYS = {"title", "kind", "section", "language", "licence"}
CONTENT_KEYS = STRUCTURAL_KEYS | {
    "summary", "region", "safety", "status", "authors", "reviewers", "reviewed", "sources",
}
OPTIONAL_KEYS = {"uncertain", "local_wikipedia", "summary"}


@dataclass
class Page:
    path: Path              # source file
    lang: str
    section: str            # "home" for the home page
    slug: str               # "index" for the home page
    meta: dict
    body: str

    @property
    def out_path(self) -> str:
        """Path of the rendered page inside the site and the ZIM."""
        if self.section == "home":
            return "index.html"
        return f"{self.section}/{self.slug}.html"

    @property
    def title(self) -> str:
        return self.meta["title"]

    @property
    def kind(self) -> str:
        return self.meta["kind"]

    @property
    def structural(self) -> bool:
        return self.kind == "structural"

    @property
    def releasable(self) -> bool:
        return self.structural or self.meta.get("status") in RELEASE_STATUSES


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, where, msg):
        self.errors.append(f"{_rel(where)}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{_rel(where)}: {msg}")

    @property
    def ok(self) -> bool:
        return not self.errors


def _rel(p) -> str:
    try:
        return str(Path(p).resolve().relative_to(ROOT))
    except (ValueError, TypeError):
        return str(p)


def parse(path: Path, lang: str) -> Page:
    text = path.read_text(encoding="utf-8")
    m = FRONT_MATTER.match(text)
    if not m:
        raise ValueError("missing YAML front matter (--- ... ---)")
    meta = yaml.safe_load(m.group(1)) or {}
    if not isinstance(meta, dict):
        raise ValueError("front matter must be a mapping")
    rel = path.relative_to(CONTENT / lang)
    if rel.parts == ("index.md",):
        section, slug = "home", "index"
    else:
        section, slug = rel.parts[0], path.stem
    return Page(path=path, lang=lang, section=section, slug=slug, meta=meta, body=m.group(2))


def load(lang: str, report: Report | None = None) -> list[Page]:
    report = report or Report()
    pages = []
    for path in sorted((CONTENT / lang).rglob("*.md")):
        try:
            pages.append(parse(path, lang))
        except (ValueError, yaml.YAMLError) as exc:
            report.error(path, str(exc))
    return pages


# --- validation ------------------------------------------------------------

def _is_date(v) -> bool:
    if isinstance(v, dt.date):
        return True
    try:
        dt.date.fromisoformat(str(v))
        return True
    except ValueError:
        return False


def validate_page(page: Page, report: Report, release: bool) -> None:
    m, where = page.meta, page.path
    kind = m.get("kind")
    if kind not in KINDS:
        report.error(where, f"kind must be one of {sorted(KINDS)}, got {kind!r}")
        return

    required = STRUCTURAL_KEYS if kind == "structural" else CONTENT_KEYS
    for key in sorted(required - m.keys()):
        report.error(where, f"missing field {key!r}")
    for key in sorted(m.keys() - CONTENT_KEYS - OPTIONAL_KEYS):
        report.error(where, f"unknown field {key!r}")

    if not str(m.get("title") or "").strip():
        report.error(where, "title is empty")
    if page.section != "home" and not SLUG.match(page.slug):
        report.error(where, "file name must be lowercase words joined by hyphens")
    if m.get("language") != page.lang:
        report.error(where, f"language {m.get('language')!r} does not match folder {page.lang!r}")

    section_slugs = {s["slug"] for s in config.sections().get(page.lang, [])}
    if page.section != "home" and page.section not in section_slugs:
        report.error(where, f"folder {page.section!r} is not a section in build/sections.yaml")
    if m.get("section") != page.section:
        report.error(where, f"section {m.get('section')!r} does not match folder {page.section!r}")

    if m.get("licence") not in config.licences():
        report.error(where, f"licence {m.get('licence')!r} is not accepted (build/licences.yaml)")

    if kind == "structural":
        return

    if m.get("region") not in config.regions():
        report.error(where, f"region {m.get('region')!r} is not in build/regions.yaml")
    if m.get("safety") not in SAFETY:
        report.error(where, f"safety must be one of {sorted(SAFETY)}")
    status = m.get("status")
    if status not in STATUSES:
        report.error(where, f"status must be one of {sorted(STATUSES)}")

    authors = m.get("authors") or []
    reviewers = m.get("reviewers") or []
    if not authors:
        report.error(where, "at least one author is required")
    if status in RELEASE_STATUSES:
        needed = 2 if m.get("safety") == "critical" else 1
        if len(set(reviewers)) < needed:
            report.error(where, f"status {status!r} with safety {m.get('safety')!r} needs {needed} reviewer(s)")
        if set(reviewers) & set(authors[:1]):
            report.error(where, "the main author cannot review their own page")
        if not _is_date(m.get("reviewed")):
            report.error(where, "reviewed must be a date (YYYY-MM-DD) once a page is reviewed")

    srcs = m.get("sources") or []
    if not srcs:
        report.error(where, "every content page cites at least one source")
    known = config.sources_by_id()
    for s in srcs:
        if not isinstance(s, dict) or "id" not in s:
            report.error(where, "each source needs an id and a locator")
            continue
        src = known.get(s["id"])
        if src is None:
            report.error(where, f"source {s['id']!r} is not in sources.yaml")
        elif src.get("status") == "excluded":
            report.error(where, f"source {s['id']!r} is excluded and cannot be cited")
        elif release and page.releasable and src.get("status") != "cleared":
            report.error(where, f"source {s['id']!r} is not cleared yet (status {src.get('status')!r})")
        if not str(s.get("locator") or "").strip():
            report.error(where, f"source {s['id']!r} needs a locator (chapter, page or section)")

    uncertain = m.get("uncertain")
    if uncertain is not None and not isinstance(uncertain, list):
        report.error(where, "uncertain must be a list of strings")


def validate_sources(report: Report) -> None:
    where = ROOT / "sources.yaml"
    seen = set()
    for i, s in enumerate(config.sources()):
        if not isinstance(s, dict) or "id" not in s:
            report.error(where, f"entry {i} has no id")
            continue
        sid = s["id"]
        if sid in seen:
            report.error(where, f"duplicate id {sid!r}")
        seen.add(sid)
        for key in ("title", "url", "evidence", "status"):
            if not s.get(key):
                report.error(where, f"{sid}: missing {key}")
        status = s.get("status")
        if status not in SOURCE_STATUSES:
            report.error(where, f"{sid}: status must be one of {sorted(SOURCE_STATUSES)}")
        if status != "excluded" and s.get("licence") not in config.licences():
            report.error(where, f"{sid}: licence {s.get('licence')!r} is not accepted")
        for f in s.get("files") or []:
            if not (isinstance(f, dict) and f.get("path") and re.fullmatch(r"[0-9a-f]{64}", str(f.get("sha256", "")))):
                report.error(where, f"{sid}: each file needs a path and a sha256")


def validate_assets(report: Report) -> None:
    records = config.assets()
    for path in sorted(CONTENT.rglob("*")):
        if path.is_dir() or path.suffix == ".md" or path.name == "assets.yaml":
            continue
        key = str(path.relative_to(CONTENT))
        rec = records.get(key)
        if rec is None:
            report.error(path, "no licence record in content/assets.yaml")
        elif rec.get("licence") not in config.licences():
            report.error(path, f"licence {rec.get('licence')!r} is not accepted")
    for key in records:
        if not (CONTENT / key).exists():
            report.warn(CONTENT / "assets.yaml", f"record for missing file {key!r}")


def validate_wikipedia(report: Report) -> None:
    for path in sorted((ROOT / "wikipedia").glob("*/*.txt")):
        lines = path.read_text(encoding="utf-8").split("\n")
        if lines and lines[-1] == "":
            lines = lines[:-1]
        if not lines:
            report.error(path, "shelf is empty")
        for n, line in enumerate(lines, 1):
            if not line.strip():
                report.error(path, f"line {n}: blank line")
            elif line.startswith("#"):
                report.error(path, f"line {n}: comments are not allowed (MWoffliner reads every line)")
            elif "_" in line:
                report.warn(path, f"line {n}: use spaces, not underscores")
            elif line != line.strip():
                report.error(path, f"line {n}: leading or trailing spaces")


def check_all(langs: list[str], release: bool) -> tuple[Report, dict[str, list[Page]]]:
    report = Report()
    validate_sources(report)
    validate_assets(report)
    validate_wikipedia(report)
    pages = {}
    for lang in langs:
        lang_pages = load(lang, report)
        outs = {}
        for p in lang_pages:
            validate_page(p, report, release)
            if p.out_path in outs:
                report.error(p.path, f"same output path as {_rel(outs[p.out_path])}")
            outs[p.out_path] = p.path
        if not any(p.section == "home" for p in lang_pages):
            report.error(CONTENT / lang, "missing home page index.md")
        pages[lang] = lang_pages
    return report, pages
