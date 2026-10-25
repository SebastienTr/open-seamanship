#!/usr/bin/env bash
# Build Open Seamanship and, with --deploy, install it into Project N.O.M.A.D.'s Kiwix library.
# With --dashboard, also install the mariner dashboard as a N.O.M.A.D. app with its own
# tile on the Command Center home page.
set -euo pipefail

LIBRARY="/opt/project-nomad/storage/zim"
CONTAINER="nomad_kiwix_server"
DEPLOY=0
ZIM=""
MODE="release"
DASHBOARD=0
DASH_PORT=8620
NOMAD_API="http://localhost:8080"
DASH_NAME="Open Seamanship"
DASH_SERVICE="nomad_custom_open_seamanship"
DASH_IMAGE="open-seamanship-dashboard"

usage() {
  cat <<EOF
Usage: ./install.sh [options]

Builds the Open Seamanship ZIM in dist/. With --deploy, copies it into the
Kiwix library and restarts the Kiwix container.

Options:
  --deploy             install the ZIM into the Kiwix library
  --dashboard          install the mariner dashboard as a N.O.M.A.D. app (home tile)
  --port PORT          host port for the dashboard (default: $DASH_PORT)
  --api URL            N.O.M.A.D. admin URL (default: $NOMAD_API)
  --zim FILE           use a prebuilt ZIM instead of building one
  --library DIR        Kiwix library folder (default: $LIBRARY)
  --container NAME     Kiwix container name (default: $CONTAINER)
  --preview            build a preview ZIM that includes unreviewed drafts
  -h, --help           show this help

Build needs: python3 (3.11+) with venv, git, make; --dashboard also needs
docker and curl. No internet is needed when --zim is given, and the dashboard
image is built locally from nginx:1.27-alpine (pulled once if missing).

Typical N.O.M.A.D. install: sudo ./install.sh --deploy --dashboard
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --deploy) DEPLOY=1 ;;
    --zim) ZIM="${2:?--zim needs a file}"; shift ;;
    --library) LIBRARY="${2:?--library needs a folder}"; shift ;;
    --container) CONTAINER="${2:?--container needs a name}"; shift ;;
    --preview) MODE="preview" ;;
    --dashboard) DASHBOARD=1 ;;
    --port) DASH_PORT="${2:?--port needs a number}"; shift ;;
    --api) NOMAD_API="${2:?--api needs a URL}"; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
  shift
done

cd "$(dirname "$0")"

# When run with sudo, build as the real user so .venv and dist/ are not owned by root.
# Only the copy into the Kiwix library and the container restart need root.
as_user() {
  if [ "$(id -u)" -eq 0 ] && [ -n "${SUDO_USER:-}" ] && [ "$SUDO_USER" != "root" ]; then
    sudo -u "$SUDO_USER" -H "$@"
  else
    "$@"
  fi
}

deps_ok() {
  [ -x .venv/bin/python ] &&
    [ "$(as_user .venv/bin/python -c "import libzim, yaml, markdown, jinja2, PIL; print('deps-ok')" 2>/dev/null)" = "deps-ok" ]
}

ensure_venv() {
  if deps_ok; then
    return
  fi
  echo "==> Setting up the Python environment in .venv"
  if ! as_user python3 -m venv --help >/dev/null 2>&1; then
    echo "python3 with venv is required. On Debian/Ubuntu: sudo apt install python3-venv" >&2
    exit 1
  fi
  # A .venv left by an interrupted run (for example created before python3-venv
  # was installed) has no pip or no packages: start again from scratch.
  rm -rf .venv
  if ! as_user python3 -m venv .venv || [ ! -x .venv/bin/pip ]; then
    echo "Could not create .venv with pip. On Debian/Ubuntu: sudo apt install python3-venv" >&2
    exit 1
  fi
  as_user .venv/bin/pip install --quiet --upgrade pip
  as_user .venv/bin/pip install --quiet -r requirements.txt
  deps_ok || { echo "Python packages failed to install; see the pip output above." >&2; exit 1; }
}

