"""Command line: python -m osp {check,site,zim,all,private,sources,dashboard} [--lang en] [--preview]."""

from __future__ import annotations

import argparse
import os
import sys

from . import DIST
from . import config
from .pages import check_all

LANGS = ["en"]  # French joins after English v1.0 (see the plan)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="osp", description="Build the Open Seamanship pack.")
    ap.add_argument("command", choices=["check", "site", "zim", "all", "private", "sources", "dashboard"])
    ap.add_argument("--lang", action="append", choices=LANGS, help="language (default: all)")
    ap.add_argument(
        "--preview",
        action="store_true",
        default=os.environ.get("MODE", "release") == "preview",
        help="include unreviewed drafts (also MODE=preview)",
    )
    args = ap.parse_args(argv)
    langs = args.lang or LANGS
    release = not args.preview

    if args.command == "sources":
        from .sourcesdoc import OUT, write

        write()
        print(f"wrote {OUT.relative_to(DIST.parent)}")
        return 0

    if args.command == "private":
        from .private import pack as pack_private

        out = pack_private()
        if out is None:
            print("private/ has no documents yet; see private/README.md")
            return 0
        print(f"private zim: {out.relative_to(DIST.parent)} ({out.stat().st_size // 1024} KiB). Do not share it.")
        return 0

    report, pages = check_all(langs, release=release)
    from .sourcesdoc import is_current

    if not is_current():
        report.error(DIST.parent / "docs" / "SOURCES.md", "out of date; run `make sources`")
    for w in report.warnings:
        print(f"warning: {w}", file=sys.stderr)
    for e in report.errors:
        print(f"error: {e}", file=sys.stderr)
    if not report.ok:
        print(f"check failed: {len(report.errors)} error(s)", file=sys.stderr)
        return 1
    n = sum(len(v) for v in pages.values())
    mode = "preview" if args.preview else "release"
    print(f"check ok: {n} page(s), {len(config.sources())} source(s), mode {mode}")
    if args.command == "check":
        return 0

    from .site import build

    info = config.build_info()
    for lang in langs:
        site_dir = DIST / "site" / (f"{lang}-preview" if args.preview else lang)
        if args.command in ("site", "all", "dashboard"):
            written = build(lang, pages[lang], site_dir, preview=args.preview)
            print(f"site {lang}: {len(written)} page(s) in {site_dir.relative_to(DIST.parent)}")
        if args.command in ("zim", "all"):
            if not site_dir.exists():
                print(f"error: {site_dir} missing; run `site` first", file=sys.stderr)
                return 1
            from .zim import pack

            suffix = "_preview" if args.preview else ""
            out = DIST / f"open-seamanship_{lang}_{info.version}{suffix}.zim"
            pack(lang, site_dir, out, flavour="preview" if args.preview else "all")
            print(f"zim {lang}: {out.relative_to(DIST.parent)} ({out.stat().st_size // 1024} KiB)")
        if args.command == "dashboard":
            from .dashboard import assemble

            out = assemble(lang, pages[lang], site_dir, preview=args.preview)
            print(f"dashboard {lang}: image context in {out.relative_to(DIST.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
