"""Tests for the page rules in CONTENT_POLICY.md. Run: make test."""

import tempfile
import unittest
from pathlib import Path

from libzim.reader import Archive
from libzim.search import Query, Searcher

from osp import CONTENT
from osp.pages import Page, Report, check_all, validate_page
from osp.site import build
from osp.zim import pack


def page(**overrides) -> Page:
    meta = {
        "title": "Engine overheating",
        "summary": "Temperature alarm on a small diesel.",
        "kind": "guide",
        "section": "fix-it",
        "region": "international",
        "language": "en",
        "licence": "CC-BY-SA-4.0",
        "safety": "normal",
        "status": "draft",
        "authors": ["alice"],
        "reviewers": [],
        "reviewed": None,
        "sources": [{"id": "navedtra-machinery-repairman", "locator": "ch. 1"}],
    }
    meta.update(overrides)
    return Page(
        path=CONTENT / "en" / "fix-it" / "engine-overheating.md",
        lang="en", section="fix-it", slug="engine-overheating", meta=meta, body="## Situation\nHot.\n",
    )


def errors(p: Page, release=True) -> list[str]:
    r = Report()
    validate_page(p, r, release)
    return r.errors


class PageRules(unittest.TestCase):
    def test_valid_draft(self):
        self.assertEqual(errors(page()), [])

    def test_non_commercial_licence_rejected(self):
        self.assertTrue(any("not accepted" in e for e in errors(page(licence="CC-BY-NC-SA-4.0"))))

    def test_page_needs_a_source(self):
        self.assertTrue(any("at least one source" in e for e in errors(page(sources=[]))))

    def test_source_needs_a_locator(self):
        e = errors(page(sources=[{"id": "navedtra-machinery-repairman", "locator": ""}]))
        self.assertTrue(any("locator" in x for x in e))

    def test_excluded_source_cannot_be_cited(self):
        e = errors(page(sources=[{"id": "who-imgs", "locator": "ch. 1"}]))
        self.assertTrue(any("excluded" in x for x in e))

    def test_unknown_source(self):
        e = errors(page(sources=[{"id": "nope", "locator": "p. 1"}]))
        self.assertTrue(any("not in sources.yaml" in x for x in e))

    def test_critical_page_needs_two_reviewers(self):
        p = page(safety="critical", status="reviewed", reviewers=["bob"], reviewed="2026-10-11")
        self.assertTrue(any("needs 2 reviewer" in e for e in errors(p)))
        p.meta["reviewers"] = ["bob", "carol"]
        self.assertEqual(errors(p), [])

    def test_author_cannot_review_own_page(self):
        p = page(status="reviewed", reviewers=["alice"], reviewed="2026-10-11")
        self.assertTrue(any("own page" in e for e in errors(p)))

    def test_reviewed_needs_a_date(self):
        p = page(status="reviewed", reviewers=["bob"])
        self.assertTrue(any("must be a date" in e for e in errors(p)))

    def test_release_needs_cleared_sources(self):
        p = page(status="reviewed", reviewers=["bob"], reviewed="2026-10-11",
                 sources=[{"id": "bowditch", "locator": "ch. 7"}])  # status: check
        self.assertTrue(any("not cleared" in e for e in errors(p, release=True)))
        self.assertEqual(errors(p, release=False), [])

    def test_unknown_region(self):
        self.assertTrue(any("region" in e for e in errors(page(region="atlantis"))))

    def test_unknown_field(self):
        self.assertTrue(any("unknown field" in e for e in errors(page(colour="blue"))))


class EndToEnd(unittest.TestCase):
    def test_repository_builds_and_packs(self):
        report, pages = check_all(["en"], release=True)
        self.assertEqual(report.errors, [])
        with tempfile.TemporaryDirectory() as tmp:
            site = Path(tmp) / "site"
            written = build("en", pages["en"], site, preview=False)
            self.assertIn("index.html", written)
            self.assertIn("emergency/index.html", written)
            self.assertIn("a-z.html", written)
            zim = pack("en", site, Path(tmp) / "test.zim")
            archive = Archive(str(zim))
            self.assertEqual(archive.main_entry.get_item().path, "index.html")
            self.assertTrue(archive.has_fulltext_index)
            self.assertTrue(archive.has_title_index)
            self.assertEqual(bytes(archive.get_metadata("Language")).decode(), "eng")
            search = Searcher(archive).search(Query().set_query("licences"))
            self.assertGreater(search.getEstimatedMatches(), 0)

    def test_drafts_only_in_preview(self):
        draft = page()
        with tempfile.TemporaryDirectory() as tmp:
            home = Page(path=CONTENT / "en" / "index.md", lang="en", section="home", slug="index",
                        meta={"title": "Home", "kind": "structural", "section": "home",
                              "language": "en", "licence": "CC-BY-SA-4.0"}, body="")
            rel = build("en", [home, draft], Path(tmp) / "r", preview=False)
            pre = build("en", [home, draft], Path(tmp) / "p", preview=True)
            self.assertNotIn("fix-it/engine-overheating.html", rel)
            self.assertIn("fix-it/engine-overheating.html", pre)
            html = (Path(tmp) / "p" / "fix-it" / "engine-overheating.html").read_text()
            self.assertIn("Unreviewed draft", html)


if __name__ == "__main__":
    unittest.main()
