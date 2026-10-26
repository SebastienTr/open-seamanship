---
title: How a diesel engine works
summary: What a marine diesel needs to run (air, compression heat, clean fuel at the right moment, oil and cooling), and how each need explains the common faults.
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
  - id: doe-hdbk-1018-mechanical-science
    locator: "Vol. 1, module ME-01 'Diesel Engine Fundamentals': 'Diesel Engines', compression ratio and speed control, pp. 2-3; 'Diesel Engine Support Systems' (cooling, lubrication, fuel, air intake, exhaust), pp. 12-16; 'The Four-Stroke Cycle' and 'The Two-Stroke Cycle', pp. 22-26; 'Governor', p. 34; 'Engine Protection', pp. 38-40"
  - id: navpers-16178-fundamentals-of-diesel-engines
    locator: "Ch. 11 'Engine Systems', sec. 11-3 'Cooling systems' (heat balance: about one third to work, 30 per cent to exhaust, 30 per cent to cooling water), p. 74"
  - id: navedtra-engineman-3-2-1979
    locator: "Ch. 10 'Fuel and Fuel Systems', 'Diesel Fuel Oil' (clean fuel, ignition delay, phases of combustion, diesel knock), pp. 207-208; 'Purging the diesel engine fuel injection system', pp. 236-237; ch. 12 'Diesel Engine Operating Procedures', oil pressure after starting and loading a cold engine, pp. 247-248"
  - id: tm-9-8000-automotive-1985
    locator: "Ch. 5, sec. VII 'Cold Weather Starting Aids', para. 5-31, p. 5-35; glossary, 'Glow Plug'"
uncertain:
  - "Timing, pressure and temperature figures on this page come from a worked example in a US Department of Energy handbook (a 16:1 engine). They show the idea; your engine's figures are in its own manual."
  - "Most small yacht and workboat diesels today have electronic or rotary injection pumps and, on newer engines, common-rail injection. The open sources describe older mechanical systems. The principles are the same; the parts and the checks may differ."
---

## The short version

A diesel engine burns fuel inside its cylinders and turns the push of the hot
gas into rotation. It has no spark plugs. It squeezes air so hard that the air
gets hot enough to light the fuel when the fuel is sprayed in
([DOE Mechanical Science, vol. 1, p. 3](../library/doe-hdbk-1018-mechanical-science.html)).

So a diesel needs five things, and nearly every fault is one of them missing:

