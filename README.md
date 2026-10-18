# Open Seamanship

A free, open, offline knowledge pack about the sea and boats: emergencies,
troubleshooting, seamanship, navigation, weather, marine engines, boat systems,
naval architecture, health at sea and maritime history.

It is built for someone on a boat, or ashore after the grid has gone, with no
internet and a problem to solve. It ships as a [Kiwix](https://kiwix.org) ZIM
file, as a community add-on for
[Project N.O.M.A.D.](https://github.com/Crosstalk-Solutions/project-nomad), and
as a printable PDF and an EPUB built from the same source.

> **Status: phase 1 (foundations).** The build works end to end, but there is
> no reviewed content yet. Nothing in a preview build should be relied on at sea.

## What is inside

| Layer | What it is | Who writes it |
| --- | --- | --- |
| Emergency cards | One screen, numbered actions, act in seconds | Us, reviewed by practitioners |
| Guides | Symptom first, then causes, fixes and "if that fails" | Us, reviewed by practitioners |
| Library | Full public-domain and openly licensed manuals | Original authors (US, UK, French and EU public bodies, old books) |
| Local Wikipedia shelves | Curated regional articles, one small ZIM per region | Wikipedia contributors |

Coverage is layered: an international core, then Europe (Brittany first, then
the French Mediterranean and the UK south coast), then other regions as open
sources allow. English first; the French edition starts after English v1.0.

## Build

Requirements: Python 3.11+ (or Docker), about 1 GB of free disk for now.

```sh
make check      # validate pages, licences and the sources manifest
make site       # build the static HTML into dist/site/
make zim        # pack dist/site/ into dist/open-seamanship_en_<version>.zim
make all        # all of the above
```

Two build modes:

- `MODE=release` (default) includes only pages with review status `reviewed`
  or `verified`.
- `MODE=preview` includes drafts, each marked "Unreviewed" on the page.

With Docker, nothing else is needed:

```sh
docker build -t open-seamanship .
docker run --rm -v "$PWD/dist:/work/dist" open-seamanship make all
```

## Private shelf

Manuals you own but may not share, such as your engine maker's owner's or
workshop manual, go in `private/`. `make private` packs them, with your own
notes, into a separate ZIM in `dist/private/`. Git ignores that folder and the
public pack never reads it. See [private/README.md](private/README.md).

## Install on Project N.O.M.A.D.

On the NOMAD host:

```sh
git clone https://github.com/<owner>/open-seamanship.git
cd open-seamanship
sudo ./install.sh --deploy
```

`install.sh` builds the ZIM (or uses a prebuilt one with `--zim FILE`), copies
it into the Kiwix library (`/opt/project-nomad/storage/zim` by default) and
restarts the Kiwix container (`nomad_kiwix_server` by default). Run
`./install.sh --help` for options. If the new pack does not appear, use
**Content Manager → Rescan Library** in NOMAD.

## Contributing

Read [CONTENT_POLICY.md](CONTENT_POLICY.md) (licences, accuracy, review) and
[CONTRIBUTING.md](CONTRIBUTING.md) (how to add a page or a source). Every page
follows [docs/PAGE_TEMPLATE.md](docs/PAGE_TEMPLATE.md).

## Licences

- Our own text and drawings: [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt).
- Build code: [Apache-2.0](LICENSES/Apache-2.0.txt).
- Library documents and Wikipedia articles keep their own licence, recorded in
  [sources.yaml](sources.yaml) and shown on every page.

This pack does not replace training, official publications or local rules.
