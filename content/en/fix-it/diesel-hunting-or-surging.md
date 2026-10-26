---
title: Engine speed hunting or surging
summary: The revs rise and fall by themselves at a steady throttle. Usually fuel starvation or air in the fuel on small diesels; on larger engines, the governor or fuel racks.
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
  - id: navpers-16178-fundamentals-of-diesel-engines
    locator: "Ch. 13 'Engine controls', section 13-2, definitions of hunting and stability, p. 90; 'Hunting' (lag in governor action, over-control), p. 91"
  - id: navedtra-engineman-3-2-1979
    locator: "Ch. 13 'Troubleshooting': 'Inoperative engine governor' (binding linkage, low oil in hydraulic governors), pp. 269-270; 'Engine hunts or will not secure', 'Speed control system', 'Fuel control racks', pp. 277-278 and figure 13-7; 'Leakage of fuel oil', 'Accumulation of lube oil' (runaway), p. 279"
  - id: tm-9-2815-252-24-dn2m
    locator: "Table 3-2 'Troubleshooting', malfunction 5 'Engine misfires or runs irregularly or stalls frequently', steps 1-3, pp. 3-4 to 3-5"
  - id: tm-9-2815-254-24-isuzu-c240
    locator: "Table 3-2 'Troubleshooting', malfunction 5, steps 1-2, p. 3-5"
  - id: navpers-engineman-2-1957
    locator: "Ch. 6 'Fuel injection equipment', 'Bleeding air out of fuel system' (air leaks in suction piping), p. 241"
  - id: wikipedia-en
    locator: "'Diesel engine runaway', sections 'Causes' and 'Stopping a runaway engine'"
uncertain:
  - "On small marine diesels with a simple mechanical governor, fuel starvation (a part-blocked filter or a small air leak) is in practice a common cause of surging. The Army tables list air and a clogged filter first for irregular running; no cleared source says which is most common on yachts."
  - "Smothering the air intake to stop a runaway engine is described by Wikipedia. It can be dangerous (hands near a strong intake; some intakes are hard to reach). Use the fuel shut-off and the stop control first."
---

## Situation

At a steady throttle setting, the engine speed rises and falls by itself,
regularly or at random. This is called hunting or surging. It is a sign that
fuel is not reaching the engine evenly, or that the governor that controls
speed is not working smoothly
([Engineman 3 & 2, p. 277](../library/navedtra-engineman-3-2-1979.html)).

Some speed change in big waves is normal: when the propeller comes near the
surface, the load drops and the governor has to catch it
([Engineman 3 & 2, p. 277](../library/navedtra-engineman-3-2-1979.html)).

## Do now

1. **Note when it happens.** Only at idle? Only at one speed? Only under load?
   Getting worse?
2. **Check the fuel filter bowl.** Water, dirt or bubbles? Drain water; change
   the filter if in doubt. A clogged filter is near the top of both Army
   tables for irregular running
   ([TM 9-2815-252-24, malfunction 5](../library/tm-9-2815-252-24-dn2m.html)).
   See [Water or bug in the diesel](fuel-contamination.html).
3. **Look for air in the fuel.** Bubbles in a clear filter bowl or in clear
   fuel hose, or frothy fuel at a bleed screw, mean air is getting in. Check
   every joint from the tank to the lift pump; the smallest leak on the
   suction side lets air in
   ([Engineman 2, p. 241](../library/navpers-engineman-2-1957.html)).
   Then [bleed the system](bleeding-a-diesel.html).
4. **Throttle and stop cables.** Work the throttle and stop controls by hand
   with the engine stopped. They should move freely and not spring back. A
   binding linkage stops the governor working
   ([Engineman 3 & 2, pp. 269-270](../library/navedtra-engineman-3-2-1979.html)).
   Check the cable clamps are tight and the stop lever is fully in run.
5. **Tank vent and fuel supply.** A blocked vent or a kinked fuel hose can
   starve the engine as it draws fuel. See
   [Engine stops or loses power](engine-stops-or-loses-power.html).
6. **Engine temperature.** A thermostat stuck open keeps the engine cold, and
   cold engines run roughly ([TM 9-2815-252-24, malfunction 5, step 4](../library/tm-9-2815-252-24-dn2m.html)).

## Why

A governor watches engine speed and adds or removes fuel to hold it. If it
reacts too late or too much, it overshoots: the engine speeds up too far, the
governor cuts back too far, and the speed swings up and down
([Fundamentals of Diesel Engines, pp. 90-91](../library/navpers-16178-fundamentals-of-diesel-engines.html)).
Friction in the governor or its linkage makes this worse
([Fundamentals of Diesel Engines, p. 91](../library/navpers-16178-fundamentals-of-diesel-engines.html)).
Uneven fuel supply can look the same: air in the fuel and a clogged filter
are among the first checks for irregular running in both Army tables
([TM 9-2815-252-24, malfunction 5](../library/tm-9-2815-252-24-dn2m.html);
[TM 9-2815-254-24, malfunction 5](../library/tm-9-2815-254-24-isuzu-c240.html)).

## Check that it worked

- At a steady throttle the engine holds steady revs in calm water, at idle and
  at cruising speed.
- The fuel in the filter bowl stays clear and bubble-free.

## If that fails

- **Governor and fuel racks.** Sticky or jammed fuel-pump racks cause hunting.
  With the engine stopped and the linkage disconnected, the rack should move
  by hand with no resistance. A sticking rack may come from dirt, damage or a
  sticking pump plunger
  ([Engineman 3 & 2, pp. 277-278](../library/navedtra-engineman-3-2-1979.html)).
  Hydraulic governors (larger engines) hunt when their oil is low
  ([Engineman 3 & 2, p. 270](../library/navedtra-engineman-3-2-1979.html)).
  Adjusting a governor is a job for the engine manual and a mechanic.
- **Injectors and injection pump.** Leaking injectors cause uneven running
  ([Engineman 3 & 2, p. 279](../library/navedtra-engineman-3-2-1979.html)).

**Runaway: speed rises and will not come down.** This is an emergency. The
engine is getting fuel or oil from somewhere the governor cannot control, for
example oil drawn into the air intake
([Engineman 3 & 2, p. 279](../library/navedtra-engineman-3-2-1979.html)).

1. Pull the stop control and close the fuel valve.
2. If it keeps running, it must be starved of air: some people block the air
   intake with a flat board or use a CO2 extinguisher into the
   intake ([Wikipedia, "Diesel engine runaway"](../library/wikipedia-en.html)).
   Never use your hand.
3. Do not restart until a mechanic has found the cause.
