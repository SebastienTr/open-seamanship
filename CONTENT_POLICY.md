# Content policy

People may act on this pack at sea. These rules exist to keep it accurate and
legally redistributable by anyone, including people who sell N.O.M.A.D. boxes.
The build enforces the parts that a machine can check (`make check`).

## 1. Licences

### Accepted

Identifiers are the ones used in page front matter and in `sources.yaml`. The
machine-readable list is [build/licences.yaml](build/licences.yaml).

| Identifier | Meaning |
| --- | --- |
| `public-domain` | Out of copyright everywhere we ship (see the two tests below) |
| `public-domain-us-federal` | Work of the US federal government (17 U.S.C. § 105) |
| `CC0-1.0` | Creative Commons Zero |
| `CC-BY-4.0` | Creative Commons Attribution 4.0 (also most EU Commission and agency documents) |
| `CC-BY-SA-4.0` | Creative Commons Attribution-ShareAlike 4.0 (our own text, Wikipedia) |
| `OGL-UK-3.0` | UK Open Government Licence v3.0 |
| `etalab-2.0` | French Licence Ouverte / Open Licence 2.0 |
| `eu-reuse-2011-833` | EU documents reusable under Commission Decision 2011/833/EU, source acknowledged |

### Rejected

- Non-commercial (NC) and no-derivatives (ND) licences, in any version.
- "Free to download" with no licence, and anything sold.
- Gallica (BnF) scan files: the works may be public domain, but the BnF
  charges for commercial reuse of its scans. Use the same work from Internet
  Archive or Wikisource, or transcribe it.
- Paid data: Shom and UKHO charts and tide predictions, Météo-France products
  that are not open data, commercial almanacs, Bloc Marine, Les Glénans, RYA,
  engine makers' manuals.

### Public domain needs two tests

1. Out of copyright in the United States.
2. Author died more than 70 years ago (EU rule). For a work with several
   authors, the last one to die counts.

Record both facts (publication date, death dates) in `sources.yaml`.

### Special cases

- **US federal works** have no US copyright. Their status abroad is untested;
  we follow Wikimedia Commons and treat them as public domain, and record the
  risk here. US military manuals also need *Distribution Statement A*.
- **French public information** is reusable, normally under the Licence
  Ouverte 2.0. A brochure's text may be fine while its photos and drawings
  belong to third parties: check each image or redraw it.
- **UK OGL** requires the attribution line given by the publisher.
- **COLREGs** come from the US Coast Guard handbook (US law), not from IMO's
  own books. IALA buoyage pages are written by us from the facts.
- **Images** follow the same rules as text. No brand logos. Our own diagrams
  are SVG under CC BY-SA 4.0.

### Tracking

- Every library file and every image has an entry in `sources.yaml`: origin
  URL, SHA-256, licence, evidence of the licence, date retrieved.
- Every page declares its licence and sources in its front matter; the footer
  shows them.
- `make check` fails if a page, file or image has no recorded licence, or if a
  licence is not on the accepted list.

## 2. Accuracy

- Every number and every procedure cites a source, down to the chapter or page.
- Anything uncertain goes in an `uncertain:` entry in the front matter and is
  shown in a visible "Uncertain" box on the page, with the reason.
- Computed tables (almanac, conversions) are checked automatically against an
  independent published source for sample values.
- Medical pages never go beyond the doses in the source they cite, and start
  with "get radio medical advice" whenever that is possible.
- Every page says where it applies (`region:`) and the footer says the pack
  does not replace training and that local rules vary.

## 3. Review

| Status | Meaning | In a release build? |
| --- | --- | --- |
| `draft` | Written, not reviewed | No (preview only, marked "Unreviewed") |
| `reviewed` | Checked against its sources by the required reviewers | Yes |
| `verified` | Reviewed, and a practitioner has tried the procedure or checked the values in the field | Yes |

- `safety: critical` pages (emergency cards, medical, gas, electrical, heavy
  weather, navigation tables) need **two reviewers**, one of them a
  practitioner: an experienced skipper for seamanship, a marine engineer for
  engines and electrical, a doctor or paramedic for medical.
- `safety: normal` pages need one reviewer.
- A reviewer is never the page's main author.
- Any change to the substance of a reviewed page sets it back to `draft`.

## 4. Errata

Anyone can open an issue. Every page shows the pack version, so a reported
error can be traced and fixed in the next release. Safety-critical errata
block the next release until they are fixed.
