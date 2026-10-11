# Local Wikipedia shelves

Each shelf is a curated list of Wikipedia articles for one region, in that
region's language. The build turns each list into its own small ZIM with
openZIM's [MWoffliner](https://github.com/openzim/mwoffliner) (`--articleList`),
so readers install only the regions they sail.

Article text is CC BY-SA 4.0; each image keeps its own Wikimedia Commons licence.

| File | Region | Language | Status |
| --- | --- | --- | --- |
| `fr/bretagne.txt` | Brittany | French | Seed list, titles not yet checked |
| `fr/mediterranee.txt` | French Mediterranean | French | To do |
| `en/uk-south-coast.txt` | UK south coast | English | To do |

## What a shelf holds

Coasts, harbours and anchorages, lighthouses, local winds and sea states,
tidal races, traditional local boats, rescue stations, shipwrecks, maritime
museums and local maritime history.

## Format

One title per line, spaces not underscores, exactly as Wikipedia spells it.
No comments or blank lines: MWoffliner reads every line as a title. Keep notes
in this README instead.

## Checking titles

Phase 5 adds `scripts/check_wikipedia.py`, which confirms each title exists and
follows redirects. Until then, the seed lists below are unverified.
