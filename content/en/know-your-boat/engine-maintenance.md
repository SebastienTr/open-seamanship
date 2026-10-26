---
title: Engine maintenance routine
summary: Checks before starting, while running and after stopping, plus the periodic jobs (oil, filters, impeller, belts, zincs) that prevent most engine failures at sea.
kind: explainer
section: know-your-boat
region: international
language: en
licence: CC-BY-SA-4.0
safety: normal
status: draft
authors: [claude]
reviewers: []
reviewed: null
sources:
  - id: navedtra-engineman-3-2-1979
    locator: "Ch. 8, cooler leaks shown by water in the lube oil or a change in oil volume, p. 170; ch. 12 'Diesel Engine Operating Procedures': starting checks (coolant level and venting, oil level, prime fuel, alarms, oil pressure after starting, do not load a cold engine), pp. 246-247; starting after a long idle period, p. 247; normal operating procedures, keep a log, listen for new noises, pp. 247-248; load and warming up, p. 248; pressures and temperatures, fuel, service tank water, p. 249; stopping and securing, p. 250; precautions (cooling water, cleanliness), pp. 250-251"
  - id: tm-9-2815-252-24-dn2m
    locator: "Ch. 3, sec. I, para. 3-1 and Table 3-1 'Preventive Maintenance Checks and Services' (oil filter 250 h, fuel filter 500 h, injectors 1000 h, oil pressure 1500 h), p. 3-1; general maintenance notes (new belt tension after 20 hours), ch. 3"
  - id: navpers-16178-fundamentals-of-diesel-engines
    locator: "Ch. 11, sec. 11-2 'Lubricating systems', additive oils are used up, oil change periods, filter elements changed with the oil, pp. 72-73; sec. 11-1 drain sumps of filters and strainers, p. 72"
  - id: navpers-engineman-1957
    locator: "Engineman 3, ch. 14 'Care of zincs' (inspect at least monthly, close sea connections first), pp. 500-501"
  - id: fao-small-fishing-vessel-inspection-2025
    locator: "Sec. 4 machinery inspection lists (sea inlet valves and strainers, belts, hoses, filters, spares and tools, electrical), p. 42; Annex A machinery checklist items 2470-2650, p. 57"
  - id: doe-hdbk-1018-mechanical-science
    locator: "Vol. 1, ME-01, 'Engine Lubrication' (filters remove metal picked up by wear), p. 14; 'Engine Protection', p. 39"
uncertain:
  - "Service intervals depend on the engine. The only modern small-diesel intervals in a cleared source are for a 1993 US Army generator engine (oil filter 250 h, fuel filter 500 h). Small marine engines often need oil changes far more often. Your engine's manual is the authority; a maker's manual can be packed in the private shelf."
  - "Rubber raw-water impellers are commonly changed every season or so; no cleared source gives an interval."
---

## Why a routine

Engines rarely fail without warning. A routine catches the warning: a belt
starting to fray, a drop of oil where there was none, a sound that was not
there last week. The Navy's advice is to log temperatures and pressures
regularly and compare them over time, so that slow changes show up, and to
listen for new noises
([Engineman 3 & 2, pp. 247-248](../library/navedtra-engineman-3-2-1979.html)).
Keep a simple engine log: date, engine hours, what you checked, what you
changed.

## Before starting (every time)

1. **Raw-water seacock open.** Strainer clear and its lid sealed.
2. **Coolant level** in the expansion tank (engine cold). Do not open a hot
   pressure cap.
3. **Engine oil level** on the dipstick. A level that rises, or oil that looks
   milky, can mean water in the oil, for example from a leaking oil cooler
   ([Engineman 3 & 2, p. 170](../library/navedtra-engineman-3-2-1979.html)).
   Do not run the engine until you know why. See
   [Low oil pressure alarm](../fix-it/low-oil-pressure.html).
4. **Gearbox oil level**, if your gearbox has a dipstick.
5. **Fuel**: enough in the tank for the trip plus a reserve; tank valve open;
   no water in the filter bowl.
6. **Belts**: present, not frayed, tight enough.
7. **Bilge under the engine**: look for fresh oil, fuel or coolant.
8. **Battery switch on**, alarms working when you turn the key.

These follow the Navy's starting checks: coolant level and venting, oil level,
fuel primed and enough of it, alarms tested
([Engineman 3 & 2, pp. 246-247](../library/navedtra-engineman-3-2-1979.html)).

## Starting and running

- After starting, **oil pressure should rise at once**. If not, stop the engine
  and find out why
  ([Engineman 3 & 2, p. 247](../library/navedtra-engineman-3-2-1979.html)).
