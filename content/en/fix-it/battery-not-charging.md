---
title: Battery not charging
summary: The charge warning light stays on, the voltmeter reads low with the engine running, or the batteries are flat every morning. How to find the cause safely on a 12 V boat.
kind: guide
section: fix-it
region: international
language: en
licence: CC-BY-SA-4.0
safety: critical
status: draft
authors: [claude]
reviewers: []
reviewed: null
sources:
  - id: tm-9-8000-automotive-1985
    locator: "chapter 12, para. 12-2e (electrolyte, specific gravity 1.28 at full charge), p. 12-3; para. 12-10c (hydrogen and oxygen from charging), p. 12-10; chapter 13, para. 13-8 (belt drive and tension), p. 13-6; para. 13-27 (regulated voltage), para. 13-30b (field relay and no-charge warning light), p. 13-35; chapter 17, para. 17-2 (voltmeter normal range 13.2 to 14.5 V; no-charge lamp), pp. 17-1 to 17-3"
  - id: navedtra-neets
    locator: "Module 1 (NAVEDTRA 14173A), chapter 2, section 2.4.3 (hydrometer and battery maintenance) and 2.4.3.4 (safety precautions with batteries), pp. 2-25 to 2-28; section 2.4.5.8 (gassing), p. 2-30. Module 16 (NAVEDTRA 14188A), chapter 1, section 1.6 (voltage measurements, set the meter on the highest range), pp. 1-25 to 1-26"
  - id: navedtra-electricians-mate-3-2-1981
    locator: "chapter 2, Safety precautions (no rings, watches or metal objects near live parts), p. 2-12"
  - id: wikipedia-en
    locator: "'Lead–acid battery', sections 'Voltages for common usage', 'Measuring the charge level' and 'Safety'; 'Alternator (automotive)', section 'Field regulation'"
  - id: mca-fishermens-safety-guide
    locator: "Section 3, engine room hazards (unventilated batteries; keep items clear that could short across them), PDF pp. 29-30"
uncertain:
  - "Resting-voltage figures are for ordinary lead-acid batteries. Lithium (LiFePO4) banks use different voltages, have their own battery management system, and some can switch themselves off. Follow the installer's figures for those."
  - "The figure of about 12.6 V for a full 12 V lead-acid battery at rest is worked out from the 2.1 V per cell given on Wikipedia. Exact values depend on battery type and temperature."
  - "No cleared source says that opening the battery switch while the engine runs damages the alternator. This is widespread practice for older alternators and is kept here as a precaution; a marine electrician should confirm."
  - "Boats with split-charge relays, diode isolators, DC-DC chargers or smart regulators add more places for a fault. No cleared source covers them; check the wiring diagram for your own boat."
---

## Situation

The charge warning light stays on with the engine running, or the voltmeter
does not rise above the battery's resting voltage, or the batteries are flat
again after a night at anchor. On a 12 V system with the engine running, the
voltage at the battery should normally be between **13.2 and 14.5 V**
([TM 9-8000, para. 17-2](../library/tm-9-8000-automotive-1985.html)). On
24 V systems, double the figures on this page.

## Do now

**Safety first.** A charging battery gives off hydrogen and oxygen, an
explosive mixture
([TM 9-8000, para. 12-10](../library/tm-9-8000-automotive-1985.html)). No
smoking, flames or sparks near it. Take off rings and your watch. Never let a
spanner touch both terminals, or one terminal and the engine
([NEETS Module 1, 2.4.3.4](../library/navedtra-neets.html)). If you get acid
in your eyes, flush them with fresh water for at least 15 minutes.

1. **Look at the belt** (engine stopped). Is it there, tight, and not glazed
   or oily? The alternator is driven by a belt, often the same one that
   drives the water pump. If the belt is gone, also watch the engine
   temperature: see [Engine overheating](engine-overheating.html).
2. **Check the battery switch** is on the bank you expect, and any charge
   selector is set correctly.
