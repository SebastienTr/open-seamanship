# Roadmap

Each phase ends with a gate; the next starts only when the gate passes. The
French edition starts after English v1.0 is released.

| Phase | What | Gate | Status |
| --- | --- | --- | --- |
| 1. Foundations | Licence policy, page template, sources manifest, build, CI, installer | An empty pack builds from a clean clone | **Done** (v0.0.1, October 2026) |
| 1b. Private shelf | Owned manuals packed into a personal, never-published ZIM; downloader for free official manuals | Private ZIM opens in Kiwix | **Done** |
| 2. First draft | Every page of [PAGE_PLAN.md](PAGE_PLAN.md) written with cited sources; safety-critical pages fact-checked by an independent pass | All pages build, no broken link | **Done** (October 2026), all pages `draft` |
| 3. Library | Ingest every cleared source with checksums; convert the most-used manuals to HTML | 100% of files pass the licence check | **Ingested**: 53 documents shipped; 24 sources still to settle (third-party figures, licence questions); HTML conversion not started |
| 4. Human review | Practitioners review emergency, health, engine, electrical and heavy-weather pages first, then the rest | Each page reviewed or verified | **Next**: nothing reviewed yet; the open questions are in each page's Uncertain boxes |
| 5. Tables and tools | Almanac, conversions, signals, lights, glossary, history shelf, local Wikipedia shelves | Computed tables match an independent check | Tables written; Wikipedia shelves built by `install.sh`; almanac not started |
| 6. N.O.M.A.D. app | Mariner dashboard with its own tile on the Command Center home page; one-command install of everything | Installs and shows on the home page | **Done** (`sudo ./install.sh`); a published image for the Supply Depot catalogue is next |
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
- Library files with third-party figures (9 Navy and Army manuals, two MCA
  fishing guides, COSWP): remove the credited figures and ship, or keep them
  reference-only.
- Bowditch 2024 and Pub. 229: NGA reserves rights outside the US and Pub. 229
  is a joint work with HM Nautical Almanac Office; reference-only until
  settled.
- Sites that refuse scripted downloads (NavCen, everyspec, dco.uscg.mil): the
  current Navigation Rules handbook stays reference-only; the official UK text
  (MSN 1781) is cited instead.
