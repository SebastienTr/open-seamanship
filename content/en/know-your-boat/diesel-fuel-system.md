---
title: The diesel fuel system
summary: The path diesel takes from tank to injector, the low-pressure and high-pressure sides, why air and water stop the engine, and where to look first.
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
    locator: "Ch. 10 'Fuel and Fuel Systems': sediment and water in fuel, p. 205; diesel fuel oil requirements, p. 207; 'External fuel system' (tank vented at a high point, lines above atmospheric pressure, transfer pump, strainer and filter, return to tank, 'water in the fuel oil will probably cause the injection system to fail', drain filter sumps), pp. 213-215; 'Fuel injection system' types, p. 215; hand priming pump for bleeding, p. 223; 'Purging the diesel engine fuel injection system' (air bubbles, suction-side leaks, running out of fuel), pp. 236-237; ch. 12, check the service tank for water through the bottom drain, p. 250"
  - id: doe-hdbk-1018-mechanical-science
    locator: "Vol. 1, ME-01, 'Fuel System' (injectors need very clean fuel, filters outside and inside the engine, fuel cools the injectors, excess returned to the tank), p. 14; 'Fuel Injectors', pp. 30-33; 'Governor', p. 34"
  - id: navpers-16178-fundamentals-of-diesel-engines
    locator: "Ch. 11, sec. 11-1 'Fuel system' (day tank vented at a high point, avoid foaming, drain the sumps of filters and strainers), pp. 71-72"
  - id: tm-9-8000-automotive-1985
    locator: "Ch. 5, sec. VII 'Cold Weather Starting Aids', para. 5-31 (diesels hard to start in cold weather), p. 5-35"
uncertain:
  - "Most small marine diesels today use a rotary or in-line injection pump, and new engines use electronic common-rail injection with fuel at very high pressure. The cleared sources describe older mechanical systems. Do not open a high-pressure pipe on a common-rail engine while it runs; follow the maker's procedure."
  - "Diesel thickens and forms wax crystals in cold weather, which can block filters. No cleared source in this pack gives figures; check what your fuel supplier says for winter grade."
  - "The behaviour of a blocked tank vent, sloshing fuel in a low tank and sludge stirred up by rough water is common experience on small boats; the cleared sources state only that tanks must be vented, that air must not be drawn in, and that running out of fuel lets air into the system."
  - "Many diesel fuels in Europe now contain biodiesel (FAME), which holds more water and may encourage microbial growth ('diesel bug'). The cleared sources predate this. See the fuel contamination page and treat it as a reason for extra care, not a known figure."
---

## The path of the fuel

Fuel on a small boat diesel travels this way:

1. **Tank**, with a **vent** to let air in as fuel is used, and a filler.
2. **Shut-off valve** at the tank.
3. **Primary filter / water separator**, usually with a clear bowl and a drain
   at the bottom.
4. **Lift pump** (also called the transfer or feed pump), driven by the engine
   or electric, often with a hand-priming lever.
5. **Secondary (fine) filter** on the engine.
6. **Injection pump**, which raises the pressure and meters the fuel.
7. **High-pressure pipes** to the **injectors**, which spray the fuel into the
   cylinders.
8. **Return line** taking surplus fuel back to the tank.

The Navy described the same chain: fuel is drawn by an engine-driven pump
through a strainer and a replaceable filter to the injection pumps, and the
excess goes back to the tank
([Engineman 3 & 2, pp. 213-214](../library/navedtra-engineman-3-2-1979.html)).

More fuel flows round the system than the engine burns. The surplus cools the
injectors and is sent back to the tank
([DOE Mechanical Science, vol. 1, p. 14](../library/doe-hdbk-1018-mechanical-science.html)).
That is why a leak in the return line, or a blocked return, also causes
trouble.

## Two sides: suction and pressure

The parts from the tank to the lift pump work **under suction**: the pressure
in the pipe is lower than the air outside. Anything after the injection pump is
under very high pressure.

This matters for faults:

- **On the suction side, a leak lets air in, not fuel out.** You may not see a
  drip at all. The smallest hole in the suction piping "will allow enough air
  to flow into the system to air bind the high-pressure pumps". Look at every
  fitting, washer and filter seal, and at copper pipe cracked by vibration
  ([Engineman 3 & 2, p. 237](../library/navedtra-engineman-3-2-1979.html)).
- **On the pressure side, a leak sprays fuel.** Keep hands and face away from a
  leaking high-pressure pipe while the engine runs.

## Why air stops a diesel

The injection pump moves a tiny, exact amount of fuel at each stroke. If air is
in the pump or pipes, the pump squeezes the bubble and the injector never
opens. The engine misfires, stops, or turns over without starting
([Engineman 3 & 2, p. 236](../library/navedtra-engineman-3-2-1979.html)).

