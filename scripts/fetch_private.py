#!/usr/bin/env python3
"""Download free, official engine manuals into the private shelf (private/).

These files are copyrighted by their makers: they stay on your own machine and
are never part of the public pack. See private/README.md.

    python3 scripts/fetch_private.py --list
    python3 scripts/fetch_private.py                     # everything
    python3 scripts/fetch_private.py --only volvo-penta-md2000,tohatsu
    python3 scripts/fetch_private.py --only tohatsu --max-hp 10 --lang French

Then `make private` packs private/ into a personal ZIM.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts" / "private_downloads.yaml"
PRIVATE = ROOT / "private"
LOG = PRIVATE / "DOWNLOADS.tsv"
UA = "Mozilla/5.0 (OpenSeamanship private-shelf fetcher; personal use)"
SAFE = re.compile(r"[^A-Za-z0-9._-]+")


def get(url: str, timeout: int = 60) -> bytes:
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except (urllib.error.URLError, TimeoutError, ConnectionError) as exc:
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"{last}")


def quote_url(url: str) -> str:
    """Encode spaces and other unsafe characters in a path (Westerbeke uses spaces)."""
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(
        (p.scheme, p.netloc, urllib.parse.quote(urllib.parse.unquote(p.path)), p.query, p.fragment)
    )


def safe_name(s: str) -> str:
    return re.sub(r"-{2,}", "-", SAFE.sub("-", s)).strip("-")[:120] or "document.pdf"


# --- resolvers: each yields (file name, absolute URL) -------------------------

def resolve(item: dict, args) -> list[tuple[str, str]]:
    kind = item["type"]
    if kind == "url":
        return [(item["name"], item["url"])]
    if kind == "flowpaper":
        html = get(item["url"]).decode("utf-8", "replace")
        m = re.search(r"""PDFFile["']?\s*:\s*["']([^"'?]+\.pdf)""", html, re.I)
        if not m:
            raise RuntimeError("no PDF found in the viewer page")
        return [(item["name"], urllib.parse.urljoin(item["url"], m.group(1)))]
    if kind == "page-pdfs":
        html = get(item["url"]).decode("utf-8", "replace").replace("&#39;", "'")
        rx = re.compile(item.get("match", "."), re.I)
        out, seen = [], set()
        for href in re.findall(r'href="([^"]+\.pdf)"', html, re.I):
            if not rx.search(href) or href in seen:
                continue
            seen.add(href)
            url = quote_url(urllib.parse.urljoin(item["url"], href))
            out.append((safe_name(Path(urllib.parse.unquote(href)).name), url))
        return out
    if kind == "tohatsu":
        data = json.loads(get(item["url"]))
        max_hp = args.max_hp if args.max_hp is not None else item.get("max_hp", 30)
        langs = args.lang or item.get("languages", ["English"])
        out, seen = [], set()
        for m in data.get("manuals", []):
            hp = re.match(r"[\d.]+", str(m.get("Hp", "")))
            if not hp or float(hp.group()) > max_hp:
                continue
            for man in m.get("Manual", []):
                path = man.get("filepath") or ""
                if man.get("language") in langs and path and path not in seen:
                    seen.add(path)
                    url = urllib.parse.urljoin(item["url"], path)
                    lang = {"French": "FR", "English": "EN"}.get(man.get("language"), str(man.get("language")))
                    out.append((safe_name(f"Tohatsu-{m.get('Model', 'manual')}-{lang}") + ".pdf", url))
        return out
    raise RuntimeError(f"unknown resolver type {kind!r}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="list groups and exit")
    ap.add_argument("--only", help="comma-separated groups to fetch")
    ap.add_argument("--max-hp", type=float, help="Tohatsu: largest engine power to include")
    ap.add_argument("--lang", action="append", help="Tohatsu: language to include (repeatable)")
    ap.add_argument("--force", action="store_true", help="download again even if the file exists")
    args = ap.parse_args(argv)

    groups = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    if args.list:
        for name, g in groups.items():
            print(f"{name:24} {g.get('note', '')}")
        return 0
    wanted = set(args.only.split(",")) if args.only else set(groups)
    unknown = wanted - set(groups)
    if unknown:
        print(f"unknown group(s): {', '.join(sorted(unknown))}; use --list", file=sys.stderr)
        return 2

    PRIVATE.mkdir(exist_ok=True)
    new_log = not LOG.exists()
    ok = skipped = failed = dupes = 0
    by_hand: list[tuple[Path, str]] = []   # sites that refuse scripts (HTTP 403): fetch in a browser
    seen_hashes: dict[str, str] = {}
    for existing in sorted(PRIVATE.rglob("*.pdf")):  # duplicates are skipped across runs too
        seen_hashes.setdefault(hashlib.sha256(existing.read_bytes()).hexdigest(), existing.name)
    with LOG.open("a", encoding="utf-8") as log:
        if new_log:
            log.write("date\tgroup\tfile\tsha256\turl\n")
        for gname in [g for g in groups if g in wanted]:
            folder = PRIVATE / gname
            folder.mkdir(exist_ok=True)
            print(f"== {gname}")
            for item in groups[gname]["items"]:
                try:
                    targets = resolve(item, args)
                except Exception as exc:  # noqa: BLE001 - report and continue
                    print(f"   FAILED to resolve {item.get('url')}: {exc}")
                    failed += 1
                    continue
                for name, url in targets:
                    dest = folder / name
                    if dest.exists() and not args.force:
                        print(f"   skip  {name} (already here)")
                        skipped += 1
                        continue
                    try:
                        data = get(url)
                    except Exception as exc:  # noqa: BLE001
                        print(f"   FAILED {name}: {exc}")
                        failed += 1
                        by_hand.append((dest, url))
                        continue
                    if not data.startswith(b"%PDF"):
                        print(f"   FAILED {name}: not a PDF (the site may have moved it)")
                        failed += 1
                        continue
                    digest = hashlib.sha256(data).hexdigest()
                    if digest in seen_hashes:
                        print(f"   same  {name} = {seen_hashes[digest]} (not saved twice)")
                        dupes += 1
                        continue
                    seen_hashes[digest] = name
                    dest.write_bytes(data)
                    log.write(f"{dt.date.today()}\t{gname}\t{name}\t{digest}\t{url}\n")
                    print(f"   ok    {name} ({len(data) // 1024} KiB)")
                    ok += 1
    if by_hand:
        print("\nThese sites refuse scripts. Open each link in a browser, then save the file as shown;")
        print("the next run skips files that are already there.")
        for dest, url in by_hand:
            print(f"   {url}\n     -> {dest.relative_to(PRIVATE.parent)}")
    print(f"\n{ok} downloaded, {skipped} already present, {dupes} duplicates skipped, {failed} failed. "
          "Next: make private")
    return 0 if ok or skipped else 1


if __name__ == "__main__":
    sys.exit(main())
