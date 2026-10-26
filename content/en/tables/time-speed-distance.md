---
title: Time, speed and distance
summary: Distance = speed × time, with ready tables in knots and nautical miles, the 6-minute and 3-minute rules, and speed over a measured mile.
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
    locator: "Vol. 2 (2024 ed.), Explanation of tables: Table 10 'Speed table for measured mile' (S = 3600/T) and Table 11 'Speed, time and distance' (D = ST/60), pp. 3-4 (PDF pp. 17-18); Appendix C, Length and Speed (1 NM = 1852 m = 2025.4 yd; 1 kn = 1.852 km/h), pp. 323-326 (PDF pp. 337-340); ch. 11, section 1101 (current alters course and speed over ground), p. 308 (PDF p. 322)"
  - id: navedtra-quartermaster-3-2-1976
    locator: "Ch. 15 (relative motion and the maneuvering board), '3-minute rule', pp. 244-245 (Internet Archive ERIC_ED132263, djvu text)"
uncertain:
  - "The 3-minute rule uses 2000 yards to the nautical mile; the true figure is about 2025 yards, so the answer is about 1 % low. The metric version (about 93 m per knot in 3 minutes) is exact enough for any use at sea."
  - "All these figures give distance through the water unless you use speed over ground. Tidal streams and currents can add or take away several knots; see the tides pages."
---

Everything on this page comes from one formula
([Bowditch vol. 2, Table 11](../library/bowditch.html)):

> **distance (NM) = speed (knots) × time (minutes) ÷ 60**

Turn it round as needed:

- **time (minutes) = 60 × distance ÷ speed**
- **speed (knots) = 60 × distance ÷ time (minutes)**

With hours instead of minutes, drop the 60: 6 knots for 3 hours is 18 NM.

## Distance run (nautical miles)

| Speed (kn) | 6 min | 10 min | 15 min | 20 min | 30 min | 60 min |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 0.2 | 0.3 | 0.5 | 0.7 | 1 | 2 |
| 3 | 0.3 | 0.5 | 0.75 | 1 | 1.5 | 3 |
| 4 | 0.4 | 0.7 | 1 | 1.3 | 2 | 4 |
| 5 | 0.5 | 0.8 | 1.25 | 1.7 | 2.5 | 5 |
| 6 | 0.6 | 1 | 1.5 | 2 | 3 | 6 |
| 7 | 0.7 | 1.2 | 1.75 | 2.3 | 3.5 | 7 |
| 8 | 0.8 | 1.3 | 2 | 2.7 | 4 | 8 |
| 10 | 1 | 1.7 | 2.5 | 3.3 | 5 | 10 |
| 12 | 1.2 | 2 | 3 | 4 | 6 | 12 |
| 15 | 1.5 | 2.5 | 3.75 | 5 | 7.5 | 15 |
| 20 | 2 | 3.3 | 5 | 6.7 | 10 | 20 |

## Time to go

| Distance (NM) | 4 kn | 5 kn | 6 kn | 8 kn | 10 kn | 15 kn | 20 kn |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 15 min | 12 min | 10 min | 8 min | 6 min | 4 min | 3 min |
| 2 | 30 min | 24 min | 20 min | 15 min | 12 min | 8 min | 6 min |
| 5 | 1 h 15 | 1 h 00 | 50 min | 38 min | 30 min | 20 min | 15 min |
| 10 | 2 h 30 | 2 h 00 | 1 h 40 | 1 h 15 | 1 h 00 | 40 min | 30 min |
| 20 | 5 h 00 | 4 h 00 | 3 h 20 | 2 h 30 | 2 h 00 | 1 h 20 | 1 h 00 |
| 50 | 12 h 30 | 10 h 00 | 8 h 20 | 6 h 15 | 5 h 00 | 3 h 20 | 2 h 30 |
| 100 | 25 h 00 | 20 h 00 | 16 h 40 | 12 h 30 | 10 h 00 | 6 h 40 | 5 h 00 |

## Quick rules

**6-minute rule.** 6 minutes is one tenth of an hour. In 6 minutes a boat
covers one tenth of its speed in nautical miles: at 7 knots, 0.7 NM. This
follows directly from the formula above.

**3-minute rule.** In 3 minutes, the distance run in hundreds of yards equals
the speed in knots: at 12 knots a ship covers about 1200 yards in 3 minutes
([Quartermaster 3 & 2, ch. 15](../library/navedtra-quartermaster-3-2-1976.html)).
In metres: each knot gives about 93 m in 3 minutes (1852 m ÷ 20). Useful with
radar, when timing a contact over 3 minutes.

**Measured mile.** Time the boat over exactly 1 NM. Speed in knots =
3600 ÷ seconds taken ([Bowditch vol. 2, Table 10](../library/bowditch.html)).
For example 1 NM in 8 min 0 s (480 s) is 7.5 knots. This is speed over the
ground: any current along the mile is included in it.

**Knots and other units.** 1 knot = 1.852 km/h exactly, about 0.51 m/s; see
[Unit conversions](unit-conversions.html).

## Current and tidal stream

The log measures speed through the water. Over the ground, a tidal stream or
current adds to or takes away from it, and pushes the boat sideways if it is
on the beam ([Bowditch vol. 2, section 1101](../library/bowditch.html)). For
an ETA, use speed over ground: 6 knots through the water against 2 knots of
stream is 4 knots over the ground, so 10 NM take 2 h 30, not 1 h 40.

## Worked example

You must cover 18 NM before a tidal gate closes in 3 hours. Needed speed over
the ground = 60 × 18 ÷ 180 = 6 knots. If the stream will be against you at
1 knot, you need 7 knots through the water. If your boat cannot make that,
leave earlier or wait for the next gate. See
[Passage planning](../run-the-boat/passage-planning.html).

## See also

- [Position fixing](../run-the-boat/position-fixing.html) (dead reckoning)
- [Tides and tidal streams](../run-the-boat/tides-and-tidal-streams.html)
- [Rule of twelfths](rule-of-twelfths.html)
- [Unit conversions](unit-conversions.html)
