---
title: Diesel cooling systems
summary: Raw-water (open) and fresh-water (closed) cooling, keel coolers, thermostats, pumps and zincs, and what each part does when you are hunting an overheating fault.
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
    locator: "Ch. 8 'Engine Cooling Systems': purpose of cooling, too hot and too cold, pp. 147-148; 'The Open Cooling System' and 'The Closed Cooling System', keel cooler, pp. 148-149; pumps, p. 152; expansion tank and venting, p. 163; 'Sea Scoops and Strainers', 'Valves', thermostatic valves, pp. 163-165; ch. 9 fresh-water treatment, glycol antifreeze with its own inhibitors, pp. 175-176; ch. 12 cooling-water temperatures when no maker's figure is available, never add cold water to a hot engine, p. 249-250"
  - id: navpers-16178-fundamentals-of-diesel-engines
    locator: "Ch. 11, sec. 11-3 'Cooling systems': heat balance, purposes of cooling, fresh water as coolant, open system with sea water not satisfactory, pp. 74-76"
  - id: navpers-engineman-1957
    locator: "Engineman 3, ch. 11, 'Zincs', pp. 416-417; ch. 14, 'Care of zincs', pp. 500-501"
  - id: doe-hdbk-1018-mechanical-science
    locator: "Vol. 1, ME-01, 'Engine Cooling', p. 12; 'Engine Protection', water jacket temperature alarm, p. 39"
  - id: tm-5-278-outboard-motors-1944
    locator: "Sec. II, para. 4f 'Cooling System' (pump and pressure-vacuum cooling on outboards), pp. 9-10"
  - id: wikipedia-en
    locator: "'Outboard motor' (revision 2026-10), section 'Cooling system' (rubber-impeller pumps; impeller ruined if run dry)"
uncertain:
  - "Most small marine diesels use a raw-water pump with a flexible rubber impeller. The cleared Navy manuals describe bronze centrifugal pumps. That a rubber impeller is ruined by running dry is stated for outboards in Wikipedia ('Outboard motor', 'Cooling system'); the same pumps are used on small diesels, but no cleared source says so directly."
  - "On most small craft the raw water leaving the heat exchanger is sprayed into the exhaust to cool it (a 'wet exhaust'). The Navy manuals say only that sea water cools the exhaust piping and silencer before going overboard."
  - "Temperature figures given here are a 1979 Navy rule for engines with no maker's figure. Many small modern engines run their coolant hotter, under a pressure cap. Use your engine's manual."
---

## Why an engine needs cooling, and why not too much

About 30 per cent of the heat in the fuel must be carried away by the cooling
water ([Fundamentals of Diesel Engines, p. 74](../library/navpers-16178-fundamentals-of-diesel-engines.html)).
Without it, the oil film between moving parts breaks down, parts swell until
clearances close up, and hot metal loses strength. Cylinder heads crack and
pistons seize ([Engineman 3 & 2, pp. 147-148](../library/navedtra-engineman-3-2-1979.html)).

Too cold is also bad. A cold engine forms acid and sludge in its oil, and
corrosive gases condense on the cylinder walls. So the cooling system's job is
to hold the engine in a temperature *range*, not to make it as cold as
possible ([Engineman 3 & 2, p. 147](../library/navedtra-engineman-3-2-1979.html)).

## Raw-water (open) cooling

In an **open** or **raw-water** system, the engine-driven pump draws water from
the sea through a hull inlet, a seacock and a strainer, pushes it through the
engine's water jackets, and sends it overboard. On the way it often cools the
oil cooler and the exhaust
([Engineman 3 & 2, p. 148](../library/navedtra-engineman-3-2-1979.html)).

It is simple, but salt and scale build up in the engine passages, and weed and
dirt come in with the water. Scale blocks flow and also acts as insulation, so
an old raw-water-cooled engine may run hot even when the pump is fine. The Navy
called direct sea-water cooling "not satisfactory for the best engine
performance" ([Fundamentals of Diesel Engines, p. 75](../library/navpers-16178-fundamentals-of-diesel-engines.html);
[Engineman 3 & 2, p. 148](../library/navedtra-engineman-3-2-1979.html)).
Outboard motors and many older small engines are raw-water cooled. See
[How an outboard works](how-an-outboard-works.html).

## Fresh-water (closed, indirect) cooling

A **closed** system has two separate circuits
([Engineman 3 & 2, pp. 148-149](../library/navedtra-engineman-3-2-1979.html)):

- **The fresh-water circuit** works like a car's: a pump circulates fresh
  water (or water with antifreeze) round the engine, through a thermostat, and
  through a **heat exchanger**, then back to the pump. An **expansion tank** at
  the highest point lets the water expand and lets air escape.
- **The raw-water circuit** has its own pump. It draws sea water through the
  seacock and strainer, through the other side of the heat exchanger (and
  often the oil cooler), and sends it overboard.

The two waters never mix. The engine stays clean inside, and the thermostat can
hold a steady temperature.

