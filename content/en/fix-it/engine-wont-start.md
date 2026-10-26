---
title: Engine turns over but won't start
summary: The diesel cranks at normal speed but does not fire, or fires and dies. Check fuel, air in the fuel, cold start aids and the stop control, cheapest first.
kind: guide
section: fix-it
region: international
language: en
licence: CC-BY-SA-4.0
safety: normal
status: draft
authors: [claude]
reviewers: []
reviewed: null
sources:
  - id: tm-9-2815-252-24-dn2m
    locator: "Table 3-2 'Troubleshooting', malfunctions 3 and 4 (engine hard to start or will not start; in cold weather), pp. 3-3 to 3-4"
  - id: tm-9-2815-254-24-isuzu-c240
    locator: "Table 3-2 'Troubleshooting', malfunction 3 (engine cranks but fails to start) and 4 (cold weather), pp. 3-4 to 3-5"
  - id: navedtra-engineman-3-2-1979
    locator: "Ch. 13 'Troubleshooting': 'Engine cranks but fails to start', 'Foreign matter in the fuel oil system', 'Insufficient fuel supply', pp. 266-267; 'Clogged fuel filters', p. 267; 'Timing' and 'Insufficient compression', pp. 268-269; 'Insufficient cranking speed', p. 270"
  - id: navpers-engineman-2-1957
    locator: "Ch. 6 'Fuel injection equipment', 'Bleeding air out of fuel system', pp. 241-243"
  - id: navpers-engineman-1957
    locator: "Engineman 3 (NAVPERS 10539), ch. 13 'Engine operating procedures, general': 'Starting in cold weather', glow plugs and ether starting fluid, pp. 453-457"
  - id: navedtra-construction-mechanic-3-2-1978
    locator: "Ch. 4 'Fuel systems', 'Water in fuel system' and 'Air in fuel system', pp. 119-120"
  - id: wikipedia-en
    locator: "'Glow plug', sections 'Design' and 'Activation method'; 'Hydrolock', section 'Causes and special cases: Marine'"
uncertain:
  - "Pre-heat times for glow plugs differ by engine. Wikipedia mentions about 20 seconds for older manual systems; this is not a figure for your engine. Use your engine's manual."
  - "Closing the raw-water seacock during long cranking is common small-boat practice; the sources explain the risk of water filling the exhaust but do not give this step. A reviewer should confirm it."
  - "Many engine manuals forbid starting fluid on engines with glow plugs or an intake heater, because the hot element can ignite it early. No cleared source states this; follow your manual."
  - "The order of checks follows the two Army troubleshooting tables for small generator diesels and the Navy manuals. Small marine diesels are close relatives, but fuel systems differ by make."
---

## Situation

