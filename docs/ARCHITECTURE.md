# Architecture

## Build pipeline

```
content/<lang>/*.md ─┐
sources.yaml (+ .d) ─┼─▶ validate (build/osp/pages.py) ─▶ render (site.py) ─▶ dist/site/<lang>/
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

## Library

`scripts/fetch_library.py` downloads every `files` entry of the cleared
sources (`sources.yaml` and `sources.d/*.yaml`) into `library/<id>/`, checks
the SHA-256 of each and keeps only matching files (`--verify` re-hashes,
`--clean` starts again). The build (`build/osp/library.py`) then publishes:

- `library/index.html`: every source that is shipped or cited, with its licence;
- `library/<id>.html` for every citable source: licence, evidence, origin,
  SHA-256, the files, and the pages that cite it (pages link here from their
  citations, so a source never needs to be in the pack to be cited);
- `library/files/<id>/…`: the files themselves, hard-linked from the cache.
  Project Gutenberg HTML books (`-h.zip`) are unpacked and their main page
  linked. PDFs get the source title as their ZIM title, so title search finds
  them.

A file is shipped only if its source is `cleared`, has no `third_party`
material, and is present with the recorded size. Files over 400 MB are listed
with `skip: too-large` and not fetched. The dashboard image leaves
`library/files/` out and nginx serves it from the pack ZIM in Kiwix
(`OSP_PACK_BOOK`, set at build time to the matching ZIM name).

The build also checks every relative link in the pages it writes and fails on
a broken one.

## Local Wikipedia shelves

`scripts/build_wikipedia.py` turns each `wikipedia/<lang>/<shelf>.txt` into
`dist/wikipedia/open-seamanship-wiki_<lang>_<shelf>.zim` with openZIM's
MWoffliner (Docker image `ghcr.io/openzim/mwoffliner:2.1.1`, `--pageList`,
WebP images, metadata from `wikipedia/shelves.yaml`). A shelf is rebuilt only
when its list is newer than its ZIM. Wikipedia rate-limits busy addresses; a
failed shelf is retried on the next run.

## One-command install

`install.sh` runs, in order: library download, private shelf download and
pack, Wikipedia shelves, pack build (preview by default), install of every ZIM
into the Kiwix library with older builds removed, a library rescan through
the N.O.M.A.D. API and a Kiwix restart, then the dashboard image build and its
registration as a custom app. Downloads and builds run as the invoking user
(`SUDO_USER`); only the copy into the Kiwix folder and Docker need root. A
failed download is a warning, not an error. `--clean` deletes `dist/`,
`library/` and the files `fetch_private.py` downloaded (listed in
`private/DOWNLOADS.tsv`), never the user's own files.

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

### The dashboard app (built)

`./install.sh --dashboard` installs **Open Seamanship** as a N.O.M.A.D. custom
app, so it gets a tile on the Command Center home page. The tile opens a
dashboard made for mariners.

- **Image.** `make dashboard` assembles `dist/dashboard/`: the dashboard
  (`dashboard/*.html|css|js`), the pack as a static site under `/pack/`, and
  `sections.json` (section tiles with page counts). `make dashboard-image`
  builds `open-seamanship-dashboard:<version>` from `nginx:1.27-alpine`. The
  private shelf is never in the image (a test checks it).
- **Registration.** `install.sh` builds the image locally, then calls the
  N.O.M.A.D. admin API, which has no authentication on the host:
  `GET /api/system/services/custom/nomad_custom_open_seamanship`, then
  `POST /api/system/services/custom` (create) or `PUT` (update, which
  recreates the container). The payload: name "Open Seamanship", host port
  8620 → container 80, category `education`, icon `IconMap`, 128 MB, `force`.
  The image is local and pinned to a version, so N.O.M.A.D. does not pull it
  and its guard raises no "moving tag" warning. N.O.M.A.D. attaches custom
  containers to `project-nomad_default` in production.
- **Same-origin proxy.** nginx resolves the N.O.M.A.D. containers at request
  time (Docker DNS `127.0.0.11`), so the dashboard starts even if they are
  down. It exposes only what the dashboard needs: `GET /kiwix/search`,
  `/kiwix/suggest`, `/kiwix/catalog/*` → `nomad_kiwix_server:8080`, and
  `POST /nomad/api/zim/rescan-library` → `nomad_admin:8080`. Upstreams, the
  Kiwix public port (8090) and URL are environment variables
  (`OSP_KIWIX_UPSTREAM`, `OSP_NOMAD_UPSTREAM`, `OSP_KIWIX_PORT`,
  `OSP_KIWIX_PUBLIC_URL`).
- **Search.** Per mariner book (Kiwix `Name` starting `open-seamanship`):
  title suggestions (`/suggest?content=<book path>`), which find PDF manuals,
  plus full-text search (`/search?books.id=<uuid>&format=xml`). Books are
  searched one by one so one bad index cannot fail the whole search. Results
  open in Kiwix on port 8090 (kiwix-serve pages use absolute paths, so they
  cannot be proxied under a sub-path). Note: `books.name` in kiwix-serve 3.8.1
  is the file-based path name, not the ZIM `Name` metadata, hence `books.id`.
- **Private shelf titles** include their folder ("Volvo penta md2000: …") so a
  search for the maker finds them.
- **Dashboard contents.** Distress panel (VHF 16, DSC 70, France 196, Mayday
  wording marked as an unreviewed draft), search, pack sections, libraries on
  this N.O.M.A.D. with a Rescan button, and tools: unit converter, fuel and
  range, rule-of-twelfths tide height, Beaufort scale. Day, dusk and red night
  modes. No external requests.
- **Tested** with kiwix-serve 3.8.1 serving the public and private ZIMs, a mock
  admin, and Playwright (day, night, phone). `tests/js/tide_test.js` checks the
  tide maths.

Still to do: fetch the large libraries on first start (into
`storage/zim`, with checksums), and publish the image so the Supply Depot can
install it without a local build.

Longer term, with the maintainers' agreement: a curated Supply Depot entry, an
anchor icon, and a Maritime category in N.O.M.A.D.'s curated content
(`collections/kiwix-categories.json`, whose ZIMs are all hosted on
download.kiwix.org, so Open Seamanship would first need a place in the Kiwix
catalogue).
