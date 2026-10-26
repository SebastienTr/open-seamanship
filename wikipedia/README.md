# Local Wikipedia shelves

Each shelf is a curated list of Wikipedia articles for one region, in that
region's language. The build turns each list into its own small ZIM with
openZIM's [MWoffliner](https://github.com/openzim/mwoffliner) (`--articleList`),
so readers install only the regions they sail.

Article text is CC BY-SA 4.0; each image keeps its own Wikimedia Commons licence.

| File | Region | Language | Articles | Status |
| --- | --- | --- | --- | --- |
| `fr/bretagne.txt` | Brittany | French | 150 | Titles verified 2026-10-26 |
| `fr/mediterranee.txt` | French Mediterranean and Corsica | French | 111 | Titles verified 2026-10-26 |
| `en/uk-south-coast.txt` | UK south coast and Channel Islands | English | 116 | Titles verified 2026-10-26 |
| `en/seamanship-core.txt` | International reference | English | 170 | Titles verified 2026-10-26 |

ZIM titles, descriptions, languages and region codes live in `shelves.yaml`.

## What a shelf holds

Coasts, harbours and anchorages, lighthouses, local winds and sea states,
tidal races, traditional local boats, rescue stations, shipwrecks, maritime
museums and local maritime history.

`en/seamanship-core.txt` is the one shelf not tied to a coast: international
reference articles (collision rules, weather, tides, knots, rigs, engines,
radio and distress, navigation, sea survival and first aid, fishing methods,
stability, and shipwrecks that changed the rules).

## Format

One title per line, spaces not underscores, exactly as Wikipedia spells it.
No comments or blank lines: MWoffliner reads every line as a title. Keep notes
in this README instead.

## Checking titles

Every title was checked on 2026-10-26 against the MediaWiki API of its
Wikipedia (`action=query&redirects=1&prop=pageprops`, 50 titles per request).
Because the API was rate-limiting, the lists were also resolved against the
Wikimedia dumps (`pages-articles-multistream-index`, `redirect` and
`page_props` tables; frwiki of 2026-10-01, enwiki of 2026-10-08); where both
ran, they agreed title for title. Redirects and normalisation were followed
and the canonical title written to the list; missing pages, disambiguation
pages and duplicates were dropped, and redirects that landed on an unrelated
article were replaced by hand. Re-run the check before each release, since
articles get renamed.
