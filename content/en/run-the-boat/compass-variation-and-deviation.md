---
title: Compass, variation and deviation
summary: Why the magnetic compass does not point to true north, how to find variation on the chart and deviation for your boat, how to convert between true, magnetic and compass courses, and how to check your compass on a transit.
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
    locator: "Vol. 1 (2024 edition), chapter 9 'Compasses': sections 906-907 (terrestrial magnetism, World Magnetic Model), printed pp. 154-155; 908-911 (compass error, deviation table, applying variation and deviation), pp. 156-160; 925 (reasons for correcting the compass), p. 176; 944-946 (heading, variation and deviation, heading relationships), p. 189; chapter 11, section 1124 'Finding compass error by trial and error', p. 218"
  - id: uscg-boat-crew-handbook-navigation
    locator: "Chapter 3, Section D, D.7 'Variation' to D.12 'Course', including D.7.b (annual change), D.8 'Deviation', D.9 'Magnetic compass deviation check' (Figure 3-49, deviation check using ranges), D.11 'Magnetic compass adjustment', pp. 3-66 to 3-74"
  - id: navedtra-quartermaster-3-2-1976
    locator: "Chapter 4 'Magnetic compass and gyrocompass', 'Precautions in vicinity of magnetic compass', p. 47"
  - id: uscg-boat-crew-handbook-seamanship
    locator: "Chapter 5, Section A, A.8 'Safety' (lightning), step 5, p. 5-7"
uncertain:
  - "Bowditch (2024) says the World Magnetic Model then in use expired at the end of 2024; a newer model is now in force. Always take variation from the most recent chart or an official model, and apply the annual change printed on the compass rose."
  - "The 5 degree limit before calling a professional adjuster comes from US Coast Guard boat practice. It is a sensible guide for small craft, not a legal rule."
  - "The numbers in the worked examples are invented for practice. Never use them as the variation for a real place."
---

A magnetic compass points to **magnetic north**, not to true north, and the
boat itself pulls it further off. Two errors must be allowed for every time
you turn a chart course into a course to steer, or a compass bearing into a
line on the chart:

- **Variation**: the angle between true north and magnetic north **where you
  are**. It depends on place and slowly changes over the years. It is the same
  on every heading ([Bowditch, sections 906 and 945](../library/bowditch.html)).
- **Deviation**: the angle between magnetic north and where **your** compass
  points, caused by iron, steel, engines, electrics and electronics on board.
  It changes with the **boat's heading**, not with place
  ([Bowditch, section 908](../library/bowditch.html);
  [Boat Crew Handbook - Navigation, D.8](../library/uscg-boat-crew-handbook-navigation.html)).

Their sum is the **compass error**. Each is named **east** (E) or **west** (W)
by which side of the reference north the compass points.

## Finding variation

Look at the **compass rose** on the chart nearest to you. The inner ring is
graduated to magnetic north, and the middle of the rose gives the variation,
the year it applied, and the **annual change**
([Bowditch, section 945](../library/bowditch.html)). Bring it up to date:

1. Note the variation and the year printed on the rose.
2. Subtract that year from the present year.
3. Multiply by the annual change.
4. Add or subtract the result as the rose says (increasing or decreasing).

([Boat Crew Handbook - Navigation, D.7.b](../library/uscg-boat-crew-handbook-navigation.html).)
Variation can differ between two roses on the same chart. Use the nearest one.
Charts also carry notes warning of **local magnetic disturbance**, small
areas where the earth's field is irregular and the compass cannot be trusted.
Other ships, piers, machinery and electric currents close by can disturb it
too ([Bowditch, section 906](../library/bowditch.html)). A severe magnetic storm
can shift variation by 5° or more for a time (same section).

## Finding deviation

Deviation belongs to your boat and your compass. It is recorded in a
**deviation table** or card kept beside the compass, giving the deviation for
each heading. Enter the table with the boat's **heading**, never with a
bearing of an object ([Bowditch, section 909](../library/bowditch.html)).
A hand-bearing compass used away from the boat's steel and electrics usually
has little deviation, which is one reason it is useful for bearings.

