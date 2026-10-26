---
title: Fixing your position without GPS
summary: Dead reckoning, compass bearings, three-point fixes, transits, running fixes, the four-point bearing, depth soundings and danger bearings - how to know where you are when the electronics fail.
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
    locator: "Vol. 1 (2024 edition): chapter 11 'Piloting', section 1102 (danger bearings, warning and danger soundings), printed pp. 199-200; 1111 'Types of fixes', pp. 205-206; 1112 'The running fix', pp. 206-209; 1113 'Fix type and fix interval', p. 210; 1115 'Using the fathometer', p. 211; 1121 (distance off by two bearings), p. 215; 1122 'Common errors', p. 216; chapter 29 'Emergency navigation', sections 2902 'Most probable position' and 2904 'Dead reckoning', printed pp. 485-487, 2911 'Finding latitude', pp. 492-493"
  - id: navedtra-quartermaster-3-2-1976
    locator: "Chapter 10 'Dead reckoning and piloting': 'Fixes', 'Selecting landmarks', 'Horizontal sextant angles', 'Running fix', pp. 142-148"
  - id: lecky-wrinkles-1901
    locator: "13th edition (Internet Archive scan wrinklesinpracti00leck_1), 'The four-point bearing' and 'Doubling the angle on the bow', pp. 683-685"
  - id: uscg-boat-crew-handbook-navigation
    locator: "Chapter 3, Section F, F.10 'Danger bearing / range', p. 3-119"
uncertain:
  - "Lecky's book dates from about 1901 and describes ships of that time. The geometry of the four-point bearing has not changed, but its examples (patent log, steam speeds) are historic."
  - "Bowditch counts two lines of position as a fix only by one definition; it recommends at least three. A position from bearings of floating buoys is only an estimated position."
---

GPS can fail, be jammed, or lose power. Then you go back to the methods
navigators used for centuries: keep track of where you have been, and check
it against what you can see and measure. Bowditch lists the usual causes of
groundings: misidentified marks, no dead reckoning, ignoring soundings,
forgetting variation or deviation, and not slowing down when unsure of the
position ([Bowditch, section 1122](../library/bowditch.html)).

## Dead reckoning: always available

**Dead reckoning (DR)** is working out your position from your last known
position, your course steered and the distance run (speed × time). It is the
one method that never fails completely
([Bowditch, section 2904](../library/bowditch.html)).

- Write in the log, every hour and at every change: time, course, log
  reading or speed, and the last fix.
- Plot the DR on the chart; label it with the time.
- Correct it for **leeway** (wind pushing you sideways) and **tidal stream or
  current** to get an **estimated position (EP)**
  ([Quartermaster 3 & 2, figure 10-10, p. 144](../library/navedtra-quartermaster-3-2-1976.html)).
- Keep the DR going from fix to fix. When information conflicts, the DR is
  often the best guide to your most probable position
  ([Bowditch, section 2902](../library/bowditch.html)).

Write down the GPS position every hour while it works. If it then fails, you
start from a known point. Speed, time and distance tables are in
[Time, speed and distance](../tables/time-speed-distance.html).

## A fix from compass bearings

A **line of position** (LOP) is a line you know you are on. Two or more lines
crossing give a **fix** ([Bowditch, section 1111](../library/bowditch.html)).

1. Choose **three** charted objects you can identify for sure: a lighthouse,
   a church spire, the edge of a headland, a beacon. Fixed objects ashore are
   best; a buoy can be off station
   ([Bowditch, section 1111](../library/bowditch.html)).
2. Choose them well spread: with two objects, about 90° apart; with three,
   about 120° apart. Lines crossing at a narrow angle give a poor fix
   ([Quartermaster 3 & 2, p. 145](../library/navedtra-quartermaster-3-2-1976.html)).
3. Take the bearings with a hand-bearing compass, quickly, one after the
   other, so that they are as nearly simultaneous as possible
   ([Quartermaster 3 & 2, p. 145](../library/navedtra-quartermaster-3-2-1976.html)).
4. Convert each compass bearing to true (or use the magnetic rose), see
   [Compass, variation and deviation](compass-variation-and-deviation.html).
5. Draw each line on the chart **from the object towards you** and note the
   time.

