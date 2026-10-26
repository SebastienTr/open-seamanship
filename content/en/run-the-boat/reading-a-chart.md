---
title: Reading a nautical chart
summary: How to read a paper or electronic chart - scale, title block, depths and chart datum, heights, dangers, light legends, how old the survey is, and how to keep charts corrected.
kind: explainer
section: run-the-boat
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
    locator: "Vol. 1 (2024 edition): chapter 2, section 210 'Datum shift', printed p. 24; chapter 5, sections 524-525 (scales, chart classification), printed pp. 67-68; 527-528 (accuracy, source diagrams and zones of confidence), pp. 68-71; 530-538 (title block, shoreline, symbols, lettering, soundings, depths and datums, heights, dangers, aids to navigation), pp. 72-76; chapter 36, section 3624 'Tidal height predictions', printed p. 614"
  - id: noaa-chart-no-1
    locator: "13th edition (15 April 2019): 'Information on selected chart features' (soundings, heights, drying heights, shoreline, landmarks, light range, aids to navigation positioning), printed p. 6; 'Colors', 'Conversion scales', 'Correction date', printed p. 7; Section Q 'Buoys, beacons', pp. 99-103"
  - id: uscg-boat-crew-handbook-navigation
    locator: "Chapter 3, Section F, F.5 'Paper chart selection' to F.5.f 'Hazards to navigation', pp. 3-111 to 3-114"
uncertain:
  - "Chart No. 1 and Bowditch describe US (NOAA and NGA) charts. Charts from other hydrographic offices use the same international (INT 1) symbols in most cases but can differ in colours, units and datums. Use the symbol key of the country that made the chart."
  - "Electronic chart displays vary with the maker and the user's settings; this page describes paper charts and the official ENC rules only."
---

A nautical chart is a map of the water: depths, dangers, marks, lights and
the shape of the coast seen from the sea. Every symbol is explained in a
symbol key. The US one, **Chart No. 1**, is in the
[library](../library/noaa-chart-no-1.html); most countries use the same
international symbols ([Bowditch, section 532](../library/bowditch.html)).

## Start with the title block

Before using a chart, read its title block. It gives
([Bowditch, section 530](../library/bowditch.html);
[Chart No. 1, p. 6](../library/noaa-chart-no-1.html)):

- **The scale** and projection.
- **The unit of depth** (metres, feet or fathoms), also printed in large
  letters outside the border. Getting this wrong can put you aground: 3 on a
  chart in fathoms is 5.5 m (18 ft).
- **The sounding datum**, the level from which depths are measured, and the
  datum for heights.
- **The horizontal datum** (for example WGS 84). If the chart is on another
  datum, a note gives the shift to apply to satellite positions before you
  plot them. On some charts surveyed long ago, satellite positions cannot be
  converted at all, and a GPS position may be off the true position on the
  chart ([Bowditch, section 210](../library/bowditch.html)).
- **The source notes**: when and how the area was surveyed.

## Scale

Scale is the ratio between a distance on the chart and on the earth: 1:50,000
means 1 cm on the chart is 50,000 cm (500 m) on the earth. A **large-scale**
chart (say 1:25,000) covers a small area in great detail; a **small-scale**
chart (1:1,000,000) covers a big area with little detail. Always use the
largest scale chart you have near dangers: small-scale charts leave detail
out ([Bowditch, sections 524-527](../library/bowditch.html)).

**Measure distance on the latitude scale**, at the side of the chart, level
with where you are: 1 minute of latitude is very nearly 1 nautical mile
(1,852 m). Never use the longitude scale at the top and bottom for distance
([Bowditch, section 524](../library/bowditch.html)).

## Depths and chart datum

The small numbers in the water are **soundings**: depths below **chart
datum**, a low-water level chosen so that the water seldom falls below it.
Chart datum differs by country: it may be mean lower low water (most US
charts), lowest astronomical tide, mean low water springs, or a mean level in
seas with little tide ([Bowditch, section 535](../library/bowditch.html)).

- **Depth now = charted depth + height of tide now.** A negative tide height
  in the tables means less water than charted. See
  [Tides and tidal streams](tides-and-tidal-streams.html) ([Bowditch, section 3624](../library/bowditch.html)).
