"""Project configuration and version information."""

from __future__ import annotations

import datetime as dt
import os
import subprocess
from dataclasses import dataclass
from functools import cache

import yaml

from . import BUILD, CONTENT, ROOT


def _load(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


@cache
def licences() -> dict:
    return _load(BUILD / "licences.yaml")


@cache
def sections() -> dict:
    return _load(BUILD / "sections.yaml")


@cache
def regions() -> dict:
    return _load(BUILD / "regions.yaml")


@cache
def sources() -> list:
    return _load(ROOT / "sources.yaml") or []


@cache
def sources_by_id() -> dict:
    return {s["id"]: s for s in sources() if isinstance(s, dict) and "id" in s}


@cache
def assets() -> dict:
    return _load(CONTENT / "assets.yaml") or {}


def _git(*args: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
        )
        return out.stdout.strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


@dataclass(frozen=True)
class BuildInfo:
    version: str
    date: dt.date
    source_url: str | None


@cache
def build_info() -> BuildInfo:
    """Version and date come from git (or the environment), never the clock.

    The same commit therefore always produces the same HTML.
    """
    version = os.environ.get("OSP_VERSION") or _git("describe", "--tags", "--always", "--dirty")
    epoch = os.environ.get("SOURCE_DATE_EPOCH") or _git("log", "-1", "--format=%ct")
    date = (
        dt.datetime.fromtimestamp(int(epoch), dt.timezone.utc).date()
        if epoch
        else dt.date(1970, 1, 1)
    )
    url = os.environ.get("OSP_SOURCE_URL") or _git("remote", "get-url", "origin")
    if url and url.startswith("git@github.com:"):
        url = "https://github.com/" + url.removeprefix("git@github.com:")
    if url:
        url = url.removesuffix(".git")
    return BuildInfo(version=version or "0.0.0-dev", date=date, source_url=url)
