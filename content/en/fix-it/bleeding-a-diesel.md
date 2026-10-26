---
title: Bleeding air from a diesel fuel system
summary: How to get air out of a diesel fuel system after running out of fuel or changing a filter, working from the tank towards the injectors.
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
    locator: "Ch. 6 'Fuel injection equipment': fuel spray can pierce skin, p. 237; 'Bleeding air out of fuel system', pp. 241-243"
  - id: navedtra-engineman-3-2-1979
    locator: "Ch. 13 'Troubleshooting', 'Foreign matter in the fuel oil system' (air in the fuel, airbound pump, cloudy-fuel test), p. 266"
  - id: tm-9-2815-252-24-dn2m
    locator: "Para 3-11 'General' (fuel system precautions), p. 3-20; para 3-12 'Bleeding and priming fuel system', p. 3-21"
  - id: tm-9-2815-254-24-isuzu-c240
    locator: "Para 3-10.6 warning (keep body clear of injector spray), p. 3-29; para 3-12 'Bleeding and priming fuel system', p. 3-65"
  - id: navedtra-construction-mechanic-3-2-1978
    locator: "Ch. 4 'Fuel systems', 'Air in fuel system', p. 120"
  - id: fm-4-01-502-watercraft-safety
    locator: "Ch. 3, para 3-51 'Prevention', principle 5 (stop oil leaks at once, wipe up spills), p. 3-10"
uncertain:
  - "Bleed screw positions, the type of lift pump and whether the injection pump has its own bleed screw differ from engine to engine. The two Army engines shown here are examples, not your engine. Use the diagram in your engine's manual."
  - "Some modern engines bleed themselves with an electric lift pump. Follow the maker's method if yours does."
  - "The tip about a 'dead' priming lever (the engine cam holding the lift-pump arm) is common practice on small diesels with a mechanical lift pump; no cleared source states it."
  - "Tightening torques for bleed screws and injector pipe nuts are in your manual. Do not over-tighten small bleed screws: they strip easily."
---

## Situation

The engine ran out of fuel, a filter was just changed, a fuel pipe was opened,
or fuel at the filter bleed screw looks cloudy or frothy. Air in a diesel fuel
system stops it starting, or makes it miss, knock and stall
([Engineman 2, p. 241](../library/navpers-engineman-2-1957.html)).

**Safety.** Diesel spray from an injector or a high-pressure pipe can be
driven through your skin and cause blood poisoning. Keep hands and face out of
the line of any spray ([Engineman 2, p. 237](../library/navpers-engineman-2-1957.html);
[TM 9-2815-254-24, p. 3-29](../library/tm-9-2815-254-24-isuzu-c240.html)).
Have rags and a container ready. Wipe spilt fuel off the engine, especially
near the exhaust, before you start it
([TM 9-2815-252-24, para 3-11](../library/tm-9-2815-252-24-dn2m.html);
[FM 4-01.502, para 3-51](../library/fm-4-01-502-watercraft-safety.html)).

## Do now

The rule is: **remove air step by step, starting at the tank end and working
towards the injectors** ([Engineman 2, p. 242](../library/navpers-engineman-2-1957.html)).

1. **Fix the cause first.** Fill the tank. Open the fuel valve. Tighten any
   loose fitting on the suction side. Even a tiny hole on the suction side lets
   air in ([Engineman 2, p. 241](../library/navpers-engineman-2-1957.html)).
2. **Fill the filters if you can.** After a filter change, filling the new
   filter with clean fuel saves a lot of pumping. If a filter has a filling
   plug on top, you can pour clean fuel in until the air is gone
   ([Engineman 2, p. 242](../library/navpers-engineman-2-1957.html)).
3. **Primary filter (water separator).** Open its bleed screw one or two turns.
   Work the hand-priming lever or pump on the lift pump until fuel comes out
   with no bubbles. Close the screw while fuel is still flowing.
   *If the lever feels dead, the engine cam may be holding the pump arm: turn
   the engine round a little by hand and try again.*
4. **Secondary (fine) filter on the engine.** Do the same at its bleed screw
   ([TM 9-2815-252-24, para 3-12 a](../library/tm-9-2815-252-24-dn2m.html)).
5. **Injection pump.** If your pump has a bleed screw, open it and pump until
   clear fuel flows, then close it
   ([TM 9-2815-254-24, para 3-12](../library/tm-9-2815-254-24-isuzu-c240.html)).
   On small engines this is often all that is needed
   ([Engineman 2, p. 242](../library/navpers-engineman-2-1957.html)).
6. **Try to start.** Set the controls as your manual says for starting, and crank. If it fires,
   let it run and watch for misses. Do not crank longer than your manual says
   ([Engineman 2, p. 242](../library/navpers-engineman-2-1957.html)).
   On a wet-exhaust boat, see the warning about water in
   [Engine turns over but won't start](engine-wont-start.html).
7. **Only if it still will not start: injector pipes.** Slacken the pipe nut
   at each injector (or at the pump outlet) slightly, holding the fitting with
   a second spanner. Crank until fuel without bubbles comes from the nut, then
   tighten it
   ([TM 9-2815-252-24, para 3-12 b-e](../library/tm-9-2815-252-24-dn2m.html);
   [Engineman 2, pp. 242-243](../library/navpers-engineman-2-1957.html)).

## Why

Liquid fuel cannot be compressed, so the injection pump can build pressure to
open the injector. Air squashes instead. A pump full of air just compresses and
expands it, and no fuel reaches the cylinder: the pump is "airbound"
([Engineman 3 & 2, p. 266](../library/navedtra-engineman-3-2-1979.html)).
Air gets in from loose joints, from cracked pipes, through an injector that
does not close properly, or when the tank runs dry
([Construction Mechanic 3 & 2, p. 120](../library/navedtra-construction-mechanic-3-2-1978.html)).

## Check that it worked

- Fuel from each bleed point comes out solid, with no bubbles, and the filter
  bowl stays clear.
- The engine starts and runs evenly, without misses, at idle and under load.
- No fuel is weeping from any screw or nut you touched.

## If that fails

- **Air keeps coming back.** There is a leak on the suction side: a filter
  bowl seal, a hose clip, a cracked pipe, or a sealing washer. Air in means
  the pressure there is below atmospheric, so fuel does not drip out to show
  you where ([Engineman 2, p. 241](../library/navpers-engineman-2-1957.html)).
  Check every joint between tank and lift pump.
- **No fuel reaches the first bleed screw.** Blocked tank pickup, closed valve,
  blocked primary filter, or a failed lift pump: see
  [Water or bug in the diesel](fuel-contamination.html).
- **Larger engines.** With a hand-operated transfer pump, open the line at
  each stage in turn (pump to strainers, strainers to filters, filters to
  injection pumps, then the overflow on the injection-pump housing) and pump
  until clear fuel flows before closing it. Prime the high-pressure lines only
  if the engine still will not start, following the maker's book
  ([Engineman 2, pp. 242-243](../library/navpers-engineman-2-1957.html)).
- **Clear fuel everywhere but no start.** Go back to
  [Engine turns over but won't start](engine-wont-start.html).

Background: [The diesel fuel system](../know-your-boat/diesel-fuel-system.html).