A **keel cooler** is a closed system without a raw-water circuit. The fresh
water runs through pipes or a tank on the outside of the hull, below the
waterline, and the sea cools it directly
([Engineman 3 & 2, p. 149](../library/navedtra-engineman-3-2-1979.html)).
There is no raw-water pump, strainer or impeller to fail, but weed and fouling
on the cooler, or a boat sitting on mud, reduce cooling.

## The parts, and how they fail

| Part | What it does | Typical fault |
| --- | --- | --- |
| Hull inlet and seacock | Lets sea water in | Left shut; blocked by weed or a plastic bag |
| Strainer | Catches weed and debris | Clogged; lid not sealing, so the pump sucks air |
| Raw-water pump | Moves sea water | Worn or broken impeller; slipping or broken belt |
| Heat exchanger, oil cooler | Pass heat from coolant or oil to sea water | Tubes blocked by scale, weed or broken impeller vanes |
| Thermostat | Sends coolant round the heat exchanger only when warm | Stuck shut (overheats) or open (runs cold) |
| Expansion tank and cap | Room for expansion; lets air out | Low coolant, air lock, failed cap |
| Fresh-water pump and belt | Circulates coolant | Belt slipping or broken; seal leaking |
| Zincs (anodes) in the raw-water side | Corrode instead of the exchanger | Eaten away, so the exchanger corrodes |

A **thermostat** is a valve with a sealed element that expands when warm. While
the engine is cold the valve stays shut and the coolant bypasses the heat
exchanger. As the engine warms, the valve opens and sends more and more coolant
through the exchanger ([Engineman 3 & 2, pp. 164-165](../library/navedtra-engineman-3-2-1979.html)).

Centrifugal pumps need small clearances to work, and wear rings or seals are
fitted to keep them ([Engineman 3 & 2, p. 152](../library/navedtra-engineman-3-2-1979.html)).
Most small engines use a rubber-impeller pump instead; it is ruined if it
runs dry for long ([Wikipedia, "Outboard motor", "Cooling system"](../library/wikipedia-en.html)).
How to change the impeller is on
[Changing a raw-water pump impeller](../fix-it/changing-a-raw-water-impeller.html).

Air trapped in the fresh-water circuit forms pockets where the metal is not
cooled. That is why the circuit is vented at its high point and why the
coolant level can drop after you refill it
([Engineman 3 & 2, p. 163](../library/navedtra-engineman-3-2-1979.html)).

## Zincs

Sea water plus different metals makes a small battery, and one metal is eaten
away. Zinc plugs or plates in the raw-water side of coolers are made to be
eaten first, so the cooler is spared. They must be clean and in good metal
contact to work. The Navy inspected them at least once a month
([Engineman 3, pp. 416-417 and 500-501](../library/navpers-engineman-1957.html)).
See [Corrosion and anodes](corrosion-and-anodes.html).

**Before you open the sea-water side of any cooler, close the seacock.**
Otherwise the boat can flood
([Engineman 3, p. 501](../library/navpers-engineman-1957.html)).

## Antifreeze and coolant

Where freezing is possible, the fresh-water circuit uses a glycol-based
antifreeze. Proper antifreeze contains its own corrosion inhibitors
([Engineman 3 & 2, pp. 175-176](../library/navedtra-engineman-3-2-1979.html)).
Drain and flush when you change from one kind of treatment to another so they
do not mix. Laying up for winter is covered in
[Laying up an engine for winter](winterising-an-engine.html).

## Temperatures

Your engine's manual gives its normal temperature. Where no maker's figure was
available, the 1979 Navy rule was fresh water leaving the engine between 60 and
77 °C (140 and 170 °F), and sea water leaving the system no hotter than about
54 °C (130 °F), because hotter sea water deposits salt
([Engineman 3 & 2, p. 249](../library/navedtra-engineman-3-2-1979.html)).
Watch the gauge in normal running so you know what is normal for *your*
engine. A high-temperature alarm is an early warning: keep running at that
temperature and the engine will be damaged
([DOE, vol. 1, p. 39](../library/doe-hdbk-1018-mechanical-science.html)).

If an engine has overheated, **never add cold water until it has cooled**. A
sudden rush of cold water into a hot engine can crack a liner or head, or seize
a piston ([Engineman 3 & 2, p. 250](../library/navedtra-engineman-3-2-1979.html)).

## Diagnosing

- Little or no water at the exhaust: raw-water side (seacock, strainer, pump,
  impeller, blocked inlet).
- Good water at the exhaust but the engine still hot: fresh-water side
  (coolant level, thermostat, belt, blocked heat exchanger) or the engine is
  overloaded.
- Runs cool and never warms up: thermostat stuck open.

Step-by-step checks: [Engine overheating](../fix-it/engine-overheating.html).
For outboards: [Outboard: no cooling-water stream](../fix-it/outboard-no-cooling-water.html).
For seacocks: [Through-hulls and seacocks](through-hulls-and-seacocks.html).
