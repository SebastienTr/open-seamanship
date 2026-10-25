# Contributing

Thank you. Please read [CONTENT_POLICY.md](CONTENT_POLICY.md) first: it says
which licences we accept and how pages are reviewed.

## Add or change a page

1. Copy the front matter from [docs/PAGE_TEMPLATE.md](docs/PAGE_TEMPLATE.md)
   into a new file under `content/en/<section>/`. The file name becomes the URL:
   use lowercase words and hyphens (`engine-overheating.md`).
2. Set `status: draft`. Only reviewers change the status.
3. Cite a source for every number and procedure. If the source is not yet in
   `sources.yaml`, add it (below).
4. Run `make check` and `MODE=preview make site`, then open
   `dist/site/index.html` and read your page.
5. Open a pull request. Say which reviewers you think fit.

## Add a source

Add an entry to `sources.yaml`:

```yaml
- id: short-unique-id
  title: Full title
  publisher: Who published it
  url: https://where-it-comes-from
  licence: public-domain-us-federal      # an identifier from build/licences.yaml
  evidence: "Distribution Statement A on the cover; US Navy work"
  status: check                          # cleared | check | excluded
  retrieved: null                        # YYYY-MM-DD once fetched
  files: []                              # path + sha256, filled when the source is ingested (phase 3)
```

Use `status: excluded` (with the reason in `evidence`) for sources we looked at
and rejected, so nobody checks them again.

Then run `make sources` to regenerate [docs/SOURCES.md](docs/SOURCES.md).
`make check` fails while that file is out of date.

## Add a free manual to the private shelf

Free manuals published by engine makers stay copyrighted, so they go in
[scripts/private_downloads.yaml](scripts/private_downloads.yaml), never in
`sources.yaml`. List only manufacturer sites, or owner associations re-hosting
a maker's own document. Test with
`python3 scripts/fetch_private.py --only <group>`.

## Add a local Wikipedia shelf

A shelf is a plain text file `wikipedia/<lang>/<region>.txt` with one article
title per line, exactly as in the article URL but with spaces. Describe the
shelf in [wikipedia/README.md](wikipedia/README.md). Check every title exists
before opening the pull request.

## Code

Build code is Apache-2.0. Keep it dependency-light: the output must open in old
Kiwix readers, so pages use no JavaScript.