Three lines rarely meet in a point; they make a small triangle (a "cocked
hat"). If it is small, take its centre as your position. If it is large,
re-take the bearings: something is wrong, and the boat may even be outside
the triangle, so keep well clear of dangers. If all
your triangles come out the same size, suspect a compass error
([Quartermaster 3 & 2, p. 145](../library/navedtra-quartermaster-3-2-1976.html);
[Bowditch, section 1124](../library/bowditch.html)).

**Transits (ranges)** are the best lines of all: when two charted objects are
in line, you are on that line, with no compass error
([Bowditch, section 1111](../library/bowditch.html)). A transit crossed with a
bearing gives a good fix.

## Distances

A distance off an object gives a circle of position. Ways to get one:
radar range (more accurate than a radar bearing), or a vertical sextant angle
between the top of a light of known height and the waterline below it, with
the table in Bowditch volume II ([Bowditch, section 1111](../library/bowditch.html)). In fog, a radar range
from each of two charted points gives a fix.

## The running fix: one object only

When only one object is in sight:

1. Take a bearing and note the time and log reading.
2. Keep a steady course and speed. When the bearing has changed by a good
   amount, so that the two lines will cross clearly, take a second bearing.
3. Move the first line of position along your course by the distance run
   between the two bearings, keeping it parallel.
4. Where the moved line crosses the second bearing is your **running fix**.

Its accuracy depends on how well you know your course and speed over the
ground in between; tidal stream must be allowed for
([Bowditch, section 1112](../library/bowditch.html);
[Quartermaster 3 & 2, pp. 146-148](../library/navedtra-quartermaster-3-2-1976.html)).

### The four-point bearing and doubling the angle

A quick mental version, used since the days of sail
([Lecky, pp. 683-685](../library/lecky-wrinkles-1901.html)):

- Note the time or log when the object is **45° (four points) on the bow**.
  Note it again when it is **abeam (90°)**. The distance run in between
  equals your distance off when abeam.
- More generally, when the angle on the bow **doubles** (for example from 30°
  to 60°), the distance run equals the distance off at the second bearing.
  This warns you earlier than waiting until abeam.

Both assume no tidal stream across your track. Bowditch gives a table
(Table 18) for any pair of angles ([Bowditch, section 1121](../library/bowditch.html)).

## Depth as a check

Compare the echo sounder with the charted depth at every fix. A line of
soundings taken at known intervals along your track and matched to the
chart can help when nothing else is visible
([Bowditch, sections 1115 and 2902](../library/bowditch.html)). Remember to
allow for the height of tide ([Tides and tidal streams](tides-and-tidal-streams.html)).
Decide in advance a **warning sounding**: if you get less, slow down, fix
more often and find out where you are; and a **danger sounding**: if you get
less, turn at once towards deep water and consider anchoring
([Bowditch, section 1115](../library/bowditch.html)).

## Staying clear without a fix: danger bearings

Before you pass a danger, draw on the chart a line from a conspicuous object
that just clears it, hatch the dangerous side, and write the limit, for
example "NMT 074°" (no more than) or "NLT" (no less than). As long as the
object's bearing stays on the safe side of that figure, you are clear,
whatever your exact position
([Bowditch, section 1102](../library/bowditch.html);
[Boat Crew Handbook - Navigation, p. 3-119](../library/uscg-boat-crew-handbook-navigation.html)).

## Offshore: latitude from the sky

Far from land, latitude can be found without accurate time from the Sun's
greatest altitude at noon or from the Pole Star, using a sextant and an
almanac. Bowditch's chapter on emergency navigation explains how to do it
with the least equipment ([Bowditch, sections 2911-2912](../library/bowditch.html)).
For the history, see [Finding longitude](../history/finding-longitude.html).

## How often to fix

In confined water, fix often: Bowditch's standard for ships is every three
minutes ([Bowditch, section 1113](../library/bowditch.html)). On a small boat,
fix more often the closer you are to danger. If you are not sure where you
are near danger, **slow down or stand off** until you are
([Bowditch, sections 1113 and 1122](../library/bowditch.html)).

## See also

- [Compass, variation and deviation](compass-variation-and-deviation.html)
- [Reading a nautical chart](reading-a-chart.html)
- [Tides and tidal streams](tides-and-tidal-streams.html)
- [Planning a passage](passage-planning.html)
- [A short history of navigation](../history/history-of-navigation.html)