| The engine needs | If it is missing you see | Go to |
| --- | --- | --- |
| Air, clean and enough of it | Black smoke, loss of power | [Exhaust smoke](../fix-it/exhaust-smoke.html) |
| Compression (hot air) | Hard starting, white smoke when cold | [Engine turns over but won't start](../fix-it/engine-wont-start.html) |
| Clean fuel, free of air and water, sprayed at the right moment | Will not start, stops, hunts, misfires | [Bleeding air from a diesel](../fix-it/bleeding-a-diesel.html), [Water or bug in the diesel](../fix-it/fuel-contamination.html) |
| Oil between moving parts | Low oil pressure alarm, then seizure | [Low oil pressure alarm](../fix-it/low-oil-pressure.html) |
| Cooling | High temperature alarm, steam | [Engine overheating](../fix-it/engine-overheating.html) |

To turn over in the first place, the starter motor also needs a charged
battery: see [Engine won't turn over](../fix-it/engine-wont-crank.html).

## Compression: why a diesel needs no spark

The **compression ratio** compares the space in the cylinder with the piston at
the bottom of its stroke to the space left with the piston at the top. Petrol
(gasoline) engines run at less than about 10:1. Diesels run at about 14:1 to
24:1. This is possible because the diesel squeezes only air; the fuel comes in
later ([DOE, vol. 1, p. 3](../library/doe-hdbk-1018-mechanical-science.html)).

In the handbook's worked example of a 16:1 engine, air that enters at about
27 °C (80 °F) reaches roughly 690 °C (1280 °F) by the top of the stroke, at a
pressure of about 50 bar (740 psi) in theory. A real engine reaches a little
less, because heat leaks into the cold metal around it
([DOE, vol. 1, pp. 23-24](../library/doe-hdbk-1018-mechanical-science.html)).

That last point explains cold starting. In a cold engine, or one with worn
rings or leaking valves, the air loses heat or pressure before the fuel
arrives, and the fuel does not light. This is why glow plugs or other cold
starting aids exist: glow plugs, or heaters that warm the intake air
([TM 9-8000, para. 5-31 and glossary](../library/tm-9-8000-automotive-1985.html)).
It is also why low compression shows up first as hard starting on a cold
morning.

## The four-stroke cycle

Most small marine diesels are four-stroke engines. Every engine must do four
things: take in air, compress it, burn fuel to push the piston, and push the
exhaust out. A four-stroke engine gives each its own stroke, so one cycle
takes two turns of the crankshaft. The camshaft, which opens the valves, turns
at half crankshaft speed
([DOE, vol. 1, pp. 21-22](../library/doe-hdbk-1018-mechanical-science.html)).

1. **Intake.** The inlet valve opens and the falling piston draws in air.
2. **Compression.** Both valves close and the rising piston squeezes the air.
3. **Power.** Near the top of the stroke the injector sprays fuel. It burns and
   the hot gas drives the piston down.
4. **Exhaust.** The exhaust valve opens and the rising piston pushes the burnt
   gas out.

In the example engine, fuel injection starts about 28° of crankshaft rotation
before the top of the stroke. The timing must be right so that the burning
gas pushes on the piston neither too early nor too late
([DOE, vol. 1, p. 24](../library/doe-hdbk-1018-mechanical-science.html)).

A two-stroke diesel does all four jobs in one turn of the crankshaft, using
ports in the cylinder wall and a blower to push fresh air in. Some older
workboat engines are two-strokes
([DOE, vol. 1, pp. 25-26](../library/doe-hdbk-1018-mechanical-science.html)).

## Burning the fuel

The fuel does not light the instant it enters. Each droplet first cools the air
around it as it turns to vapour, then heats up until it ignites. This short
**ignition delay** is normal. If the delay is too long, as in a cold engine or
with poor fuel, too much fuel collects before it lights, and it all burns at
once: a hard knock
([Engineman 3 & 2, pp. 207-208](../library/navedtra-engineman-3-2-1979.html)).
Some knock is normal in a diesel, especially at light load and when cold. A new
or changed knock is not: see
[Knocking, vibration or unusual noise](../fix-it/engine-knocking-or-vibration.html).

Injectors have very fine holes and tight fits, so the fuel must be very clean
([DOE, vol. 1, p. 14](../library/doe-hdbk-1018-mechanical-science.html)).
Air in the high-pressure part of the system is just as bad: the pump squeezes
the bubble instead of opening the injector, and the engine misfires, stops or
will not start ([Engineman 3 & 2, pp. 236-237](../library/navedtra-engineman-3-2-1979.html)).
The [fuel system page](diesel-fuel-system.html) explains the path the fuel
takes.

## Speed control: the governor

A petrol engine controls power by throttling the air. A diesel always takes in
a full charge of air, and its speed depends only on how much fuel is injected.
Left alone it would race, so every diesel has a **governor** that adjusts the
fuel to hold the speed you set with the throttle lever
([DOE, vol. 1, pp. 3 and 34](../library/doe-hdbk-1018-mechanical-science.html)).
A sticking governor or fuel control, or a fuel supply that comes and goes,
makes the engine speed rise and fall: see
[Engine speed hunting or surging](../fix-it/diesel-hunting-or-surging.html).

## Where the heat goes

Only about a third of the heat in the fuel becomes useful work. About
30 per cent goes out with the exhaust and about 30 per cent into the cooling
water ([Fundamentals of Diesel Engines, p. 74](../library/navpers-16178-fundamentals-of-diesel-engines.html)).
So the cooling system carries away nearly as much energy as the propeller
gets. When it fails, temperatures climb within minutes. See
[Diesel cooling systems](diesel-cooling-systems.html).

## Oil

Every moving part rides on a thin film of oil. The oil also carries heat away
from the bearings. A pump draws oil from the sump through a filter and sends it
to the bearings; a relief valve limits the pressure
([DOE, vol. 1, pp. 13-14](../library/doe-hdbk-1018-mechanical-science.html)).
Loss of oil pressure "can destroy an engine in short order"
([DOE, vol. 1, p. 39](../library/doe-hdbk-1018-mechanical-science.html)).
After starting, oil pressure should rise at once. If it does not, stop the
engine and find out why
([Engineman 3 & 2, p. 248](../library/navedtra-engineman-3-2-1979.html)).

## The alarms on your panel

Larger engines carry alarms or shutdowns for overspeed, high coolant
temperature, high exhaust temperature, low oil pressure and high crankcase
pressure ([DOE, vol. 1, pp. 38-40](../library/doe-hdbk-1018-mechanical-science.html)).
Small marine engines usually have at least the oil pressure and temperature
alarms. Treat each as a request to slow down and look, not as noise.

## Looking after it

Warm the engine up before you load it: loading a cold engine causes carbon,
wear and fuel in the oil
([Engineman 3 & 2, p. 248](../library/navedtra-engineman-3-2-1979.html)).
The routine checks are on [Engine maintenance routine](engine-maintenance.html).
For the history of the engine, see [The marine diesel engine](../history/the-marine-diesel.html).
