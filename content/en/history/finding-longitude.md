---
title: Finding longitude
summary: Why east-west position was so hard to find at sea, and how the lunar distance method and the marine chronometer solved it between 1714 and the mid-1800s.
kind: history
section: history
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
    locator: "Vol. I (2024 printing), chapter 1, section 103 'Important Conventions and Concepts' (prime meridians, Greenwich 1884), pp. 5-6; section 108 'Finding Latitude and Longitude' (Board of Longitude, Harrison, time balls, radio time signals), p. 9; section 109 'The Navigational Triangle' (lunar distances, Bowditch's 1802 method, chronometer cost), pp. 9-10; section 110 'The Time Sight', p. 10; Preface, 'Nathaniel Bowditch (1773-1838)', pp. iii-iv"
  - id: lecky-wrinkles-1901
    locator: "chapter IV 'The Marine Chronometer' (lunars went out when chronometers came in; time signals by gun, ball or cone), pp. 44-45; 'The Moon as a Chronometer, or the Rationale of Lunars' (Harrison's timekeeper; accuracy of lunars, 20 miles in the tropics), pp. 456-459"
  - id: wikipedia-en
    locator: "'Longitude rewards' (sections 'Background', 'Establishing the prizes', 'List of awardees by amount'); 'John Harrison' (sections 'First three marine timekeepers', 'H4'); 'History of longitude' (sections 'Government initiatives', 'Lunar distances versus chronometers', 'Land surveying and telegraphy', 'Wireless methods'); 'Marine chronometer' (sections 'First examples', 'Further development'); 'Scilly naval disaster of 1707' (lead)"
uncertain:
  - "Sources give slightly different figures for Harrison's trials. Bowditch (p. 9) says his best timekeeper lost 15 seconds on a 156-day round trip to Barbados; English Wikipedia ('John Harrison', section H4) says H4 was 5 seconds slow after the 81-day voyage to Jamaica in 1761-62 and within 39 seconds on the 1764 Barbados trial. This page uses the Wikipedia figures and names the voyage for each."
  - "Bowditch (p. 9) dates the first radio time signals for ships to 1904; English Wikipedia ('History of longitude', section 'Wireless methods') gives 1907, from Halifax, Nova Scotia. Both are given."
  - "Harrison's total reward is given as £23,065 (Wikipedia) while Bowditch says he finally received 'his full reward of £20,000'. The totals count different payments; this page uses the itemised Wikipedia figure."
---

At sea, latitude was never the real problem. Measure the height of the Sun
at noon, look up its declination for the day, and you have your latitude to
within a degree or two. Navigators of the 1400s already did this, and anyone
who takes a noon sight or a sight of the Pole Star today uses the same idea
([Bowditch, section 108](../library/bowditch.html)).

Longitude, your position east or west, was different. For about three
centuries ships crossed oceans without a reliable way to find it.

## Why longitude is a clock problem

The Earth turns 360 degrees in 24 hours, so 1 degree of longitude equals 4
minutes of time ([Wikipedia: History of longitude](../library/wikipedia-en.html)).
If you know your local time (from the Sun) and, at the same moment, the time
at a reference place such as Greenwich, the difference is your longitude. A
clock error of 1 minute means 15 minutes of arc: about 15 nautical miles (28 km)
at the equator.

So the question was: how do you carry the time of the home port across an
ocean? Pendulum clocks failed on a rolling ship. Spring clocks drifted with
heat and cold. Until the 1700s, ships relied on
[dead reckoning](../run-the-boat/position-fixing.html): course, speed and
time, with errors that grew every day.

## Wrecks, prizes and a Board

Several governments offered rewards: Philip II of Spain in 1567, Philip III
in 1598, and the Dutch States General soon after. None was won
([Wikipedia: Longitude rewards](../library/wikipedia-en.html)).

On 22 October 1707 four British warships struck rocks off the Isles of Scilly
and between 1,400 and 2,000 sailors died. The causes included poor position
finding, wrong charts and poor compasses
([Wikipedia: Scilly naval disaster of 1707](../library/wikipedia-en.html)).
In 1714 the British Parliament passed the Longitude Act. It offered £10,000
for a method accurate to 1 degree, £15,000 for 40 minutes and £20,000 for
30 minutes, tested on a voyage to the West Indies. A Board of Longitude
judged the entries ([Wikipedia: Longitude rewards](../library/wikipedia-en.html);
[Bowditch, section 108](../library/bowditch.html)).

