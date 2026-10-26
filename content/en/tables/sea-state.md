---
title: Sea state (Douglas / WMO)
summary: Sea state code 0 to 9 with wave heights in metres and feet, the French terms used in forecasts, the swell scale, and what a forecast wave height really means.
kind: explainer
section: tables
region: international
language: en
licence: CC-BY-SA-4.0
safety: normal
status: draft
authors: [claude]
reviewers: []
reviewed: null
sources:
  - id: bowditch
    locator: "Vol. 1 (2024 ed.), ch. 41, Table 4112 'Beaufort wind scale with corresponding sea codes', p. 707 (PDF p. 719); ch. 38 'Waves, breakers and surf', section 3802 (table of relative wave heights) and section 3804 (effects of current), p. 634 (PDF p. 646)"
  - id: wikipedia-en
    locator: "Sea state, section 'WMO sea state code'; Douglas sea scale, sections 'State of the sea (wind sea)' and 'Swell'"
  - id: wikipedia-fr
    locator: "État de la mer, section 'Description de l'état de la mer' (French terms, force 0-9 with heights in metres)"
uncertain:
  - "The feet column is converted from the metre limits and rounded. Bowditch Table 4112 gives the same feet values from code 4 up (4-8, 8-13, 13-20, 20-30, 30-45, 45 and over) but slightly different, rounded figures for codes 1 to 3."
  - "The swell part of the Douglas scale is given in different words by different services. The wavelength and height limits below come from the Wikipedia article only; treat them as indicative."
  - "Some services give wave heights in metres instead of, or as well as, a code word; the words may then be used loosely."
---

Forecasts describe the sea with a code from 0 to 9, or with the word that goes
with each code: "slight", "moderate", "rough" and so on. The World
Meteorological Organization (WMO) code largely follows the wind-sea part of
the Douglas scale ([Sea state, wikipedia-en](../library/wikipedia-en.html)).
The height is that of the waves made by the local wind, not the swell.

## Sea state code (wind sea)

| Code | English | French forecast term | Wave height (m) | Wave height (ft) |
| --- | --- | --- | --- | --- |
| 0 | Calm (glassy) | calme | 0 | 0 |
| 1 | Calm (rippled) | ridée | 0-0.1 | 0-⅓ |
| 2 | Smooth (wavelets) | belle | 0.1-0.5 | ⅓-1½ |
| 3 | Slight | peu agitée | 0.5-1.25 | 1½-4 |
| 4 | Moderate | agitée | 1.25-2.5 | 4-8 |
| 5 | Rough | forte | 2.5-4 | 8-13 |
| 6 | Very rough | très forte | 4-6 | 13-20 |
| 7 | High | grosse | 6-9 | 20-30 |
| 8 | Very high | très grosse | 9-14 | 30-45 |
| 9 | Phenomenal | énorme | over 14 | over 45 |

Metres and English terms: Wikipedia "Sea state" and "Douglas sea scale". French
terms: Wikipedia "État de la mer". Feet: converted from metres, matching
Bowditch Table 4112 from code 4 up.

Bowditch Table 4112 lines the codes up with the wind: roughly code 3 with
force 4, code 4 with force 5, code 5 with force 6, code 6 with forces 7 to 9,
code 7 with force 10, code 8 with force 11 and code 9 with force 12. This
holds only after a long blow over open water; see
[Beaufort scale](beaufort-scale.html).

## Swell (Douglas scale)

Swell is made by wind somewhere else. It runs long and regular, often from a
different direction from the wind sea.

| Degree | Swell | Wave length | Wave height |
| --- | --- | --- | --- |
| 0 | No swell | | |
| 1 | Very low | short or average | low (under 2 m) |
| 2 | Low | long | low |
| 3 | Light | short | moderate (2-4 m) |
| 4 | Moderate | average | moderate |
| 5 | Moderate rough | long | moderate |
| 6 | Rough | short | high (over 4 m) |
| 7 | High | average | high |
| 8 | Very high | long | high |
| 9 | Confused | cannot be defined | cannot be defined |

Short means under 100 m (330 ft), average 100-200 m, long over 200 m
(660 ft) ([Douglas sea scale, wikipedia-en](../library/wikipedia-en.html)).

## What a forecast wave height means

A forecast or reported wave height is the **significant wave height**: the
average height of the highest third of the waves. Observers' estimates come
out at about this value ([Bowditch vol. 1, section 3802](../library/bowditch.html)).
Many waves are smaller, and some are much bigger:

| Wave | Height compared with the significant height |
| --- | --- |
| Average wave | 0.64 × |
| Significant wave (the forecast figure) | 1 × |
| Average of the highest 10 % | 1.29 × |
| Highest wave | 1.87 × |

So with a forecast of 3 m, expect some waves near 4 m and the odd wave near
5.5 m (18 ft).

A current running against the waves makes them shorter and higher; a current
running with them makes them longer and lower (Bowditch section 3804). Waves
also steepen and break over shoals and bars. Expect the worst sea where wind
meets tide, at headlands and races, and at harbour entrances; see
[Tides and tidal streams](../run-the-boat/tides-and-tidal-streams.html).

## See also

- [Beaufort scale](beaufort-scale.html)
- [Reading the weather](../run-the-boat/reading-the-weather.html)
- [Heavy weather](../run-the-boat/heavy-weather.html)
- [France: marine weather bulletins](../regions/france-weather-bulletins.html)