**Check deviation on a transit (range).** A transit is two charted objects
that you see in line, such as leading lights, or a church spire and a water
tower ([Boat Crew Handbook - Navigation, D.9](../library/uscg-boat-crew-handbook-navigation.html)).

1. Pick a transit on the chart well away from wrecks, steel piers, bridges or
   pipelines.
2. Measure its bearing on the chart and convert it to **magnetic**.
3. Steer along the transit, objects in line, and read the steering compass.
4. Deviation on that heading = magnetic bearing minus compass reading.
   **Compass less than magnetic: deviation east. Compass more than magnetic:
   deviation west.** Example from the US Coast Guard handbook: transit 272°
   magnetic, compass reads 274°, so deviation is 2° W
   (Figure 3-49).
5. Repeat on several headings, for example every 45°, and make a table.

Make a new table every year and whenever equipment near the compass changes.
If deviation on any heading is more than 5°, have the compass adjusted by a
professional ([Boat Crew Handbook - Navigation, D.9 and D.11](../library/uscg-boat-crew-handbook-navigation.html)).
A well-adjusted compass is steadier and easier to steer by
([Bowditch, section 925](../library/bowditch.html)).

## Converting courses and bearings

The order is always **True - Variation - Magnetic - Deviation - Compass**
([Bowditch, section 946](../library/bowditch.html)).

| Going | Easterly error | Westerly error | Memory aid |
| --- | --- | --- | --- |
| Compass to true ("correcting") | Add | Subtract | **C**an **D**ead **M**en **V**ote **T**wice **A**t **E**lections: Compass, Deviation, Magnetic, Variation, True, Add East |
| True to compass ("uncorrecting") | Subtract | Add | **T**elevision **M**akes **D**ull **C**hildren **A**ll **W**eekend: add West |

Another check: **"compass least, error east; compass best, error west"**
([Bowditch, section 946](../library/bowditch.html)).

**Worked example (invented numbers).** The chart course is 221° true.
Variation 9° E; deviation on this heading 2° W.

- True 221°, subtract easterly variation 9°: **magnetic 212°**.
- Magnetic 212°, add westerly deviation 2°: **compass 214°**. Steer 214°.

Going back: compass 214°, subtract westerly deviation: magnetic 212°; add
easterly variation: true 221°. The same rules apply to a bearing, except that
the deviation is the one for the **heading you were on** when you took it
([Bowditch, section 909](../library/bowditch.html)).

## Keeping the compass honest

- Keep iron and magnets away from the compass: tools, knives, keys, torches,
  cans, mobile phones, portable radios, loudspeakers, wires carrying direct
  current, electric motors
  ([Quartermaster 3 & 2, p. 47](../library/navedtra-quartermaster-3-2-1976.html);
  [Boat Crew Handbook - Navigation, D.8](../library/uscg-boat-crew-handbook-navigation.html)).
- If several fixes from three bearings all make triangles of the same size,
  the compass may have a constant error. Try applying a few degrees to all
  bearings; if the triangles shrink to a point, you have found it. Then look
  for the cause ([Bowditch, section 1124](../library/bowditch.html)).
- An electronic heading sensor (fluxgate) does its own correction when
  calibrated, but metal near it still upsets it
  ([Boat Crew Handbook - Navigation, D.10](../library/uscg-boat-crew-handbook-navigation.html)).
- After a lightning strike, expect the compass to be wrong until checked
  ([Boat Crew Handbook - Seamanship, p. 5-7](../library/uscg-boat-crew-handbook-seamanship.html));
  see [Reading the weather at sea](reading-the-weather.html).

## See also

- [Reading a nautical chart](reading-a-chart.html)
- [Fixing your position without GPS](position-fixing.html)
- [Planning a passage](passage-planning.html)
- [A short history of navigation](../history/history-of-navigation.html)
