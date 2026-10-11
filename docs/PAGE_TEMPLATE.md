# Page template

Every written page is a Markdown file under `content/<lang>/<section>/` with a
YAML front matter block. `make check` validates every field.

## Front matter

```yaml
---
title: Engine overheating            # the words a worried person would type
summary: Temperature alarm or steam from the exhaust on a small marine diesel.
kind: guide                          # card | guide | explainer | history | structural
section: fix-it                      # see build/sections.yaml
region: international                # international | eu | fr | fr-bretagne | fr-mediterranee | uk | ...
language: en
licence: CC-BY-SA-4.0                # our own text; adapted text keeps the stricter licence
safety: critical                     # critical | normal
status: draft                        # draft | reviewed | verified
authors: [your-handle]
reviewers: []                        # handles; critical pages need two, one a practitioner
reviewed: null                       # YYYY-MM-DD of the last review
sources:                             # ids from sources.yaml, with an exact locator
  - id: navedtra-engineman
    locator: "chapter 6, pp. 6-12 to 6-15"
uncertain:                           # optional; each entry is shown in an "Uncertain" box
  - "Raw-water impeller life varies widely by make; no open source gives a figure."
local_wikipedia: []                  # optional; titles from a local shelf, shown in a box
---
```

`kind: structural` pages (home, about, indexes) need only `title`, `kind`,
`section`, `language` and `licence`.

## Body

Cards and guides use these headings, in this order. Leave out a heading only if
it truly does not apply.

```markdown
## Situation
When this page applies, in one or two sentences.

## Do now
1. One action per step, imperative, short.
2. Units in metric and imperial: 10 m (33 ft).

## Why
The reasoning, briefly. A reader under stress can skip it.

## Check that it worked
What the reader should see, hear or measure.

## If that fails
The next thing to try, or the page to go to.
```

Explainers and history pages are free-form prose, but still cite every fact.

## Style

- Plain English: short sentences, everyday words, readable by non-native speakers.
- Titles use the symptom, not the system: "Taking on water", not "Hull integrity".
- Write numbers as digits; give metric first, imperial in brackets.
- No brand names unless needed to identify a part; no advertising.
- Link to the library with the exact page: `[Bowditch, ch. 7](../library/bowditch.html#ch7)`.