- **Look for cooling water at the exhaust** within a few seconds.
- **Warm up before loading.** Loading a cold engine causes carbon, extra wear
  and fuel in the oil
  ([Engineman 3 & 2, pp. 247-248](../library/navedtra-engineman-3-2-1979.html)).
- **Watch the gauges** and know your normal readings. Unusual operation is
  nearly always load, lubrication, cooling, speed or fuel
  ([Engineman 3 & 2, p. 248](../library/navedtra-engineman-3-2-1979.html)).

## After stopping

- Close the seacocks if the boat will be left (unless the engine maker says
  otherwise).
- Wipe the engine down and keep the bilge under it clean and dry, so new leaks
  are easy to see. Repair even small faults promptly
  ([Engineman 3 & 2, p. 250](../library/navedtra-engineman-3-2-1979.html)).
- Note the engine hours in the log.

## Periodic jobs

| Job | Why | Notes |
| --- | --- | --- |
| Engine oil and oil filter | Oil additives get used up; the filter holds wear metal ([Fundamentals, pp. 72-73](../library/navpers-16178-fundamentals-of-diesel-engines.html); [DOE, p. 14](../library/doe-hdbk-1018-mechanical-science.html)) | Change the filter with the oil. Warm the engine first so the oil drains. |
| Fuel filters (primary and fine) | Catch dirt and water before the injection pump | Drain the bowls often ([Fundamentals, p. 72](../library/navpers-16178-fundamentals-of-diesel-engines.html)). Bleed after changing. Carry spares. |
| Raw-water impeller | Rubber vanes wear and crack | See [Changing a raw-water pump impeller](../fix-it/changing-a-raw-water-impeller.html). Carry a spare. |
| Raw-water strainer | Weed and shells block flow | Clean whenever you see debris; close the seacock first. |
| Zincs (anodes) on the engine | Protect the heat exchanger | Inspect, clean or renew. Navy practice: at least monthly ([Engineman 3, pp. 500-501](../library/navpers-engineman-1957.html)). |
| Belts | Drive the water pump and alternator | Check tension and wear; a new belt stretches, so check it again after about 20 hours ([TM 9-2815-252-24, ch. 3](../library/tm-9-2815-252-24-dn2m.html)). |
| Coolant | Antifreeze inhibitors wear out | Renew as the engine's manual says. |
| Hoses and clips | Rubber hardens and cracks | Squeeze each hose; look for rust on clips. |
| Air filter | Clean air for the engine | Clean or renew. |
| Gearbox oil | Lubricates the gearbox | As the gearbox manual says. |
| Injectors | Spray quality decays | Tested by a specialist; one small diesel's schedule says every 1000 hours ([TM 9-2815-252-24, Table 3-1](../library/tm-9-2815-252-24-dn2m.html)). |

For scale: a 1993 US Army manual for a small two-cylinder diesel sets the oil
filter at 250 hours and the fuel filter at 500 hours
([TM 9-2815-252-24, Table 3-1](../library/tm-9-2815-252-24-dn2m.html)). The
1945 Navy rule, without oil analysis, was a 100-hour oil change for small,
high-speed engines
([Fundamentals of Diesel Engines, p. 73](../library/navpers-16178-fundamentals-of-diesel-engines.html)).
Your engine's manual overrides both.

## Spares and tools to carry

An inspection list for small fishing vessels asks for spares and tools on
board, including belts, hoses and filters
([FAO 2025, p. 42 and Annex A](../library/fao-small-fishing-vessel-inspection-2025.html)).
A sensible small-boat kit: impeller and gasket, fuel filters, oil filter, oil
for one change, one of each belt, a length of the main hoses and spare clips,
spare zincs, and the tools that fit them. Most fixes at sea are one of these
parts.

## Safety while working

- **Stop the engine** before reaching near belts or the flywheel.
- **Close the seacock** before opening anything on the raw-water side
  ([Engineman 3, p. 501](../library/navpers-engineman-1957.html)).
- **Never add cold water to a hot engine**
  ([Engineman 3 & 2, p. 250](../library/navedtra-engineman-3-2-1979.html)).
- Keep oily rags out of the bilge, and clean spills: cleanliness is "one of the
  basic essentials" of running a diesel
  ([Engineman 3 & 2, p. 251](../library/navedtra-engineman-3-2-1979.html)).

## Related pages

- [How a diesel engine works](how-a-diesel-engine-works.html)
- [Diesel cooling systems](diesel-cooling-systems.html)
- [The diesel fuel system](diesel-fuel-system.html)
- [Laying up an engine for winter](winterising-an-engine.html)
- [Batteries](batteries.html)
