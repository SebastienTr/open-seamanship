---
title: Batteries
summary: How lead-acid (flooded, AGM, gel) and lithium iron phosphate batteries work on a boat, how to tell how charged they are, how they fail, and the dangers of gas, acid, short circuits and thermal runaway.
kind: explainer
section: know-your-boat
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
    locator: "Ch. 12 'Batteries': para. 12-2 construction, cells of 2 V, specific gravity 1.28 when full, p. 12-1 to 12-3; paras. 12-3 to 12-5 discharge and charge, capacity falls with high discharge rate and in cold (about 40 per cent of cranking capacity at -18 °C), deteriorates if left discharged, pp. 12-4 to 12-6; para. 12-6 starting (SLI) and deep-cycle batteries and cycle lives, pp. 12-6 to 12-7; para. 12-8 maintenance-free batteries, p. 12-8; para. 12-10 installation, chlorine gas from salt water on a damaged lead-acid battery, hydrogen and oxygen explosive, ventilation, pp. 12-9 to 12-10; para. 12-11 series and parallel connection, p. 12-10"
  - id: navedtra-neets
    locator: "Module 1 (NAVEDTRA 14173A, 2011), ch. 2: 2.4.3 'Battery Maintenance', specific gravity and hydrometer, pp. 2-25 to 2-27; 2.4.3.4 'Safety Precautions with Batteries' (never short the terminals, no sparks or flames near charging batteries, flush electrolyte from skin or eyes for at least 15 minutes), p. 2-28; 2.4.4 capacity and the 20-hour rating, pp. 2-28 to 2-29; 2.4.5 charging, equalizing and floating charge, gassing and the explosion warning, pp. 2-29 to 2-31"
  - id: wikipedia-en
    locator: "'Lead–acid battery' (revision 2026-10): sections 'Voltages for common usage' (cell voltage 2.1 V full, 1.8 V discharged), 'Absorbent glass mat', 'Gelled electrolytes', 'Valve-regulated lead–acid (VRLA) batteries', 'Starting batteries', 'Deep-cycle batteries', 'Sulfation and desulfation', 'Safety'. 'Lithium iron phosphate battery' (revision 2026-10-13): sections 'Specifications' (3.2 V nominal cell, 3.60-3.65 V maximum charge), 'Viable alternative to lead-acid batteries' (four cells give 12.8 V; charging must be adapted; protection needed below 2.5 V), 'Safety', 'State of charge estimation challenges' (flat voltage between about 20 and 80 per cent). 'Lithium-ion battery' (revision 2026-10-23): sections 'Fire hazard' (charging below 0 °C plates lithium; flammable electrolyte; toxic, flammable smoke), 'Damaging and overloading' (thermal runaway, battery management circuits), 'Voltage limits'"
  - id: mca-small-fishing-vessel-code-2024
    locator: "Sec. 4.8.3 'D.C. Systems Up To 24 volts', 4.8.3.4 (batteries secured, protected from short circuit, clear of heat) and 4.8.3.5 (double-pole cut-off switch at each battery or bank; automatic bilge pumps connected before it); 6.12.1 (batteries securely fastened)"
uncertain:
  - "Lithium battery practice on small boats is changing fast and is not covered by the cleared government manuals. This page uses Wikipedia for lithium facts. Follow the battery maker's instructions and any current national guidance; have a lithium installation checked by a qualified marine electrician."
  - "Voltage-to-charge tables for 12 V lead-acid batteries vary by type and temperature, and the voltage must be read after the battery has rested for some hours. The figures here (about 12.6 V full, about 12.0 V nearly flat at rest) follow from the cell voltages in the Wikipedia article (2.1 V and below about 2.0 V per cell), not from a cleared table."
  - "Joining only batteries of the same type, age and size, and keeping a separate starting battery, are common good practice rather than statements in a cleared source."
  - "The common advice not to discharge lead-acid batteries below about half their capacity is not stated as a figure in a cleared source; the sources say only that deep discharge shortens life, especially of starting batteries."
---

## What a battery does on board