- **Drying heights** are underlined figures: the height above chart datum of
  rocks and banks that cover and uncover ([Chart No. 1, p. 6](../library/noaa-chart-no-1.html)).
- **Depth contours** join points of equal depth. A broken contour is
  uncertain. Shallow areas are often tinted blue
  ([Bowditch, section 534](../library/bowditch.html)).
- The chart shows the **least depths** found; between soundings there may be
  shallower spots that were never found. Keep clear of known shoal areas and
  watch your echo sounder ([Bowditch, section 534](../library/bowditch.html)).

## Heights and clearances

Heights are measured from a different level than depths. Bowditch says a
light's height is usually given above mean sea level; Chart No. 1 says US
charts give heights of lights and landmarks above the shoreline (high-water)
level. The title block of your chart says which
([Bowditch, section 536](../library/bowditch.html);
[Chart No. 1, p. 6](../library/noaa-chart-no-1.html)).
Clearances under bridges and power lines are usually given above mean high
water, which leaves you a margin at most tides, but not at a high spring tide
or in a storm surge ([Bowditch, section 536](../library/bowditch.html)). The
coastline drawn on the chart is usually the high-water line
([Bowditch, section 531](../library/bowditch.html)).

## Lettering, colours and dangers

- **Upright lettering** is used for things that are dry at high water;
  **sloping lettering** for things under water or floating. A "rock" named in
  sloping letters is covered at high water ([Bowditch, section 533](../library/bowditch.html)).
- On NOAA charts land is buff (grey on NGA charts), the area that dries is
  green, shallow water blue, deep water white. Magenta (purple) marks
  important navigation information: lights, compass roses, regulated areas
  ([Chart No. 1, p. 7](../library/noaa-chart-no-1.html)).
- Rocks, wrecks and obstructions have their own symbols. A wreck with a dotted
  line round it is considered dangerous (less than 30 m over it on US charts)
  ([Bowditch, section 537](../library/bowditch.html)).
- Tide rips, eddies, kelp and fish traps are shown by symbol or words.

## Lights and marks

A light on the chart has a magenta flare and a **legend**, written in this
order: number, character, colour, period, height, range. For example
`"6" Fl(2) R 10s 80m 19M` is light number 6, group flashing 2, red, every
10 seconds, 80 m above the height datum, seen 19 nautical miles. On smaller
scales part of the legend is left out ([Bowditch, section 538](../library/bowditch.html)).
On NOAA charts a light with several colours shows only the shortest range
([Chart No. 1, p. 6](../library/noaa-chart-no-1.html)).

A buoy symbol has a small circle at its foot: the approximate position of its
sinker. The buoy itself can be some distance away on its chain
([Bowditch, section 538](../library/bowditch.html)). The meaning of each mark
is on [Buoys and beacons](iala-buoyage.html).

## How far to trust the chart

A chart is a patchwork of surveys, some very old. Look at the source note or
source diagram. Few, scattered soundings or large blank areas mean the area
was not surveyed in detail: go slowly with the echo sounder running.
Entrances with strong currents or surf, and dredged channels, change quickly
([Bowditch, sections 527-528](../library/bowditch.html)). Electronic charts
may show **zones of confidence** (ZOC) from A1 (best) to D (poor) and U
(unassessed) ([Bowditch, section 528](../library/bowditch.html)).

## Keep it up to date

Check the edition date in the lower left corner and the date of the last
correction ([Chart No. 1, p. 7](../library/noaa-chart-no-1.html)). Apply the
corrections published in Notices to Mariners, in pen, and write down each one
on the chart or on a correction card. Even a corrected chart can be wrong:
hazards move and some surveys are old. Mark your own boat's draught contour
and the dangers along your route before you go
([Boat Crew Handbook - Navigation, pp. 3-111 to 3-114](../library/uscg-boat-crew-handbook-navigation.html)).

## See also

- [Buoys and beacons (IALA A and B)](iala-buoyage.html)
- [Compass, variation and deviation](compass-variation-and-deviation.html) (the compass rose)
- [Fixing your position without GPS](position-fixing.html)
- [Tides and tidal streams](tides-and-tidal-streams.html)
- [Planning a passage](passage-planning.html)
- [Unit conversions](../tables/unit-conversions.html)
