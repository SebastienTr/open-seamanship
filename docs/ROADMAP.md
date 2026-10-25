# Roadmap

Each phase ends with a gate; the next starts only when the gate passes. The
French edition starts after English v1.0 is released.

| Phase | What | Gate | Status |
| --- | --- | --- | --- |
| 1. Foundations | Licence policy, page template, sources manifest, build, CI, installer | An empty pack builds from a clean clone | **Done** (v0.0.1, October 2026) |
| 1b. Private shelf | Owned manuals packed into a personal, never-published ZIM; downloader for free official manuals | Private ZIM opens in Kiwix | **Done** |
| 2. Pilot slice | 5 emergency cards, "engine won't start" and "engine overheating" trees, Bowditch and the COLREGs in the library | Installs on N.O.M.A.D., opens on a phone offline, PDF prints; cards reviewed | Next |
| 3. Library | Ingest every cleared source with checksums; convert the most-used manuals to HTML | 100% of files pass the licence check | Sources mapped ([docs/SOURCES.md](SOURCES.md)) |
| 4. Guides | Emergency, Fix it, Run the boat, Health, Know your boat; then fishing and engine-room guides | Each page reviewed or verified | Not started |
| 5. Tables and tools | Almanac, conversions, signals, lights, glossary, history shelf, local Wikipedia shelves | Computed tables match an independent check | Not started |
| 6. N.O.M.A.D. app | Mariner dashboard with its own tile on the Command Center home page; later, libraries fetched on first start and a published image | Installs and shows on the home page | **Dashboard done** (`install.sh --dashboard`); fetch and publishing next ([ARCHITECTURE.md](ARCHITECTURE.md#the-dashboard-app-built)) |
| 7. English v1.0 | Full link and licence audit; ZIM, PDF and EPUB release | No open safety-critical issue | — |
| 8. French edition | Translate our pages; French sources under Licence Ouverte | Same review rules | — |

## Audience

Widened in October 2026 from leisure sailors to all mariners: yachtsmen,
fishermen, workboat, ferry and merchant crews. Written guides start with small
craft, then add fishing boats and the engine rooms of larger vessels, with
diesels from 10 hp to ship engines.

## Open decisions

- Reviewers for engines, electrical and medical pages.
- Whether public pages may cite makers' manuals for facts only (intervals,
  clearances, torques), in our own words.
- Regions after Europe.
- A boat or anchor icon for the home tile (needs a change in N.O.M.A.D.).
