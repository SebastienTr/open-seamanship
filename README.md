# Open Seamanship

A free, open, offline knowledge pack for everyone who works or sails at sea:
yachtsmen, fishermen, workboat, ferry and merchant crews. Emergencies,
troubleshooting, seamanship, navigation, weather, marine engines of every
size, boat systems, naval architecture, health at sea and maritime history.

It is built for someone on a boat, or ashore after the grid has gone, with no
internet and a problem to solve. It ships as a [Kiwix](https://kiwix.org) ZIM
file and as a community add-on for
[Project N.O.M.A.D.](https://github.com/Crosstalk-Solutions/project-nomad).

> **Status (October 2026): foundations done, no reviewed content yet.**
> The build, licence checks and packaging work end to end, and about 100
> sources are mapped, half of them already cleared. Written pages come next.
> Nothing in a preview build should be relied on at sea. See [docs/ROADMAP.md](docs/ROADMAP.md).

## What is inside

| Layer | What it is | Who writes it | Status |
| --- | --- | --- | --- |
| Emergency cards | One screen, numbered actions, act in seconds | Us, reviewed by practitioners | Not started |
| Guides | Symptom first, then causes, fixes and "if that fails" | Us, reviewed by practitioners | Not started |
| Library | Public-domain and openly licensed manuals | US, UK, French and EU public bodies; old books | [sources mapped](docs/SOURCES.md), not yet ingested |
| Local Wikipedia shelves | Curated regional articles, one small ZIM per region | Wikipedia contributors | Brittany seed list |
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
| `make sources` | Regenerate `docs/SOURCES.md` from `sources.yaml` |
| `make fetch-private` | Download free official engine manuals into `private/` |
| `make private` | Pack `private/` into a personal ZIM in `dist/private/` |

Two build modes: `MODE=release` (default) keeps only reviewed pages;
`MODE=preview` also includes drafts, each marked "Unreviewed" on the page.

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

Today, as a ZIM, following N.O.M.A.D.'s community add-on convention. On the
N.O.M.A.D. host:

```sh
git clone https://github.com/SebastienTr/open-seamanship.git
cd open-seamanship
sudo ./install.sh --deploy
```

`install.sh` builds the ZIM (or uses a prebuilt one with `--zim FILE`), copies
it into the Kiwix library (`/opt/project-nomad/storage/zim` by default) and
restarts the Kiwix container (`nomad_kiwix_server` by default). Run
`./install.sh --help` for options. If the pack does not appear, use
**Content Manager → Rescan Library**.

Next: a Supply Depot app, so the pack installs from N.O.M.A.D.'s app catalogue
and gets its own tile on the home page. The design, based on N.O.M.A.D.'s code,
is in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md#delivery-through-the-nomad-supply-depot).

## Repository layout

```
content/en/          written pages (Markdown + front matter), one folder per section
content/assets.yaml  licence record for every image or file under content/
sources.yaml         every library source: URL, licence, evidence, status
docs/                page template, roadmap, architecture, generated SOURCES.md
build/osp/           the build: validation, site generator, ZIM packer, private shelf
build/templates/     HTML template (no JavaScript)
scripts/             fetch_private.py and its download list
wikipedia/           local Wikipedia shelves (article lists)
private/             your private shelf (ignored by git)
tests/               test suite
install.sh           N.O.M.A.D. installer
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
