#!/usr/bin/env python3
"""Download the library: every `files` entry of the cleared sources in sources.yaml / sources.d.

Each file goes to library/<source-id>/<path> and must match its recorded SHA-256; a
mismatch is reported and the file is not kept. Files already present with the right
size are skipped (use --verify to re-hash them, --clean to start from nothing).

    python3 scripts/fetch_library.py [--clean] [--verify] [--only id1,id2] [--jobs 4]
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import shutil
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "build"))

from osp import library  # noqa: E402

UA = "OpenSeamanship-library/1.0 (+https://github.com/SebastienTr/open-seamanship)"
MAGIC = {".pdf": b"%PDF", ".zip": b"PK", ".epub": b"PK"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(f: library.LibFile, tries: int = 3) -> str:
    tmp = f.local.with_name(f.local.name + ".part")
    f.local.parent.mkdir(parents=True, exist_ok=True)
    last = ""
    for attempt in range(1, tries + 1):
        try:
            req = urllib.request.Request(f.url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=120) as r, tmp.open("wb") as out:
                shutil.copyfileobj(r, out, 1 << 20)
            magic = MAGIC.get(f.local.suffix.lower())
            if magic and not tmp.read_bytes()[:8].startswith(magic):
                raise ValueError("not the expected file type (the site may have moved it)")
            got = sha256(tmp)
            if f.sha256 and got != f.sha256:
                raise ValueError(f"SHA-256 mismatch: got {got[:12]}…, expected {f.sha256[:12]}…")
            tmp.replace(f.local)
            return "ok"
        except Exception as exc:  # noqa: BLE001 - report and retry
            last = str(exc)
            tmp.unlink(missing_ok=True)
            if attempt < tries:
                time.sleep(3 * attempt)
    return f"FAILED: {last}"


def prune() -> None:
    """Remove files in the cache that no source lists any more (and interrupted downloads)."""
    if not library.CACHE.exists():
        return
    keep = {f.local.resolve() for e in library.entries() for f in e.files if e.source.get("status") == "cleared"}
    removed = 0
    for path in sorted(library.CACHE.rglob("*"), reverse=True):
        if path.is_file() and path.resolve() not in keep:
            path.unlink()
            removed += 1
            print(f"   removed {path.relative_to(library.CACHE)} (no longer listed)")
        elif path.is_dir() and not any(path.iterdir()):
            path.rmdir()
    if removed:
        print(f"pruned {removed} file(s) no longer in the library")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--clean", action="store_true", help="delete the library cache first")
    ap.add_argument("--verify", action="store_true", help="re-hash files already present")
    ap.add_argument("--only", help="comma-separated source ids")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--prune", action="store_true",
                    help="delete cached files that sources.yaml no longer lists")
    args = ap.parse_args(argv)

    if args.clean and library.CACHE.exists():
        shutil.rmtree(library.CACHE)
        print(f"removed {library.CACHE}")
    wanted = set(args.only.split(",")) if args.only else None
    if args.prune:
        prune()

    todo, have, skipped = [], 0, 0
    for e in library.entries():
        if e.source.get("status") != "cleared" or (wanted and e.id not in wanted):
            continue
        for f in e.files:
            if f.skip or not f.url:
                skipped += 1
                continue
            if f.present and not (args.verify and sha256(f.local) != f.sha256):
                have += 1
                continue
            todo.append((e.id, f))

    total = sum(f.size or 0 for _, f in todo)
    print(f"library: {have} file(s) already here, {len(todo)} to download "
          f"({library.human_size(total) or 'size unknown'}), {skipped} skipped (too large or no URL)")
    failed = 0
    with cf.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        futures = {pool.submit(download, f): (sid, f) for sid, f in todo}
        for fut in cf.as_completed(futures):
            sid, f = futures[fut]
            res = fut.result()
            if res != "ok":
                failed += 1
            print(f"   {'ok    ' if res == 'ok' else ''}{sid}/{f.path}{'' if res == 'ok' else ': ' + res}", flush=True)
    print(f"\n{len(todo) - failed} downloaded, {have} already present, {failed} failed. Library in {library.CACHE}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