3. **Measure the battery voltage** with the engine stopped and no load, then
   with the engine running at a fast idle. Set the meter to its highest DC
   range first, then step down
   ([NEETS Module 16, 1.6](../library/navedtra-neets.html)).
   - Running voltage the same as resting voltage: **no charge**. Go to step 4.
   - Running voltage above about 14.5 V, battery hot or smelling of acid,
     cells bubbling hard: **overcharging**. Stop the engine as soon as it is
     safe to do so, keep sparks and flames away and ventilate the battery
     space. Do not open the battery switch with the engine running (see
     "If that fails"). This can make a battery burst.
   - Running voltage normal but battery flat next morning: the battery is
     worn out, or something is drawing current. Go to step 6.
4. **Check the connections** at the alternator, the battery terminals and
   the engine earth (negative) strap. Look for loose, green or white
   corroded terminals, and wires that are warm after running. Clean and
   tighten them with the engine stopped.
5. **Check the warning lamp and fuses.** On many alternators, the small
   current that wakes up the alternator passes through the warning lamp. If
   the bulb is blown or that thin wire is off, the alternator may not charge
   at all ([Wikipedia, 'Alternator (automotive)'](../library/wikipedia-en.html)).
   With the key on and engine stopped, the lamp should light. If it does
   not, suspect the bulb, the fuse, or the wire.
6. **Test the battery.** Let it rest for some hours off charge. A full 12 V
   lead-acid battery at rest reads about 12.6 V (6 cells of about 2.1 V).
   If you can open the cells, use a hydrometer: full charge is about 1.28
   at 27 °C (80 °F); a cell much lower than the others is failing
   ([TM 9-8000, para. 12-2](../library/tm-9-8000-automotive-1985.html)).
7. **If all of that is good,** the alternator or its regulator has failed.
   Change it if you carry a spare, or save power and charge another way.

## Why

The alternator makes current only when its field coil is fed and the belt
turns it. The regulator then holds the voltage in a narrow band, high enough
to push current into the battery, low enough not to boil it
([TM 9-8000, paras 13-27 and 13-30](../library/tm-9-8000-automotive-1985.html)).
Most "no charge" faults on boats are the simple ones: belt, switch,
corroded connection, or the warning-lamp wire. Corrosion adds resistance, so
the alternator's output is lost as heat in the joint.

Overcharging is the dangerous fault. Above the gassing voltage (about 14.4 V
for a normal lead-acid battery) water is split into hydrogen and oxygen. A
spark from a loose terminal can ignite the gas and blow the top off the
battery, spraying acid
([Wikipedia, 'Lead–acid battery', 'Safety'](../library/wikipedia-en.html)).
Keep battery boxes ventilated to outside
([MCA guide, PDF p. 30](../library/mca-fishermens-safety-guide.html)).

## Check that it worked

- Warning lamp lights with key on, goes out once the engine runs.
- Battery voltage rises to between 13.2 and 14.5 V within a minute or two
  of starting, and falls slowly back as the battery fills.
- No terminal or cable is warm to the touch after half an hour of charging.

## If that fails

- **Save power:** switch off everything not needed for safety (navigation
  lights, VHF, bilge pump come first). Keep one battery for starting.
- Charge from solar, wind, a generator or shore power if you have it.
- Avoid opening the battery switch while the engine is running; on many
  alternators the voltage surge can damage it.
- **Wiring smells hot or smokes:** isolate the battery and see
  [Fire on board](../emergency/fire-on-board.html).
- To trace a wiring fault step by step, see
  [Finding a 12 V electrical fault](electrical-fault-finding.html). For how
  the system is built, see [Batteries](../know-your-boat/batteries.html) and
  [12 V and 24 V systems on board](../know-your-boat/marine-electrical-systems.html).
- **Engine will not crank** because the battery is flat: see
  [Engine won't turn over](engine-wont-crank.html).
- **Acid on skin or in eyes:** flush with water for 15 minutes and see
  [Burns](../health/burns.html).