## Two answers: the Moon and the clock

Two methods worked in the end.

**Lunar distances.** The Moon moves against the stars by about half a degree
an hour. With tables that predict where it will be at each Greenwich hour,
the Moon becomes a clock in the sky. The navigator measures the angle between
the Moon and a star or the Sun with a sextant, "clears" it of refraction and
parallax, and reads Greenwich time from the almanac
([Bowditch, section 109](../library/bowditch.html)). Tobias Mayer's lunar
tables reached the Board in 1755. Nevil Maskelyne, Astronomer Royal, turned
them into the *Nautical Almanac*, first published for the year 1767
([Wikipedia: History of longitude](../library/wikipedia-en.html)). The
working took hours. In 1802 Nathaniel Bowditch, a Salem mariner, published a
simpler method in *The New American Practical Navigator*; it is said that
every man in his crew, the cook included, could work a lunar
([Bowditch, Preface](../library/bowditch.html)).

**The chronometer.** John Harrison (1693-1776), a joiner and clockmaker from
Yorkshire, spent more than 30 years on sea clocks. H1 sailed to Lisbon and
back in 1736. H2 and H3 followed. Then he changed approach and built H4, a
large watch about 12 cm (5 in) across. On the official trial to Jamaica
(1761-62) in HMS *Deptford*, H4 was 5 seconds slow after 81 days, an error of
about 1 nautical mile. On a second trial to Barbados in 1764 it kept time to
within 39 seconds ([Wikipedia: John Harrison](../library/wikipedia-en.html)).
The Board doubted the result and asked for more. Harrison received payments
over many years, £23,065 in all, the last after Parliament stepped in in 1773
([Wikipedia: Longitude rewards](../library/wikipedia-en.html)).

France worked on the same problem. Pierre Le Roy and Ferdinand Berthoud built
marine timekeepers, and French sea trials between 1767 and 1772 tested both
clocks and lunar distances
([Wikipedia: History of longitude](../library/wikipedia-en.html)). Le Roy's
detent escapement and compensated balance (1766) are seen as the basis of the
later chronometer ([Wikipedia: Marine chronometer](../library/wikipedia-en.html)).

## From rare instrument to standard kit

| Year | Step |
| --- | --- |
| 1767 | First *Nautical Almanac* with lunar distance tables |
| 1780 | Earnshaw and Arnold simplify the chronometer for production |
| 1825 | Royal Navy routinely supplies chronometers to its ships |
| 1850 | Most ocean navigators have given up lunars |
| 1884 | Greenwich adopted as the prime meridian |
| 1907 | Lunar tables dropped from the British *Nautical Almanac* |

Sources: [Wikipedia: Marine chronometer and History of longitude](../library/wikipedia-en.html);
[Bowditch, section 103](../library/bowditch.html).

Early chronometers were very costly. Reliable ones existed by 1800, but most
ships still used lunars ([Bowditch, section 109](../library/bowditch.html)).
Prices fell through the 1800s. By 1901 Captain S. T. S. Lecky could write that
"when chronometers came in, lunars went out", that a good chronometer cost
£26 to £30, and that better ships on long voyages carried three. He judged
that even a careful observer could not expect a lunar to place a ship closer
than about 20 miles in the tropics
([Lecky, pp. 44 and 456-459](../library/lecky-wrinkles-1901.html)).
Ships carried more than one chronometer because two that disagree cannot tell
you which is wrong; three can
([Wikipedia: History of longitude](../library/wikipedia-en.html)).

## Checking the clock

A chronometer is only useful if you know its error. Ports set up time balls,
dropped at a fixed moment each day, and some used guns or a collapsing cone
([Bowditch, section 108](../library/bowditch.html);
[Lecky, ch. IV](../library/lecky-wrinkles-1901.html)). Telegraph cables then
carried time between observatories; a cable from Brest to Duxbury,
Massachusetts, opened in 1870 and was used to check transatlantic longitudes.
Radio time signals for ships followed in the early 1900s
([Wikipedia: History of longitude](../library/wikipedia-en.html)).

## What it means for you

Today satellite receivers give longitude and time together. But the old idea
still works: an accurate watch, a sextant and an almanac will give a position
if the electronics fail. See [Fixing your position without GPS](../run-the-boat/position-fixing.html)
and [A short history of navigation](history-of-navigation.html).
