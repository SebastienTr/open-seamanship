#!/usr/bin/env python3
"""Build the local Wikipedia shelves: one small ZIM per list in wikipedia/<lang>/<shelf>.txt.

Uses openZIM's MWoffliner in Docker (pinned below). Needs internet and docker. Output:
dist/wikipedia/open-seamanship-wiki_<lang>_<shelf>.zim. A shelf whose ZIM already exists and
is newer than its list is skipped; --clean rebuilds everything.

    python3 scripts/build_wikipedia.py [--clean] [--only fr/bretagne] [--email you@example.org]
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SHELVES = ROOT / "wikipedia"
OUT = ROOT / "dist" / "wikipedia"
IMAGE = "ghcr.io/openzim/mwoffliner:2.1.1"
WIKI = {"fr": "https://fr.wikipedia.org", "en": "https://en.wikipedia.org"}
ZIM_LANG = {"fr": "fra", "en": "eng"}


def admin_email(arg: str | None) -> str:
    if arg:
        return arg
    if os.environ.get("OSP_ADMIN_EMAIL"):
        return os.environ["OSP_ADMIN_EMAIL"]
    try:
        out = subprocess.run(["git", "config", "user.email"], cwd=ROOT, capture_output=True, text=True)
        if out.stdout.strip():
            return out.stdout.strip()
    except OSError:
        pass
    return "open-seamanship@users.noreply.github.com"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--clean", action="store_true", help="rebuild every shelf")
    ap.add_argument("--only", help="comma-separated shelves, e.g. fr/bretagne")
    ap.add_argument("--email", help="operator email sent to Wikipedia (MWoffliner requires one)")
    ap.add_argument("--docker", default=os.environ.get("DOCKER", "docker"))
    ap.add_argument("--skip-lang", action="append", default=[],
                    help="language whose shelves are not built (a full Wikipedia is already installed)")
    args = ap.parse_args(argv)

    if shutil.which(args.docker) is None:
        print("docker is required to build the Wikipedia shelves", file=sys.stderr)
        return 1
    meta = yaml.safe_load((SHELVES / "shelves.yaml").read_text(encoding="utf-8")) if (SHELVES / "shelves.yaml").exists() else {}
    wanted = set(args.only.split(",")) if args.only else None
    if args.clean and OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    os.chmod(OUT, 0o777)          # MWoffliner runs as its own user inside the container
    email = admin_email(args.email)

    failed = 0
    for lst in sorted(SHELVES.glob("*/*.txt")):
        lang, shelf = lst.parent.name, lst.stem
        key = f"{lang}/{shelf}"
        if wanted and key not in wanted:
            continue
        if lang in args.skip_lang:
            print(f"== {key}: skipped, a full {lang} Wikipedia is installed (the dashboard links into it)")
            continue
        info = meta.get(f"{key}.txt") or meta.get(key) or {}
        name = f"open-seamanship-wiki_{lang}_{shelf}"
        zim = OUT / f"{name}.zim"
        if zim.exists() and zim.stat().st_mtime > lst.stat().st_mtime:
            print(f"== {key}: up to date ({zim.name})")
            continue
        n = sum(1 for line in lst.read_text(encoding="utf-8").splitlines() if line.strip())
        print(f"== {key}: {n} articles from {WIKI[lang]}", flush=True)
        cmd = [
            args.docker, "run", "--rm",
            "-v", f"{SHELVES}:/shelves:ro", "-v", f"{OUT}:/out",
            IMAGE, "mwoffliner",
            f"--mwUrl={WIKI[lang]}", f"--adminEmail={email}",
            f"--pageList=/shelves/{lang}/{shelf}.txt", "--outputDirectory=/out",
            f"--customZimName={name}", f"--customZimFilename={name}.zim",
            f"--customZimTitle={str(info.get('title', 'Wikipedia: ' + shelf))[:30]}",
            f"--customZimDescription={str(info.get('description', 'Wikipedia articles for mariners'))[:80]}",
            f"--customZimLanguage={ZIM_LANG[lang]}", "--publisher=Open Seamanship",
            "--customZimTags=_category:wikipedia;maritime;open-seamanship", "--webp",
        ]
        for proxy in ("HTTPS_PROXY", "HTTP_PROXY", "https_proxy", "http_proxy"):
            if os.environ.get(proxy):
                cmd[3:3] = ["-e", proxy]
        res = subprocess.run(cmd)
        made = sorted(OUT.glob(f"{name}*.zim"), key=lambda p: p.stat().st_mtime)
        if res.returncode != 0 or not made:
            print(f"   FAILED {key} (exit {res.returncode}); Wikipedia may be rate-limiting, try again later")
            failed += 1
            continue
        if made[-1] != zim:
            made[-1].replace(zim)
        print(f"   ok {zim.name} ({zim.stat().st_size // 1024} KiB)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