A battery stores energy as chemistry. It starts the engine, and on a sailing
boat or at anchor it runs everything else: lights, radio, pumps, instruments.
The engine's alternator (or solar panels, wind or shore power) recharges it.
See [12 V and 24 V systems on board](marine-electrical-systems.html).

## Lead-acid batteries

A lead-acid battery is a row of **cells of about 2 V each**: six in series make
a 12 V battery. Each cell holds lead plates in sulfuric acid. As the battery
discharges, both plates turn to lead sulfate and the acid turns towards water;
charging reverses this
([TM 9-8000, pp. 12-1 to 12-5](../library/tm-9-8000-automotive-1985.html)).

Types you will meet:

| Type | What it is | Care |
| --- | --- | --- |
| Flooded ("wet") | Liquid acid, removable caps | Check level; top up with distilled water only ([NEETS 1, p. 2-27](../library/navedtra-neets.html)) |
| Sealed / maintenance-free | Flooded, but calcium plates lose little water | No topping up ([TM 9-8000, p. 12-8](../library/tm-9-8000-automotive-1985.html)) |
| AGM | Acid held in glass mat; valve-regulated | Sealed; any position; do not overcharge |
| Gel | Acid set as a gel; valve-regulated | Sealed; lower surge current; do not overcharge |

AGM and gel batteries are both "valve-regulated" (VRLA): they recombine most
of their gas inside and vent only when overcharged or overheated
([Wikipedia, "Lead–acid battery", "AGM", "Gelled electrolytes", "VRLA"](../library/wikipedia-en.html)).

**Starting and deep-cycle batteries are different.** A starting battery has
many thin plates for a big short burst; it survives fewer than about 100 deep
discharges. Deep-cycle batteries have thicker plates and survive hundreds to
thousands ([TM 9-8000, pp. 12-6 to 12-7](../library/tm-9-8000-automotive-1985.html)).
"Marine" or "leisure" batteries are a compromise between the two
([Wikipedia, "Lead–acid battery", "Deep-cycle batteries"](../library/wikipedia-en.html)).
Many boats keep a starting battery separate from the "house" bank, so that
running the lights flat never stops you starting the engine.

### How charged is it?

- **Hydrometer** (flooded only): the acid gets weaker as the battery
  discharges. Full is about 1.28 at 27 °C (80 °F)
  ([TM 9-8000, p. 12-3](../library/tm-9-8000-automotive-1985.html);
  [NEETS 1, pp. 2-25 to 2-27](../library/navedtra-neets.html)).
- **Voltage at rest**: a cell reads about 2.1 V when full and falls as it
  discharges ([Wikipedia, "Voltages for common usage"](../library/wikipedia-en.html)).
  For a 12 V battery rested for some hours, that is about 12.6 V full; around
  12.0 V or below it is nearly flat. A reading taken while charging or under
  load means little.

### Capacity

Capacity is in **ampere-hours** (Ah), usually at the 20-hour rate: a 100 Ah
battery gives 5 A for 20 hours. Drawn faster, it gives less
([NEETS 1, pp. 2-28 to 2-29](../library/navedtra-neets.html)). Cold cuts it
hard: at -18 °C (0 °F) a battery has only about 40 per cent of its warm
cranking capacity ([TM 9-8000, p. 12-6](../library/tm-9-8000-automotive-1985.html)).

### How they die

- **Left discharged.** Lead sulfate hardens into crystals ("sulfation") and
  the battery will no longer take a full charge
  ([TM 9-8000, p. 12-6](../library/tm-9-8000-automotive-1985.html);
  [Wikipedia, "Sulfation and desulfation"](../library/wikipedia-en.html)).
  Recharge fully, and soon, after every discharge.
- **Deep discharge again and again**, especially starting batteries.
- **Overcharging**: water is split into gas; flooded cells dry out, sealed ones
  vent and swell ([Wikipedia, "Safety"](../library/wikipedia-en.html)). A
  swollen battery must be isolated and replaced.
- **Old age**: plates shed material and grids corrode.

## Lithium iron phosphate (LiFePO4, LFP)

