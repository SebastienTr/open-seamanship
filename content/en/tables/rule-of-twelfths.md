---
title: Rule of twelfths
summary: A quick way to estimate the height of tide between high and low water, with a worked example and where it fails.
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
  - id: wikipedia-en
    locator: "Rule of twelfths, sections 'The rule' (table of rule against sine values), 'Example calculations: Tides' and 'Caveats'"
  - id: bowditch
    locator: "Vol. 1 (2024 ed.), ch. 36 'Tides and tidal currents', sections 3604-3607 (rate of rise not uniform; sine-like curve; semidiurnal, diurnal and mixed tides; double high and low waters), pp. 604-606 (PDF pp. 616-618); ch. 5, section 537 'Dangers' (drying heights underlined); Vol. 2 (2024 ed.), ch. 11 'Tide and current predictions', sections 1101-1102 (depth = charted depth + height of tide; low water about 6 h 12 min from high water) and 1106 (Table 3 assumes a sine curve), pp. 308-310 (PDF pp. 322-324)"
uncertain:
  - "The rule is a rough estimate. Real tide curves are not exact sine curves, and where the tide is irregular the error can be much larger than the figures below. Use official tide predictions and the tidal curve for the port when you have them."
  - "Weather changes sea level: high pressure or a persistent offshore wind can make the tide lower than predicted, low pressure or an onshore gale higher (Bowditch vol. 2, section 1101). Keep a safety margin under the keel."
---

Between low water and high water the tide does not rise at a steady rate. It
starts slowly, runs fastest around half tide, and slows again near high water.
The fall is the same in reverse
([Bowditch vol. 1, section 3604](../library/bowditch.html)). The rule of
twelfths turns this into simple sums.

## The rule

Divide the time from low water to high water into 6 equal parts ("tide
hours"). Divide the range (high water height minus low water height) by 12.
Then, in each tide hour, the tide rises by:

| Tide hour | Rise in that hour | Total since low water | Total as % of range |
| --- | --- | --- | --- |
| 1st | 1/12 | 1/12 | 8 % |
| 2nd | 2/12 | 3/12 | 25 % |
| 3rd | 3/12 | 6/12 | 50 % |
| 4th | 3/12 | 9/12 | 75 % |
| 5th | 2/12 | 11/12 | 92 % |
| 6th | 1/12 | 12/12 | 100 % |

Easy to remember: **1, 2, 3, 3, 2, 1**. On a falling tide, count down from high
water in the same way ([Rule of twelfths, wikipedia-en](../library/wikipedia-en.html)).

Half the range comes and goes in the middle two hours. In many places,
though not all, the tidal stream also runs hardest around half tide
([Bowditch vol. 2, section 1101](../library/bowditch.html)).

## Worked example

Low water 1.0 m at 0600. High water 5.8 m at 1200. What is the height of tide at
0900, and at 1000?

1. Range = 5.8 − 1.0 = 4.8 m. One twelfth = 0.4 m.
2. Duration = 6 hours, so each tide hour is 1 hour.
3. By 0900 (3 tide hours): 1 + 2 + 3 = 6 twelfths = 2.4 m above low water.
   Height of tide = 1.0 + 2.4 = **3.4 m**.
4. By 1000 (4 tide hours): 9 twelfths = 3.6 m. Height = **4.6 m**.

| Time | 0600 | 0700 | 0800 | 0900 | 1000 | 1100 | 1200 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Height (m) | 1.0 | 1.4 | 2.2 | 3.4 | 4.6 | 5.4 | 5.8 |

Depth of water = charted depth + height of tide
([Bowditch vol. 2, section 1101](../library/bowditch.html)). A rock charted at
0.5 m has 3.4 + 0.5 = 3.9 m over it at 0900. A drying height (underlined on
the chart: the rock stands that far above chart datum) is subtracted instead: a
rock drying 1.2 m has 3.4 − 1.2 = 2.2 m over it
([Bowditch vol. 1, section 537](../library/bowditch.html)).

If the time from low to high water is not 6 hours, divide it into 6 equal
parts anyway. With 6 h 30 min, each tide hour is 65 minutes. Low and high water
are usually a little over 6 hours apart, about 6 h 12 min on average
([Bowditch vol. 2, section 1102](../library/bowditch.html)).

## How good is it?

The rule copies a sine curve, which is how tide tables model the tide between
high and low water ([Bowditch vol. 2, section 1106](../library/bowditch.html)).
Against a true sine curve:

| After tide hour | Rule (fraction of range) | Sine curve |
| --- | --- | --- |
| 1 | 0.083 | 0.067 |
| 2 | 0.25 | 0.25 |
| 3 | 0.50 | 0.50 |
| 4 | 0.75 | 0.75 |
| 5 | 0.917 | 0.933 |

The difference is under 2 % of the range: 8 cm on a 5 m range. Real tides
differ from a sine curve more than that.

## Where it fails

- **Double high or low waters.** Some ports have a long stand or a second high
  or low water, for example Southampton (double high water) and Hoek van Holland
  (double low water) ([Bowditch vol. 1, section 3607](../library/bowditch.html)).
  Poole Harbour, the Solent and Weymouth Bay are also cited
  ([Rule of twelfths, wikipedia-en](../library/wikipedia-en.html)).
- **Diurnal and mixed tides.** Where there is one tide a day, or two very
  unequal tides, the 6-hour pattern does not hold (Bowditch section 3605).
- **Very small ranges.** Where the range is small, weather can change the water
  level more than the tide does.
- **Rivers and shallow estuaries.** The tide wave steepens in shallow water;
  the rise can be much quicker than the fall, and in a few places it arrives as
  a bore (Bowditch section 3607).

In all these places use the port's own tidal curve or predictions. See
[Tides and tidal streams](../run-the-boat/tides-and-tidal-streams.html).

The pack's home dashboard has a tide calculator that uses this rule.

## See also

- [Tides and tidal streams](../run-the-boat/tides-and-tidal-streams.html)
- [Time, speed and distance](time-speed-distance.html)
- [Brittany: the coast, tides and races](../regions/brittany-coast.html)
