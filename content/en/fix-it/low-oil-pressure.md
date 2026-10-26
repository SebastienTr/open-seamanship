---
title: Low oil pressure alarm
summary: The oil pressure light or buzzer comes on, or the gauge drops. Stop the engine as soon as it is safe, then check level, oil condition and the sender.
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
  - id: navpers-engineman-2-1957
    locator: "Ch. 11 'Auxiliary machinery and equipment', diesel emergency generators, 'Lubricating system': 'Do not operate the engine without lubricating oil pressure' and causes of loss of oil pressure in most probable order, p. 464"
  - id: navpers-engineman-1957
    locator: "Engineman 3 (NAVPERS 10539): ch. 13, starting after routine securing, step 14 (shut down if oil pressure does not rise at once), p. 451; ch. 14, 'Maintenance of strainers' (metal particles in drained oil), pp. 495-496; 'Oil changes' (water makes oil cloudy; change oil after water, fuel dilution or overheating), pp. 498-499"
  - id: navedtra-construction-mechanic-3-2-1978
    locator: "Ch. 5 'Cooling and lubricating systems', oil pressure readings, gauge faults, strainer, oil pump and relief valve, pp. 144-145"
  - id: tm-9-2815-254-24-isuzu-c240
    locator: "Table 3-2 'Troubleshooting', malfunction 9 'Low oil pressure', p. 3-7"
  - id: tm-9-2815-252-24-dn2m
    locator: "Table 3-2 'Troubleshooting', malfunction 9 'Low oil pressure', p. 3-8"
  - id: navedtra-engineman-3-2-1979
    locator: "Ch. 13 'Troubleshooting': instruments must be checked when suspected of being inaccurate, pp. 260-261; 'Leakage of fuel oil' (crankcase dilution from leaking injectors), p. 279"
uncertain:
  - "Normal oil pressures at idle and at cruising speed are in your engine's manual. No cleared source gives figures for small marine diesels, and this page gives none."
  - "Where water in the oil comes from (head gasket, oil cooler, exhaust back-flow, condensation) is not listed in one place in the sources; the list on this page is a reviewer's check item."
  - "Many small engines have only a warning light, worked by a pressure switch. A faulty switch or wire can give a false alarm, but you cannot tell that without a mechanical test gauge. Treat every alarm as real until proven otherwise."
---

## Situation

The oil pressure warning light or buzzer comes on while the engine runs, or the
gauge reads lower than usual. Running a diesel without oil pressure wrecks its
bearings. The Navy rule is short: "Do not operate the engine without
lubricating oil pressure" ([Engineman 2, p. 464](../library/navpers-engineman-2-1957.html)).

At start-up the light is normally on until the engine runs. If the pressure
does not rise straight away after starting, stop the engine
([Engineman 3, p. 451](../library/navpers-engineman-1957.html)).

## Do now

1. **Stop the engine as soon as it is safe.** If you need it for a few
   minutes to get clear of danger, run it at the lowest revs you can. See
   [Engine failure near danger](../emergency/engine-failure-near-danger.html).
2. **Listen as it runs down.** Knocking with low oil pressure points to worn
   bearings ([Engineman 2, p. 464](../library/navpers-engineman-2-1957.html)).
   If you heard knocking, do not restart.
3. **Wait a few minutes, then check the level** on the dipstick with the boat
   as level as you can get it. Low? Look for the leak before you top up: under
   the engine, the oil filter, the drain hose, the oil cooler pipes.
4. **Look at the oil on the dipstick.**
   - *Milky, grey or with droplets:* water in the oil. Cloudy oil shows water
     ([Engineman 3, p. 498](../library/navpers-engineman-1957.html)). Do not
     run the engine. The water may come from a failed head gasket, an oil
     cooler or a leaking exhaust. Change the oil when the cause is fixed.
   - *Thin, high on the dipstick, smelling of diesel:* fuel dilution, for example
     from a leaking injector
     ([Engineman 3 & 2, p. 279](../library/navedtra-engineman-3-2-1979.html)).
     Thin oil gives low pressure.
   - *Shiny metal particles:* bearing wear
     ([Engineman 3, pp. 495-496](../library/navpers-engineman-1957.html)).
     Get a mechanic.
5. **Was the engine hot?** Overheated oil thins and pressure falls. If the
   temperature was high too, go to [Engine overheating](engine-overheating.html)
   ([TM 9-2815-252-24, malfunction 9](../library/tm-9-2815-252-24-dn2m.html)).
6. **Check the sender and wiring.** A loose or corroded wire on the oil
   pressure switch can give a false alarm. A gauge fault is a common cause of
   strange readings
   ([Construction Mechanic 3 & 2, pp. 144-145](../library/navedtra-construction-mechanic-3-2-1978.html);
   [Engineman 3 & 2, pp. 260-261](../library/navedtra-engineman-3-2-1979.html)).
   Only a separate test gauge proves it.

## Why

The Navy list of causes of lost oil pressure, in the most probable order,
starts with a **dirty filter**, then a stuck check valve in the pump suction,
**too little oil**, a wrongly set or stuck pressure-regulating (relief) valve,
air leaks in the pump suction, leaking or broken oil pipes, **worn bearings**
(heard as knocking), and a leak in the oil cooler (oil in the cooling-water
discharge) ([Engineman 2, p. 464](../library/navpers-engineman-2-1957.html)).
The Army table for a small diesel adds the **wrong grade of oil** and an
**overheated engine** at the top, then the relief valve, a clogged pump
strainer and the pump itself
([TM 9-2815-254-24, malfunction 9](../library/tm-9-2815-254-24-isuzu-c240.html)).
Oil pumps rarely fail outright; look at the cheap causes first
([Construction Mechanic 3 & 2, p. 145](../library/navedtra-construction-mechanic-3-2-1978.html)).

## Check that it worked

- After fixing the cause, the light goes out (or the gauge rises) within a few
  seconds of starting.
- Pressure stays steady when the engine is hot and at idle, which is when it
  is lowest.
- The dipstick level stays where it should after a run.

## If that fails

- **Change the oil and filter** with the grade in your engine's manual. A
  filter change is cheap and is first on the Navy list.
- **Oil sludge or a blocked pickup strainer** needs the sump off on many
  engines ([Construction Mechanic 3 & 2, p. 145](../library/navedtra-construction-mechanic-3-2-1978.html)).
- **Relief valve, oil pump, worn bearings:** workshop jobs.
- If you must move the boat, sail or [get a tow](../run-the-boat/towing.html)
  rather than run an engine with no oil pressure.

Background: [Engine maintenance routine](../know-your-boat/engine-maintenance.html).