Air gets in when:

- the tank runs dry ([Engineman 3 & 2, p. 237](../library/navedtra-engineman-3-2-1979.html));
  in a seaway a nearly empty tank can do the same as the fuel sloshes away
  from the pick-up;
- a filter has been changed and not bled;
- a joint on the suction side is loose.

Cloudy fuel at a bleed screw means small air bubbles
([Engineman 3 & 2, p. 236](../library/navedtra-engineman-3-2-1979.html)).
Removing the air is called **bleeding**. Work point by point in the direction
the fuel flows (after the lift pump, after each filter, then at the injection
pump), working the hand-priming pump until only clear fuel comes out at each
point. Try to start the engine before you bleed the high-pressure pipes
([Engineman 3 & 2, pp. 223 and 237](../library/navedtra-engineman-3-2-1979.html)).
Full steps: [Bleeding air from a diesel fuel system](../fix-it/bleeding-a-diesel.html).

## Why fuel must be clean and dry

Injectors and injection pumps are built to very fine clearances with very small
holes ([DOE, vol. 1, p. 14](../library/doe-hdbk-1018-mechanical-science.html)).
Sediment and water cause wear, gumming and corrosion, and make the engine run
unevenly and lose power
([Engineman 3 & 2, p. 205](../library/navedtra-engineman-3-2-1979.html)).
Water in the fuel "will probably cause the injection system to fail"
([Engineman 3 & 2, p. 214](../library/navedtra-engineman-3-2-1979.html)).

Water is heavier than diesel, so it sinks to the bottom of the tank and of each
filter bowl. That is why:

- you drain the bowl of the primary filter and look at what comes out; and
- you sample from the bottom of the tank, if it has a drain, to check for water
  and sludge ([Engineman 3 & 2, p. 250](../library/navedtra-engineman-3-2-1979.html);
  [Fundamentals of Diesel Engines, p. 72](../library/navpers-16178-fundamentals-of-diesel-engines.html)).

Water in the tank comes from condensation, from a leaking filler or deck
fitting, or with bad fuel. Rough water stirs up sludge from the tank bottom, so
a blocked filter may show up in the first rough passage after a calm spell.
See [Water or bug in the diesel](../fix-it/fuel-contamination.html).

## The vent

The tank vent lets air in as fuel is drawn out. Navy practice was to vent the
supply tank at a high point and to keep fuel from foaming or splashing, so that
air does not get mixed into it
([Fundamentals of Diesel Engines, p. 71](../library/navpers-16178-fundamentals-of-diesel-engines.html)).
A blocked vent (by a wasp's nest, salt or a kinked hose) makes a vacuum in the
tank. The engine starts, runs a while, then loses power and stops as the lift
pump can no longer draw fuel. Open the filler cap: if you hear air rush in and
the engine recovers, you have found it.

## Injection and the governor

Injection systems come in several types: an injection pump feeding a pipe to
each injector, a distributor (rotary) pump, unit injectors, and common rail
([Engineman 3 & 2, p. 215](../library/navedtra-engineman-3-2-1979.html)). In
each case, the governor sets how much fuel each stroke delivers, and so the
engine speed ([DOE, vol. 1, p. 34](../library/doe-hdbk-1018-mechanical-science.html)).
A fuel supply that is partly blocked can make the engine run well at idle but
lose power or hunt under load: see
[Engine speed hunting or surging](../fix-it/diesel-hunting-or-surging.html) and
[Engine stops or loses power](../fix-it/engine-stops-or-loses-power.html).

Injectors are precision parts. Leaking or dribbling injectors cause smoke,
carbon and loss of power; testing them needs a special tester
([Engineman 3 & 2, p. 236](../library/navedtra-engineman-3-2-1979.html)). See
[Exhaust smoke](../fix-it/exhaust-smoke.html).

## Cold weather

Diesels are hard to start in the cold, mainly because cold fuel does not
vaporise easily ([TM 9-8000, para. 5-31](../library/tm-9-8000-automotive-1985.html)).
Cold-starting aids heat the intake air. See
[How a diesel engine works](how-a-diesel-engine-works.html).

## First checks when the fuel side is suspected

1. Is there fuel in the tank, and is the tank valve open?
2. Is the vent clear?
3. Is there water or dirt in the primary filter bowl?
4. Has a filter just been changed? Bleed the system.
5. Any wet, loose or weeping joints on the suction side?

Then follow [Engine turns over but won't start](../fix-it/engine-wont-start.html)
or [Engine stops or loses power](../fix-it/engine-stops-or-loses-power.html).
Filter changes are part of the [Engine maintenance routine](engine-maintenance.html).
