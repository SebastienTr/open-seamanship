# Architecture

## Build pipeline

```
content/<lang>/*.md ─┐
sources.yaml ────────┼─▶ validate (build/osp/pages.py) ─▶ render (site.py) ─▶ dist/site/<lang>/
content/assets.yaml ─┘         licences, sources,          Jinja template,      ─▶ pack (zim.py)
                               review status, regions      no JavaScript         ─▶ dist/*.zim
```

- **Validation** (`make check`) fails on: a page or file without an accepted
  licence, a page without sources or locators, a cited source that is excluded
  (or not yet cleared, in a release build), too few reviewers for the page's
  safety level, an author reviewing their own page, an unknown region or field,
  a malformed Wikipedia shelf, and a stale `docs/SOURCES.md`.
- **Rendering**: one HTML page per Markdown file, section index pages, an A-Z
  index and a home page with one tile per section. Draft pages appear only in
  preview builds, marked "Unreviewed".
- **Packing**: python-libzim with full-text and title indexes, ZIM metadata
  (name, language, licence, version, 48×48 icon).
- **Determinism**: version and date come from git (or `OSP_VERSION` and
  `SOURCE_DATE_EPOCH`), never from the clock, so the same commit gives the same
  HTML. The ZIM file itself differs between builds because libzim writes a
  random identifier; its content is identical.

## Private shelf

`scripts/fetch_private.py` reads `scripts/private_downloads.yaml` and saves
free official manuals into `private/<group>/`. Resolvers handle direct links,
FlowPaper viewer pages (Beta Marine), web pages listing PDFs (Westerbeke) and
the Tohatsu manual catalogue (JSON). Each file is checked to be a PDF, skipped
if identical to one already present, and logged with its SHA-256 in
`private/DOWNLOADS.tsv`. Some sites refuse automated downloads (Yanmar
answered HTTP 403 in October 2026); those are reported, not fatal.

`make private` (`build/osp/private.py`) packs `private/` into
`dist/private/open-seamanship-private_<date>.zim`: an index page grouped by
folder, Markdown notes rendered as pages, PDFs findable by title (their text is
not full-text indexed). `private/` is ignored by git and never read by the
public build; a test checks that.

## Delivery through the N.O.M.A.D. Supply Depot

Goal: install the pack from N.O.M.A.D.'s app catalogue and have it appear on
the home page. Findings from N.O.M.A.D. v1.35.1 (October 2026):

- The home page (`admin/inertia/pages/home.tsx`) shows a tile for every
  installed service that has a launch location (`ui_location` or
  `custom_url`).
- A Supply Depot **custom app** gets its launch location from its first host
  port (`buildCustomContainerConfig` in
  `admin/app/controllers/system_controller.ts`). So any installed custom app
  with a port gets a home tile, with no change to N.O.M.A.D.
- A **ZIM file** never gets its own tile; it appears inside the Kiwix library.
  Kiwix only sees a new file after a library rebuild
  (`POST /api/zim/rescan-library`, or **Rescan Library** in the UI).
- Custom-app bind mounts inside N.O.M.A.D.'s storage root
  (`/opt/project-nomad/storage` by default) are accepted without warning
  (`admin/app/services/custom_app_guard.ts`).
- Tile icons come from a fixed list (`admin/inertia/lib/icons.ts`); there is no
  anchor or boat icon. A custom app has no description field, so its tile shows
  a generic description.

Planned design, a small "Mariner" app:

1. The container image carries the written pack as a static website, so its
   home tile works as soon as it starts.
2. On first start, while online, it fetches the large libraries into
   `storage/mariner` with checksums, resuming if interrupted, and shows
   progress on a status page.
3. It writes the Open Seamanship ZIM into `storage/zim` and asks N.O.M.A.D. to
   rescan the Kiwix library, or tells the user to press **Rescan Library**.
4. The private shelf is never in the image.

Longer term, with the maintainers' agreement: a curated Supply Depot entry, an
anchor icon, and a Maritime category in N.O.M.A.D.'s curated content
(`collections/kiwix-categories.json`, whose ZIMs are all hosted on
download.kiwix.org, so Open Seamanship would first need a place in the Kiwix
catalogue).
