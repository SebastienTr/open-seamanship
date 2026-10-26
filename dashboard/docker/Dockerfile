# Open Seamanship dashboard for Project N.O.M.A.D. Built by `make dashboard` from dist/dashboard/.
FROM nginx:1.27-alpine
ENV OSP_RESOLVER=127.0.0.11 \
    OSP_KIWIX_UPSTREAM=nomad_kiwix_server:8080 \
    OSP_NOMAD_UPSTREAM=nomad_admin:8080 \
    OSP_KIWIX_PORT=8090 \
    OSP_KIWIX_PUBLIC_URL="" \
    OSP_PACK_BOOK=open-seamanship_en_all
COPY default.conf.template /etc/nginx/templates/default.conf.template
COPY 40-osp-config.sh /docker-entrypoint.d/40-osp-config.sh
RUN rm -f /etc/nginx/conf.d/default.conf
COPY www/ /usr/share/nginx/html/
ARG OSP_VERSION=dev
LABEL org.opencontainers.image.title="Open Seamanship" \
      org.opencontainers.image.description="Offline mariner dashboard for Project N.O.M.A.D." \
      org.opencontainers.image.source="https://github.com/SebastienTr/open-seamanship" \
      org.opencontainers.image.licenses="Apache-2.0 AND CC-BY-SA-4.0" \
      org.opencontainers.image.version="${OSP_VERSION}"
