# Open Seamanship

A free, open, offline knowledge pack for everyone who works or sails at sea:
yachtsmen, fishermen, workboat, ferry and merchant crews. Emergencies,
troubleshooting, seamanship, navigation, weather, marine engines of every
size, boat systems, naval architecture, health at sea and maritime history.

It is built for someone on a boat, or ashore after the grid has gone, with no
internet and a problem to solve. It ships as a [Kiwix](https://kiwix.org) ZIM
file and as a community add-on for
[Project N.O.M.A.D.](https://github.com/Crosstalk-Solutions/project-nomad).

> **Status (October 2026): first full draft, not yet reviewed by people.**
> About 110 pages cover every section, each citing its sources down to the
> page; safety-critical pages have been fact-checked once by an independent
> pass, but **no page has been reviewed by a human expert yet**, so every page
> is marked "Unreviewed". The library holds 53 openly licensed documents
> (about 1.8 GB). Do not rely on this pack at sea until pages are reviewed.
> See [docs/ROADMAP.md](docs/ROADMAP.md).

## What is inside

| Layer | What it is | Who writes it | Status |
| --- | --- | --- | --- |
| Emergency cards | One screen, numbered actions, act in seconds | Us, reviewed by practitioners | 12 drafts, fact-checked |
| Guides and explainers | Fix it, run the boat, health, know your boat, tables, regions, history | Us, reviewed by practitioners | About 100 drafts ([plan](docs/PAGE_PLAN.md)) |
| Library | Public-domain and openly licensed manuals, one page each with licence and evidence | US, UK, French and EU public bodies; old books | 53 documents in the pack ([sources](docs/SOURCES.md)) |
| Local Wikipedia shelves | Curated regional articles, one small ZIM per shelf | Wikipedia contributors | 4 shelves ([wikipedia/](wikipedia/README.md)) |
| Private shelf | Manuals you own but may not share, packed for your own use | Engine makers | Working |

Coverage is layered: an international core, then Europe (Brittany first, then
the French Mediterranean and the UK south coast), then other regions as open
sources allow. English first; the French edition starts after English v1.0.

## Quick start

Requirements: Python 3.11+ (or Docker) and git.

```sh
git clone https://github.com/SebastienTr/open-seamanship.git
cd open-seamanship
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
make all PYTHON=.venv/bin/python
```

The ZIM lands in `dist/`. Open it with any Kiwix reader.

| Command | What it does |
| --- | --- |
| `make check` | Validate pages, licences, the sources manifest and `docs/SOURCES.md` |
| `make test` | Run the test suite |
| `make site` | Build the static HTML into `dist/site/en/` |
| `make zim` | Pack the site into `dist/open-seamanship_en_<version>.zim` |
| `make all` | Tests, then site and ZIM |
| `make sources` | Regenerate `docs/SOURCES.md` from `sources.yaml` and `sources.d/` |
| `make fetch-library` | Download the library files into `library/` and check their SHA-256 |
| `make fetch-private` | Download free official engine manuals into `private/` |
| `make private` | Pack `private/` into a personal ZIM in `dist/private/` |
| `make dashboard` | Assemble the N.O.M.A.D. dashboard image context in `dist/dashboard/` |
| `make dashboard-image` | Build the dashboard Docker image |

Two build modes: `MODE=release` (default for `make`) keeps only reviewed pages;
`MODE=preview` also includes drafts, each marked "Unreviewed" on the page.
Run `make fetch-library` first to put the library documents in the pack.

With Docker, nothing else is needed:

```sh
docker build -t open-seamanship .
docker run --rm -v "$PWD/dist:/work/dist" open-seamanship make all
```

## Private shelf

Engine makers publish many manuals for free, but they stay copyrighted, so
they can never be in the public pack. `make fetch-private` downloads the ones
listed in [scripts/private_downloads.yaml](scripts/private_downloads.yaml)
(Westerbeke/Universal technical manuals, Kohler KDW workshop manual, Solé,
Beta, Vetus, Yanmar, Tohatsu, Yamaha, Volvo Penta MD2000 series) into
`private/`. Add your own documents and notes there too, then `make private`
packs everything into a personal ZIM. Git ignores `private/`, CI never sees it,
and the public build never reads it. See [private/README.md](private/README.md).

## Install on Project N.O.M.A.D.

One command on the N.O.M.A.D. host does everything, and is safe to run again
at any time (after `git pull`, for example):

```sh
git clone https://github.com/SebastienTr/open-seamanship.git
cd open-seamanship
sudo ./install.sh
```

In order, it:

1. downloads the library (only the files not already there, each checked
   against its SHA-256);
2. downloads the free official engine manuals into `private/` and packs your
   private shelf (never published);
3. builds the local Wikipedia shelves with MWoffliner (in Docker), except for a
   language whose full Wikipedia is already in the Kiwix library: the
   dashboard then opens the curated articles straight in it;
4. builds the pack ZIM;
5. installs every ZIM into the Kiwix library (`/opt/project-nomad/storage/zim`),
   replaces older builds and asks N.O.M.A.D. to rescan;
6. builds the dashboard and registers it as a N.O.M.A.D. app, so
   **Open Seamanship** appears on the Command Center home page.

Each run also removes what is no longer used: library files dropped from the
sources, older pack builds, unneeded Wikipedia shelves and old dashboard
images (your own files in `private/` are never touched). A failed download
does not stop the rest; the warnings are listed at the end,
and running the command again fetches what is still missing. Some engine
manuals must be downloaded by hand: the script prints the link and where to
save each one.

| Option | Effect |
| --- | --- |
| `--clean` | delete downloads and builds first, then download everything again (your own files in `private/` stay) |
| `--release` | pack reviewed pages only (default: preview, drafts marked "Unreviewed") |
| `--no-library`, `--no-private`, `--no-wikipedia`, `--no-dashboard` | skip that step |
| `--no-deploy` | build only, install nothing |
| `--port`, `--api`, `--library`, `--container` | dashboard port (8620), N.O.M.A.D. admin URL, Kiwix folder and container |

The dashboard: distress channels and the Mayday call, one search box across
the pack, the library, your private shelf and the Wikipedia shelves, the
pack's sections, your Kiwix libraries, the local Wikipedia shelves (curated
articles for each coast, opened in your full Wikipedia if you have one), and tools (unit converter, fuel and
range, tide height by the rule of twelfths, Beaufort scale), with day, dusk
and red night modes. It runs as a small nginx container on port 8620,
registered through N.O.M.A.D.'s own app API, so it can be stopped or removed in
the Supply Depot. How it works: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

The first run downloads about 2 GB for the library and builds a pack of about
1.5 GB, plus the private shelf (about 300 MB) and the Wikipedia shelves. Search
finds private PDFs by file and folder name, so name your own files well (for
example `private/volvo-penta-md2000/MD2020-workshop-notes.pdf`).

## Repository layout

```
content/en/          written pages (Markdown + front matter), one folder per section
content/assets.yaml  licence record for every image or file under content/
sources.yaml         every library source: URL, licence, evidence, status, files and SHA-256
sources.d/           more sources, one file per topic (same format)
library/             downloaded library files (ignored by git; make fetch-library)
docs/                page template, page plan, roadmap, architecture, generated SOURCES.md
build/osp/           the build: validation, site generator, ZIM packer, private shelf
build/templates/     HTML template (no JavaScript)
dashboard/           N.O.M.A.D. dashboard (HTML, CSS, JS) and its nginx image
scripts/             fetch_library.py, fetch_private.py, build_wikipedia.py
wikipedia/           local Wikipedia shelves (article lists)
private/             your private shelf (ignored by git)
tests/               test suite (Python, plus tests/js for the dashboard maths)
install.sh           one-command N.O.M.A.D. installer
```

## Contributing

Read [CONTENT_POLICY.md](CONTENT_POLICY.md) (licences, accuracy, review) and
[CONTRIBUTING.md](CONTRIBUTING.md) (how to add a page or a source). Every page
follows [docs/PAGE_TEMPLATE.md](docs/PAGE_TEMPLATE.md).

## Licences

- Our own text and drawings: [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt).
- Build code: [Apache-2.0](LICENSES/Apache-2.0.txt).
- Library documents and Wikipedia articles keep their own licence, recorded in
  [sources.yaml](sources.yaml) (readable as [docs/SOURCES.md](docs/SOURCES.md))
  and shown on every page.

This pack does not replace training, official publications or local rules.
