# Pinned build environment: `docker build -t open-seamanship .`
# then `docker run --rm -v "$PWD/dist:/work/dist" open-seamanship make all`
# Pin by digest (python:3.13-slim-bookworm@sha256:...) once the first release is cut.
FROM python:3.13-slim-bookworm

RUN apt-get update \
 && apt-get install -y --no-install-recommends git make \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /work
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# The repository is copied without guarantees about .git; pass the version explicitly
# when building outside a clone: docker run -e OSP_VERSION=v0.1.0 -e SOURCE_DATE_EPOCH=...
RUN git config --global --add safe.directory /work
CMD ["make", "all"]