The lithium batteries fitted on boats are mostly lithium iron phosphate.
Each cell is 3.2 V nominal, so four in series give 12.8 V, close to a lead-acid
battery ([Wikipedia, "Lithium iron phosphate battery"](../library/wikipedia-en.html)).
They are much lighter for their capacity, last thousands of cycles, and can be
used deeper than lead-acid. LFP is more stable than other lithium chemistries,
but it can still catch fire if overcharged, overheated or crushed (same
article, "Safety").

What is different, and what matters for safety
([Wikipedia, "Lithium-ion battery", "Fire hazard", "Damaging and overloading", "Voltage limits"](../library/wikipedia-en.html);
["Lithium iron phosphate battery", "Viable alternative to lead-acid"](../library/wikipedia-en.html)):

- **A battery management system (BMS) is essential.** It disconnects the
  battery when a cell's voltage goes too high or too low, or when it is too
  hot or cold. Lithium packs without effective management are at risk of
  thermal runaway. When the BMS disconnects, the boat's power can vanish
  without warning: know how your system behaves.
- **Charging must suit lithium.** Charge voltages must not exceed about
  3.6 V per cell, and lead-acid habits such as equalising or a permanent
  trickle charge do harm.
- **Do not charge below 0 °C (32 °F).** Many lithium cells plate metal lithium
  on charging in the cold, which can make the pack unsafe.
- **Voltage tells you little about charge.** The voltage of an LFP cell is
  almost flat between about 20 and 80 per cent. Use the BMS or a battery
  monitor.
- **A lithium fire is hard to put out.** A cell in thermal runaway can stay
  above 500 °C, and its smoke is toxic and flammable. Get the crew out of the
  smoke and follow [Fire on board](../emergency/fire-on-board.html).

## Dangers with every battery

- **Hydrogen.** Charging lead-acid batteries gives off hydrogen and oxygen, an
  explosive mixture. No smoking, sparks or flames near charging batteries, and
  ventilate battery boxes
  ([NEETS 1, pp. 2-28 and 2-31](../library/navedtra-neets.html);
  [TM 9-8000, p. 12-10](../library/tm-9-8000-automotive-1985.html)). Connecting
  or disconnecting a lead to a gassing battery can make the spark that sets
  it off ([Wikipedia, "Lead–acid battery", "Safety"](../library/wikipedia-en.html)).
  Switch off the charger before touching the terminals.
- **Short circuits.** Never short the terminals
  ([NEETS 1, p. 2-28](../library/navedtra-neets.html)). A spanner across a
  battery can weld, burn the hand and start a fire. Cover the positive
  terminal.
- **Acid.** Wear eye protection. If acid gets on skin or in the eyes, flush with
  plenty of fresh water for at least 15 minutes, holding the eyelids open
  ([NEETS 1, p. 2-28](../library/navedtra-neets.html)). See
  [Burns](../health/burns.html).
- **Sea water.** Salt water on a damaged lead-acid battery makes **chlorine
  gas** ([TM 9-8000, p. 12-10](../library/tm-9-8000-automotive-1985.html)).
  Keep batteries high and dry, and get away from the fumes if the battery
  compartment floods.
- **Heavy and loose.** A battery that breaks free in a knockdown is a missile
  and a short circuit. Batteries must be firmly secured, protected from short
  circuit and kept away from heat
  ([MCA small fishing vessel code, 4.8.3.4 and 6.12.1](../library/mca-small-fishing-vessel-code-2024.html)).

## Battery switches and banks

A **battery switch** (isolator) cuts each battery or bank from the boat. The UK
code for small fishing vessels asks for a double-pole switch at each battery or
bank, with automatic bilge pumps wired before it so they keep working when the
boat is left ([MCA code, 4.8.3.5](../library/mca-small-fishing-vessel-code-2024.html)).

Batteries in **series** add their voltages (two 12 V make 24 V); in
**parallel** they add their capacity at the same voltage
([TM 9-8000, p. 12-10](../library/tm-9-8000-automotive-1985.html)). Only join
batteries of the same type, age and size.

When batteries do not charge, see
[Battery not charging](../fix-it/battery-not-charging.html). When the engine
will not crank, see [Engine won't turn over](../fix-it/engine-wont-crank.html).
