#!/bin/sh
# Write the browser config from the environment at container start.
set -eu
cat > /usr/share/nginx/html/config.js <<JS
window.OSP_CONFIG = { kiwixPort: "${OSP_KIWIX_PORT}", kiwixPublicUrl: "${OSP_KIWIX_PUBLIC_URL}" };
JS