if [ -z "$ZIM" ]; then
  echo "==> Building Open Seamanship ($MODE)"
  # Earlier runs under sudo may have left root-owned build folders: hand them back.
  if [ "$(id -u)" -eq 0 ] && [ -n "${SUDO_USER:-}" ] && [ "$SUDO_USER" != "root" ]; then
    for d in .venv dist; do [ -e "$d" ] && chown -R "$SUDO_USER": "$d"; done
  fi
  ensure_venv
  rm -f dist/open-seamanship_*.zim
  as_user make all PYTHON=.venv/bin/python MODE="$MODE"
  ZIM="$(ls -1 dist/open-seamanship_*.zim | head -n 1)"
fi

[ -f "$ZIM" ] || { echo "ZIM not found: $ZIM" >&2; exit 1; }
echo "==> ZIM ready: $ZIM"

deploy_zim() {
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
}

# JSON for the N.O.M.A.D. custom-app API (POST creates, PUT updates and recreates the container).
dashboard_payload() {
  python3 - "$1" "$2" "$DASH_NAME" "$DASH_PORT" "$DASH_SERVICE" <<'PY'
import json, sys
image, method, name, port, service = sys.argv[1:]
body = {
    "friendly_name": name,
    "image": image,
    "ports": [{"container": 80, "host": int(port)}],
    "category": "education",
    "icon": "IconMap",
    "memory_mb": 128,
    "force": True,
}
if method == "PUT":
    body["service_name"] = service
print(json.dumps(body))
PY
}

deploy_dashboard() {
  command -v docker >/dev/null 2>&1 || { echo "--dashboard needs docker" >&2; exit 1; }
  command -v curl >/dev/null 2>&1 || { echo "--dashboard needs curl" >&2; exit 1; }
  code="$(curl -s -o /dev/null -w '%{http_code}' "$NOMAD_API/api/system/services/custom/$DASH_SERVICE" || true)"
  case "$code" in
    200) method=PUT ;;
    404) method=POST ;;
    *) echo "N.O.M.A.D. admin not reachable at $NOMAD_API (HTTP $code). Is N.O.M.A.D. running? Use --api." >&2; exit 1 ;;
  esac

  echo "==> Building the dashboard"
  ensure_venv
  as_user make dashboard PYTHON=.venv/bin/python MODE="$MODE"
  version="$(as_user env PYTHONPATH=build .venv/bin/python -c 'from osp import config; print(config.build_info().version)')"
  tag="$(printf '%s' "${version#v}" | tr -c 'A-Za-z0-9_.-' '-')"
  image="$DASH_IMAGE:$tag"
  docker build -q --build-arg OSP_VERSION="$version" -t "$image" dist/dashboard >/dev/null
  echo "==> Built image $image"

  echo "==> Registering '$DASH_NAME' with N.O.M.A.D. ($method)"
  resp="$(dashboard_payload "$image" "$method" |
    curl -sS -X "$method" -H 'Content-Type: application/json' --data-binary @- \
      -w '\n%{http_code}' "$NOMAD_API/api/system/services/custom")"
  status="$(printf '%s' "$resp" | tail -n 1)"
  body="$(printf '%s' "$resp" | sed '$d')"
  if [ "$status" != "200" ]; then
    echo "N.O.M.A.D. refused the app (HTTP $status): $body" >&2
    exit 1
  fi
  # Ask Kiwix to pick up any new ZIM (the pack or the private shelf).
  curl -s -o /dev/null -X POST "$NOMAD_API/api/zim/rescan-library" || true
  host="$(hostname -I 2>/dev/null | awk '{print $1}')"
  echo "==> Done. 'Open Seamanship' is on the Command Center home page,"
  echo "    or open http://${host:-localhost}:$DASH_PORT/ directly."
}

if [ "$DEPLOY" -eq 0 ] && [ "$DASHBOARD" -eq 0 ]; then
  echo "Not deployed. Run again with --deploy (Kiwix library) and/or --dashboard (home tile)."
  exit 0
fi
[ "$DEPLOY" -eq 1 ] && deploy_zim
[ "$DASHBOARD" -eq 1 ] && deploy_dashboard
exit 0