The starter turns the engine at its normal speed but it does not fire, or it
fires a few times and stops. If the engine does not turn, or turns very
slowly, go to [Engine won't turn over](engine-wont-crank.html) first.

A diesel needs three things: enough compression to heat the air, clean fuel
arriving at the injectors, and the fuel injected at the right moment
([Engineman 3 & 2, p. 261](../library/navedtra-engineman-3-2-1979.html)).
Most of the causes are in the fuel and the fuel system
([Engineman 3 & 2, p. 266](../library/navedtra-engineman-3-2-1979.html)).

## Do now

Work down the list. Crank in short bursts and let the starter cool between
tries: cranking longer than the time in your engine's manual only drains the
battery ([Engineman 2, p. 242](../library/navpers-engineman-2-1957.html)).

1. **Stop control.** Is the stop lever or pull-knob fully back in the run
   position? Some stop cables stick half-way. This is step 1 in the Army table
   ([TM 9-2815-252-24, malfunction 3](../library/tm-9-2815-252-24-dn2m.html)).
2. **Fuel in the tank, valve open.** Look in the tank or dip it; do not trust
   the gauge. Check every fuel valve between tank and engine is open
   ([Engineman 3 & 2, p. 266](../library/navedtra-engineman-3-2-1979.html)).
3. **Water in the fuel.** Drain a little from the bottom of the water-separating
   filter into a clear jar. Water settles at the bottom. Drain until clean fuel
   comes out. Some filters block completely when they meet water
   ([Construction Mechanic 3 & 2, pp. 119-120](../library/navedtra-construction-mechanic-3-2-1978.html)).
   See [Water or bug in the diesel](fuel-contamination.html).
4. **Air in the fuel.** If the engine ran out of fuel, a filter was just
   changed, or the bleed screw on the filter gives cloudy or bubbly fuel, there
   is air in the system
   ([Engineman 2, p. 241](../library/navpers-engineman-2-1957.html)).
   Bleed it: see [Bleeding air from a diesel fuel system](bleeding-a-diesel.html).
5. **Blocked filter.** If fuel will not flow freely through the filters when
   you bleed, change the elements
   ([Engineman 3 & 2, p. 267](../library/navedtra-engineman-3-2-1979.html);
   [TM 9-2815-254-24, malfunction 3, step 2](../library/tm-9-2815-254-24-isuzu-c240.html)).
6. **Cold engine: use the glow plugs or heater.** Hold the pre-heat for the
   time in your manual, then crank. If the engine starts easily when warm but
   not when cold, test the glow plugs
   ([TM 9-2815-252-24, malfunction 4](../library/tm-9-2815-252-24-dn2m.html)).
7. **Air in.** Check that nothing blocks the air intake or air filter, and that
   the engine compartment vents are open.
8. **Exhaust out.** Check the exhaust seacock (if fitted) is open.

**Water danger while cranking.** On an engine with a wet exhaust, the
raw-water pump keeps pumping while you crank. If the engine does not fire,
water can fill the exhaust and run back into the cylinders
([Wikipedia, "Hydrolock"](../library/wikipedia-en.html)). If you must crank
for a long time (for example while bleeding), close the raw-water seacock, and
open it again **as soon as the engine fires**.

## Why

Compression heat is what lights a diesel. A cold block, a slow starter or
thick oil can steal enough heat that the fuel does not ignite
([Engineman 3 & 2, p. 270](../library/navedtra-engineman-3-2-1979.html)).
Glow plugs and air-intake heaters add heat for starting
([Engineman 3, pp. 453-455](../library/navpers-engineman-1957.html);
[Wikipedia, "Glow plug"](../library/wikipedia-en.html)). Air in the
high-pressure pump is compressed and expanded instead of opening the injector,
so no fuel is sprayed: the pump is "airbound"
([Engineman 3 & 2, p. 266](../library/navedtra-engineman-3-2-1979.html)).

## Check that it worked

- The engine fires within a few seconds of cranking and settles to an even
  idle.
- Cooling water comes out of the exhaust within a few seconds. If it does not,
  stop and see [Engine overheating](engine-overheating.html).
- Oil pressure rises at once; if not, stop and see
  [Low oil pressure alarm](low-oil-pressure.html).

## If that fails

The next causes in both Army tables are, in order: dirty or faulty injectors,
wrong injection-pump timing, and a faulty injection pump
([TM 9-2815-252-24, malfunction 3, steps 4-6](../library/tm-9-2815-252-24-dn2m.html);
[TM 9-2815-254-24, malfunction 3, steps 4-6](../library/tm-9-2815-254-24-isuzu-c240.html)).
Low compression from worn rings or leaking valves also stops a diesel starting
([Engineman 3 & 2, pp. 268-269](../library/navedtra-engineman-3-2-1979.html)).
These need tools, test gear and your engine's manual.

**Starting fluid (ether).** It ignites much more easily than diesel and is
highly flammable ([Engineman 3, pp. 456-457](../library/navpers-engineman-1957.html)).
Use it only if your engine's manual allows it.

**Larger engines.** Check that cylinder test cocks are closed, the throttle is
not at "off", any overspeed trip is reset, and a hydraulic governor has oil
([Engineman 3 & 2, pp. 266 and 269-270](../library/navedtra-engineman-3-2-1979.html)).

If it still will not start, make a plan without the engine: sail, anchor, or
arrange a [tow](../run-the-boat/towing.html). Background:
[The diesel fuel system](../know-your-boat/diesel-fuel-system.html).
