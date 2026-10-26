---
title: Engine stops or loses power
summary: The diesel dies, slows under load, or will not reach its usual revs. Most often fuel starvation, then air, then something holding the boat back.
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
  - id: navedtra-engineman-3-2-1979
    locator: "Ch. 13 'Troubleshooting': 'Engine stalls frequently or stops suddenly', 'Misfiring', pp. 270-271; 'Clogged air cleaners and silencers', p. 271; 'Obstruction in the exhaust system', 'Insufficient intake air', pp. 272-273; 'Piston seizure', 'Defective auxiliary drive mechanisms', pp. 274-275; figures 13-5 and 13-6 and 'Engine will not carry load', p. 276; 'Clogged fuel filters', p. 267"
  - id: tm-9-2815-252-24-dn2m
    locator: "Table 3-2 'Troubleshooting', malfunctions 5 (misfires, runs irregularly or stalls) and 6 (does not develop full power), pp. 3-4 to 3-7"
  - id: tm-9-2815-254-24-isuzu-c240
    locator: "Table 3-2 'Troubleshooting', malfunctions 5 and 6, pp. 3-5 to 3-6"
  - id: navpers-engineman-2-1957
    locator: "Ch. 6 'Fuel injection equipment', 'Bleeding air out of fuel system' (air leaks in suction piping), p. 241"
  - id: navedtra-construction-mechanic-3-2-1978
    locator: "Ch. 4 'Fuel systems', 'Water in fuel system' and 'Air in fuel system', pp. 119-120"
  - id: navpers-engineman-1957
    locator: "Engineman 3 (NAVPERS 10539), ch. 13, 'Load' (overload signs), p. 459"
  - id: tm-55-1030-evinrude-1945
    locator: "Section XII 'Trouble shooting', para 41 'Engine runs but boat makes little or no progress' (rope or obstruction dragging, weeds on propeller), p. 19"
  - id: tm-5-278-outboard-motors-1944
    locator: "Section IV, para 14 b and figure 35 (tank vent must be open for fuel to flow), pp. 32-34"
uncertain:
  - "A blocked fuel-tank vent is given as a cause in the 1944 outboard manual (petrol). The same physics applies to a diesel tank, but no cleared diesel source lists it. A reviewer should confirm."
  - "Engines that stop after heavy rolling, or when the tank is low, often have dirt or water stirred up from the tank bottom, or an uncovered fuel pickup. This is widely reported by sailors but not stated in the cleared sources."
---

## Situation

The engine stops by itself, or it runs but loses power: it will not reach its
usual revs, slows when you open the throttle, or misfires. If it stops and
will not restart, use this page with [Engine turns over but won't start](engine-wont-start.html).

If you are near danger, see
[Engine failure near danger](../emergency/engine-failure-near-danger.html)
before anything else.

## Do now

1. **Make the boat safe.** Sail, anchor or drift clear before you open up the
   engine.
2. **Look at the gauges and alarms before they go dark.** High temperature?
   Go to [Engine overheating](engine-overheating.html). Low oil pressure? Go to
   [Low oil pressure alarm](low-oil-pressure.html).
3. **Fuel in the tank.** Dip it; do not trust the gauge.
4. **Filters and water.** Check the bowl of the water-separating filter. Drain
   any water. A clogged filter can starve the engine and cause loss of power,
   misfiring or stopping ([Engineman 3 & 2, pp. 267 and 270](../library/navedtra-engineman-3-2-1979.html)).
   Water in the fuel makes an engine miss and then stop
   ([Construction Mechanic 3 & 2, pp. 119-120](../library/navedtra-construction-mechanic-3-2-1978.html)).
   Change the elements if in doubt; see [Water or bug in the diesel](fuel-contamination.html).
5. **Air in the fuel.** If the engine misses, then stops, and the filter bleed
   screw gives frothy fuel, air is getting in. The smallest leak on the suction
   side of the lift pump lets air in
   ([Engineman 2, p. 241](../library/navpers-engineman-2-1957.html)).
   Tighten fittings, then [bleed the system](bleeding-a-diesel.html).
6. **Tank vent.** A blocked vent stops fuel flowing as the tank empties; the
   same is true of any fuel tank
   ([TM 5-278, para 14 b](../library/tm-5-278-outboard-motors-1944.html)).
   Check the vent pipe and its screen.
7. **Air filter and intake.** A clogged air cleaner causes misfiring, loss of
   power, smoke and overheating
   ([Engineman 3 & 2, p. 271](../library/navedtra-engineman-3-2-1979.html)).
8. **Propeller.** If the engine revs but the boat is slow, or the engine slows
   and labours, look for rope, net or weed on the propeller
   ([TM 55-1030, para 41](../library/tm-55-1030-evinrude-1945.html)).
   See [Rope or net round the propeller](fouled-propeller.html).

## Why

Both Army tables for small diesels start with the same short list for an
engine that stalls or lacks power: air in the fuel, a clogged fuel filter, the
governor, a blocked air intake, and overheating
([TM 9-2815-252-24, malfunctions 5 and 6](../library/tm-9-2815-252-24-dn2m.html);
[TM 9-2815-254-24, malfunctions 5 and 6](../library/tm-9-2815-254-24-isuzu-c240.html)).
The Navy manual says the same troubles that stop an engine starting also make
it stall, and that one fault, such as a clogged filter, can cause several
symptoms at once ([Engineman 3 & 2, p. 270](../library/navedtra-engineman-3-2-1979.html)).

An engine that is overloaded shows high temperatures and smoky exhaust
([Engineman 3, p. 459](../library/navpers-engineman-1957.html)): a fouled
propeller or a heavy tow does this.

## Check that it worked

- The engine reaches its usual full revs in neutral and its usual cruising
  revs in gear.
- It runs for a long spell at your normal cruising power without stopping
  or misfiring. A filter that is slowly blocking may take time to show again.
- Fuel in the filter bowl stays clear, with no bubbles.

## If that fails

**Sudden stop with a bang or a grinding noise.** Do not restart. A broken
valve, a seized piston or a broken gear in the timing drive can stop an engine
suddenly ([Engineman 3 & 2, pp. 274-275](../library/navedtra-engineman-3-2-1979.html)).
Turning it would cause more damage. See
[Knocking, vibration or unusual noise](engine-knocking-or-vibration.html).

**Exhaust blocked.** A restricted exhaust or silencer raises back pressure and
causes loss of power, high exhaust temperature or stalling
([Engineman 3 & 2, pp. 272-273](../library/navedtra-engineman-3-2-1979.html)).
On small boats, check the exhaust mixing elbow and the outlet.

**Still losing power.** The next causes are injectors, injection timing, the
injection pump and low compression
([TM 9-2815-254-24, malfunction 5](../library/tm-9-2815-254-24-isuzu-c240.html)).
These need a mechanic and your engine's manual.

**Larger engines.** Add to the list: turbocharger or blower faults, low
cooling-water temperature and governor faults
([Engineman 3 & 2, pp. 270-274](../library/navedtra-engineman-3-2-1979.html)).
See also [Engine speed hunting or surging](diesel-hunting-or-surging.html).
