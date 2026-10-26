#!/usr/bin/env bash
# Open Seamanship: set up everything on a Project N.O.M.A.D. host in one command.
#
#   sudo ./install.sh            download what is missing, build, install, register the dashboard
#   sudo ./install.sh --clean    same, but download everything again from scratch
#
# Safe to run again at any time (after `git pull`, for example): it only downloads what is
# missing, rebuilds, replaces the installed files and updates the dashboard app.
set -euo pipefail

LIBRARY="/opt/project-nomad/storage/zim"
CONTAINER="nomad_kiwix_server"
NOMAD_API="http://localhost:8080"
DASH_PORT=8620
DASH_NAME="Open Seamanship"
DASH_SERVICE="nomad_custom_open_seamanship"
DASH_IMAGE="open-seamanship-dashboard"
MODE="preview"
CLEAN=0
DO_LIBRARY=1
DO_PRIVATE=1
DO_WIKIPEDIA=1
DO_DASHBOARD=1
DO_DEPLOY=1
WARNINGS=()

usage() {
  cat <<EOF
Usage: sudo ./install.sh [options]

Does everything, in order:
  1. downloads the library (openly licensed manuals listed in sources.yaml)
  2. downloads the free official engine manuals into private/ and packs your private shelf
  3. builds the local Wikipedia shelves (wikipedia/*/*.txt) with MWoffliner
  4. builds the Open Seamanship pack (pages + library) as a ZIM
  5. installs every ZIM into the Kiwix library and asks N.O.M.A.D. to rescan it
  6. builds the dashboard and registers it as a N.O.M.A.D. app (home tile)
Anything already downloaded is kept. A failed download is reported at the end and
does not stop the rest.

Options:
  --clean            delete downloaded and built files first, then download everything again
                     (your own documents in private/ are never deleted)
  --release          pack reviewed pages only (default: preview, drafts marked "Unreviewed")
  --no-library       skip step 1        --no-private      skip step 2
  --no-wikipedia     skip step 3        --no-dashboard    skip step 6
  --no-deploy        build only; install nothing (steps 5 and 6 skipped)
  --port PORT        dashboard host port (default: $DASH_PORT)
  --api URL          N.O.M.A.D. admin URL (default: $NOMAD_API)
  --library DIR      Kiwix library folder (default: $LIBRARY)
  --container NAME   Kiwix container (default: $CONTAINER)
  -h, --help         show this help

Needs: python3 (3.11+) with venv, git, make, docker, curl, and internet for the downloads.
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --clean) CLEAN=1 ;;
    --release) MODE="release" ;;
    --preview) MODE="preview" ;;
    --no-library) DO_LIBRARY=0 ;;
    --no-private) DO_PRIVATE=0 ;;
    --no-wikipedia) DO_WIKIPEDIA=0 ;;
    --no-dashboard) DO_DASHBOARD=0 ;;
    --no-deploy) DO_DEPLOY=0; DO_DASHBOARD=0 ;;
    --deploy|--dashboard) ;;   # older options: these steps now run by default
    --port) DASH_PORT="${2:?--port needs a number}"; shift ;;
    --api) NOMAD_API="${2:?--api needs a URL}"; shift ;;
    --library) LIBRARY="${2:?--library needs a folder}"; shift ;;
    --container) CONTAINER="${2:?--container needs a name}"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

cd "$(dirname "$0")"

step() { printf '\n==> %s\n' "$*"; }
warn() { echo "WARNING: $*" >&2; WARNINGS+=("$*"); }

# Run as the real user under sudo, so .venv, library/, private/ and dist/ are not owned by root.
REAL_USER=""
if [ "$(id -u)" -eq 0 ] && [ -n "${SUDO_USER:-}" ] && [ "$SUDO_USER" != "root" ]; then
  REAL_USER="$SUDO_USER"
fi
as_user() {
  if [ -n "$REAL_USER" ]; then sudo -u "$REAL_USER" -H "$@"; else "$@"; fi
}
give_back() {
  if [ -n "$REAL_USER" ]; then
    for d in "$@"; do [ -e "$d" ] && chown -R "$REAL_USER": "$d"; done
  fi
  return 0
}

need() { command -v "$1" >/dev/null 2>&1 || { echo "$1 is required: $2" >&2; exit 1; }; }
need python3 "sudo apt install python3 python3-venv"
need make "sudo apt install make"
need git "sudo apt install git"
if [ "$DO_WIKIPEDIA" -eq 1 ] || [ "$DO_DASHBOARD" -eq 1 ] || [ "$DO_DEPLOY" -eq 1 ]; then
  need docker "Project N.O.M.A.D. installs it"
  need curl "sudo apt install curl"
fi
if [ "$DO_DEPLOY" -eq 1 ] && [ "$(id -u)" -ne 0 ]; then
  echo "Installing into $LIBRARY needs root: run with sudo (or use --no-deploy)." >&2
  exit 1
fi

deps_ok() {
  [ -x .venv/bin/python ] &&
    [ "$(as_user .venv/bin/python -c "import libzim, yaml, markdown, jinja2, PIL; print('deps-ok')" 2>/dev/null)" = "deps-ok" ]
}
ensure_venv() {
  deps_ok && return
  step "Setting up the Python environment in .venv"
  as_user python3 -m venv --help >/dev/null 2>&1 ||
    { echo "python3 with venv is required. On Debian/Ubuntu: sudo apt install python3-venv" >&2; exit 1; }
  rm -rf .venv   # a .venv from an interrupted run may lack pip or packages
  if ! as_user python3 -m venv .venv || [ ! -x .venv/bin/pip ]; then
    echo "Could not create .venv with pip. On Debian/Ubuntu: sudo apt install python3-venv" >&2
    exit 1
  fi
  as_user .venv/bin/pip install --quiet --upgrade pip
  as_user .venv/bin/pip install --quiet -r requirements.txt
  deps_ok || { echo "Python packages failed to install; see the pip output above." >&2; exit 1; }
}
PY=.venv/bin/python

give_back .venv dist library private
ensure_venv

# --- 0. clean -------------------------------------------------------------------------
if [ "$CLEAN" -eq 1 ]; then
  step "Cleaning: everything will be downloaded again"
  rm -rf dist library
  as_user "$PY" scripts/fetch_private.py --clean || true
fi

# --- 1. library -----------------------------------------------------------------------
if [ "$DO_LIBRARY" -eq 1 ]; then
  step "1/6 Library: openly licensed manuals"
  as_user "$PY" scripts/fetch_library.py || warn "some library files failed to download (see above); run again later"
fi

# --- 2. private shelf -----------------------------------------------------------------
if [ "$DO_PRIVATE" -eq 1 ]; then
  step "2/6 Private shelf: free official engine manuals (never published)"
  as_user "$PY" scripts/fetch_private.py ||
    warn "some engine manuals must be downloaded by hand: see the list printed above"
  as_user make private PYTHON="$PY" || warn "could not pack the private shelf"
fi

# --- 3. Wikipedia shelves -------------------------------------------------------------
if [ "$DO_WIKIPEDIA" -eq 1 ]; then
  step "3/6 Local Wikipedia shelves (this can take a while the first time)"
  email="$(as_user git config user.email 2>/dev/null || true)"
  "$PY" scripts/build_wikipedia.py ${email:+--email "$email"} ||
    warn "some Wikipedia shelves failed (Wikipedia may be rate-limiting); run again later"
  give_back dist
fi

# --- 4. the pack ----------------------------------------------------------------------
step "4/6 Building the Open Seamanship pack ($MODE)"
rm -f dist/open-seamanship_*.zim
as_user make all PYTHON="$PY" MODE="$MODE"
PACK="$(ls -1 dist/open-seamanship_*.zim | head -n 1)"
echo "    $PACK ($(du -h "$PACK" | cut -f1))"
[ "$MODE" = "preview" ] && echo "    Preview build: pages not yet reviewed are included and marked \"Unreviewed\"."

# --- 5. install into Kiwix ------------------------------------------------------------
install_zim() {   # install_zim FILE PATTERN-OF-OLDER-BUILDS
  local f="$1" pattern="$2" name old
  name="$(basename "$f")"
  for old in $LIBRARY/$pattern; do
    [ -e "$old" ] || continue
    [ "$(basename "$old")" = "$name" ] && continue
    rm -f -- "$old" && echo "    removed older $(basename "$old")"
  done
  install -m 0644 "$f" "$LIBRARY/$name"
  echo "    installed $name"
}

nomad_up() { [ "$(curl -s -o /dev/null -w '%{http_code}' "$NOMAD_API/api/system/services/custom/$DASH_SERVICE" || true)" != "000" ]; }

if [ "$DO_DEPLOY" -eq 1 ]; then
  step "5/6 Installing into the Kiwix library ($LIBRARY)"
  [ -d "$LIBRARY" ] || { echo "Kiwix library folder not found: $LIBRARY (use --library)" >&2; exit 1; }
  install_zim "$PACK" "open-seamanship_en_*.zim"
  for f in dist/private/open-seamanship-private_*.zim; do
    [ -e "$f" ] && install_zim "$f" "open-seamanship-private_*.zim"
  done
  for f in dist/wikipedia/open-seamanship-wiki_*.zim; do
    [ -e "$f" ] && install_zim "$f" "$(basename "$f")"
  done
  if nomad_up; then
    curl -s -o /dev/null -X POST "$NOMAD_API/api/zim/rescan-library" && echo "    asked N.O.M.A.D. to rescan the library"
  fi
  if docker ps --format '{{.Names}}' | grep -qx "$CONTAINER"; then
    docker restart "$CONTAINER" >/dev/null && echo "    restarted $CONTAINER"
  else
    warn "Kiwix container $CONTAINER is not running; start the Information Library in N.O.M.A.D."
  fi
fi

# --- 6. dashboard ---------------------------------------------------------------------
dashboard_payload() {
  python3 - "$1" "$2" "$DASH_NAME" "$DASH_PORT" "$DASH_SERVICE" <<'PY'
import json, sys
image, method, name, port, service = sys.argv[1:]
body = {"friendly_name": name, "image": image, "ports": [{"container": 80, "host": int(port)}],
        "category": "education", "icon": "IconMap", "memory_mb": 128, "force": True}
if method == "PUT":
    body["service_name"] = service
print(json.dumps(body))
PY
}

if [ "$DO_DASHBOARD" -eq 1 ]; then
  step "6/6 Dashboard (home tile in the Command Center)"
  code="$(curl -s -o /dev/null -w '%{http_code}' "$NOMAD_API/api/system/services/custom/$DASH_SERVICE" || true)"
  case "$code" in
    200) method=PUT ;;
    404) method=POST ;;
    *) method="" ; warn "N.O.M.A.D. admin not reachable at $NOMAD_API (HTTP $code); dashboard not registered (use --api)" ;;
  esac
  if [ -n "$method" ]; then
    as_user make dashboard PYTHON="$PY" MODE="$MODE"
    version="$(as_user env PYTHONPATH=build "$PY" -c 'from osp import config; print(config.build_info().version)')"
    tag="$(printf '%s' "${version#v}" | tr -c 'A-Za-z0-9_.-' '-')"
    image="$DASH_IMAGE:$tag"
    docker build -q --build-arg OSP_VERSION="$version" -t "$image" dist/dashboard >/dev/null
    echo "    built image $image"
    resp="$(dashboard_payload "$image" "$method" |
      curl -sS -X "$method" -H 'Content-Type: application/json' --data-binary @- \
        -w '\n%{http_code}' "$NOMAD_API/api/system/services/custom")"
    status="$(printf '%s' "$resp" | tail -n 1)"
    if [ "$status" = "200" ]; then
      echo "    registered '$DASH_NAME' with N.O.M.A.D. ($method)"
    else
      warn "N.O.M.A.D. refused the dashboard (HTTP $status): $(printf '%s' "$resp" | sed '$d')"
    fi
  fi
fi

give_back .venv dist library private
step "Done"
if [ "$DO_DASHBOARD" -eq 1 ]; then
  host="$(hostname -I 2>/dev/null | awk '{print $1}')"
  echo "Open Seamanship is on the Command Center home page, or at http://${host:-localhost}:$DASH_PORT/"
fi
if [ "${#WARNINGS[@]}" -gt 0 ]; then
  echo
  echo "Finished with ${#WARNINGS[@]} warning(s):"
  for w in "${WARNINGS[@]}"; do echo "  - $w"; done
fi
exit 0
