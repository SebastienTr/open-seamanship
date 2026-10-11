#!/usr/bin/env bash
# Build Open Seamanship and, with --deploy, install it into Project N.O.M.A.D.'s Kiwix library.
# Follows the N.O.M.A.D. community add-on convention.
set -euo pipefail

LIBRARY="/opt/project-nomad/storage/zim"
CONTAINER="nomad_kiwix_server"
DEPLOY=0
ZIM=""
MODE="release"

usage() {
  cat <<EOF
Usage: ./install.sh [options]

Builds the Open Seamanship ZIM in dist/. With --deploy, copies it into the
Kiwix library and restarts the Kiwix container.

Options:
  --deploy             install the ZIM into the Kiwix library
  --zim FILE           use a prebuilt ZIM instead of building one
  --library DIR        Kiwix library folder (default: $LIBRARY)
  --container NAME     Kiwix container name (default: $CONTAINER)
  --preview            build a preview ZIM that includes unreviewed drafts
  -h, --help           show this help

Build needs: python3 (3.11+) with venv, git, make. No internet is needed when
--zim is given.
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --deploy) DEPLOY=1 ;;
    --zim) ZIM="${2:?--zim needs a file}"; shift ;;
    --library) LIBRARY="${2:?--library needs a folder}"; shift ;;
    --container) CONTAINER="${2:?--container needs a name}"; shift ;;
    --preview) MODE="preview" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

cd "$(dirname "$0")"

if [ -z "$ZIM" ]; then
  echo "==> Building Open Seamanship ($MODE)"
  if [ ! -x .venv/bin/python ]; then
    python3 -m venv .venv
    .venv/bin/pip install --quiet --upgrade pip
    .venv/bin/pip install --quiet -r requirements.txt
  fi
  rm -f dist/open-seamanship_*.zim
  make all PYTHON=.venv/bin/python MODE="$MODE"
  ZIM="$(ls -1 dist/open-seamanship_*.zim | head -n 1)"
fi

[ -f "$ZIM" ] || { echo "ZIM not found: $ZIM" >&2; exit 1; }
echo "==> ZIM ready: $ZIM"

if [ "$DEPLOY" -eq 0 ]; then
  echo "Not deployed. Run again with --deploy to install it into $LIBRARY."
  exit 0
fi

[ -d "$LIBRARY" ] || { echo "Kiwix library folder not found: $LIBRARY (use --library)" >&2; exit 1; }

# Remove older builds of the same pack and flavour (release or preview), then copy the new one.
name="$(basename "$ZIM")"
is_preview() { case "$1" in *_preview.zim) return 0 ;; *) return 1 ;; esac; }
for old in "$LIBRARY"/open-seamanship_en_*.zim; do
  [ -e "$old" ] || continue
  [ "$(basename "$old")" = "$name" ] && continue
  old_kind=release; is_preview "$old" && old_kind=preview
  new_kind=release; is_preview "$name" && new_kind=preview
  if [ "$old_kind" = "$new_kind" ]; then
    rm -f -- "$old" && echo "==> Removed older build $(basename "$old")"
  fi
done
install -m 0644 "$ZIM" "$LIBRARY/$name"
echo "==> Copied to $LIBRARY/$name"

if command -v docker >/dev/null 2>&1 && docker ps --format '{{.Names}}' 2>/dev/null | grep -qx "$CONTAINER"; then
  docker restart "$CONTAINER" >/dev/null
  echo "==> Restarted $CONTAINER"
else
  echo "Container $CONTAINER is not running; start N.O.M.A.D. and it will pick up the file."
fi
echo "If the pack does not appear, open Content Manager and use 'Rescan Library'."
