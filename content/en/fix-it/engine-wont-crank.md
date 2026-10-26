---
title: Engine won't turn over
summary: You press the start button and the diesel does not turn, turns very slowly, or the starter whirs without turning the engine.
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
    locator: "Ch. 13 'Troubleshooting': 'Engine fails to start' and 'Engine cannot be cranked nor barred over', pp. 261-262; 'Engine cannot be cranked but can be barred over', p. 263; 'Electric start malfunctions', p. 265; 'Insufficient cranking speed', p. 270; 'Obstruction in the exhaust system', pp. 272-273"
  - id: tm-9-2815-252-24-dn2m
    locator: "Table 3-2 'Troubleshooting', malfunctions 1 and 2, p. 3-3; para 3-3.1 'General instructions' (disconnect batteries before work), p. 3-11"
  - id: tm-9-2815-254-24-isuzu-c240
    locator: "Table 3-2 'Troubleshooting', malfunctions 1 and 2, p. 3-4"
  - id: navpers-engineman-1957
    locator: "Engineman 3 (NAVPERS 10539), ch. 13 'Engine operating procedures, general': starting after routine securing, steps 8-10, p. 451; starting in cold weather, p. 453; stopping and securing, step 3 (indicator cocks left open to show water in cylinders), p. 470"
  - id: wikipedia-en
    locator: "'Hydrolock', sections 'Symptoms and damage' and 'Causes and special cases: Marine' and 'Diesel engines'"
uncertain:
  - "No cleared source gives battery voltages for a small boat. This page does not give any: use a meter and the figures in the battery or engine manual."
  - "Closing the raw-water seacock during long cranking, and opening it again as soon as the engine fires, is common small-boat practice to stop the exhaust filling with water. The sources explain why water builds up (Wikipedia, 'Hydrolock') but none gives this step. A reviewer should confirm it."
  - "Some small diesels have decompression levers that make turning by hand easier. Whether yours has them, and how to use them, is in your engine's manual only."
---

## Situation

You turn the key or press the start button and the engine does not turn at
all, turns very slowly, or the starter spins and whines without turning the
engine. This page is about *cranking*. If the engine turns over at normal speed
but will not fire, go to [Engine turns over but won't start](engine-wont-start.html).

If you are near rocks or a lee shore, deal with the boat first: anchor, sail
or call for help. See [Engine failure near danger](../emergency/engine-failure-near-danger.html).

## Do now

1. **Stop pressing the button.** Repeated cranking can flatten the battery and,
   on a boat with a wet exhaust, can fill the exhaust with water (see step 6).
2. **Check the simple things.** Battery isolator switch on? Engine stop control
   pushed fully home (run position)? Gear lever where your engine needs it to
   start? Navy manuals put "failure to follow instructions" near the top of
   every list ([Engineman 3 & 2, pp. 263 and 266](../library/navedtra-engineman-3-2-1979.html)).
3. **Listen, and match what you hear:**
   - *Nothing at all, or a single click:* an electrical fault. Go to step 4.
   - *Starter whirs or whines, engine does not turn:* the starter pinion is not
     engaging the flywheel. Go to step 5.
   - *Starter tries, engine turns a little and stops hard, or turns very
     slowly:* go to step 5 and step 6.
4. **Electrical (nothing happens).** The usual causes are a broken or corroded
   connection, a flat battery, or a failed solenoid or starter
   ([Engineman 3 & 2, p. 265](../library/navedtra-engineman-3-2-1979.html)).
   - Check both battery terminals and the engine earth (ground) strap: clean,
     tight, not hot after a start attempt.
   - Check the battery with a meter. A starter needs much more current than
     anything else on board, so a battery that runs the lights can still be
     too weak to crank.
   - If you hear the solenoid click but the starter does not turn, the fault is
     the heavy cable, the solenoid contacts or the starter motor
     ([TM 9-2815-252-24, table 3-2, malfunction 1](../library/tm-9-2815-252-24-dn2m.html)).
   - See [Finding a 12 V electrical fault](electrical-fault-finding.html) and
     [Batteries](../know-your-boat/batteries.html).
5. **Starter whirs but the engine does not turn.** Dirt or corrosion can stop
   the pinion moving out, or the pinion or flywheel ring gear teeth are worn or
   broken ([Engineman 3 & 2, p. 265](../library/navedtra-engineman-3-2-1979.html);
   [TM 9-2815-254-24, malfunction 2](../library/tm-9-2815-254-24-isuzu-c240.html)).
   This usually needs the starter removed. Do not keep trying: it chews the
   teeth further.
6. **Try to turn the engine by hand.** Switch off the battery isolator first,
   so nobody can start it on you
   ([TM 9-2815-252-24, p. 3-11](../library/tm-9-2815-252-24-dn2m.html)).
   Turn the crankshaft with a spanner on the
   crankshaft pulley nut, in the normal direction of rotation.
   - *It turns freely over several revolutions:* the engine is free. The
     problem is electrical or the starter.
   - *It stops hard at the same point and will not go past:* suspect water or
     oil in a cylinder (hydraulic lock) or a seized part. Do not force it with
     the starter.

## Why

A diesel must be turned fast enough to make its air hot by compression.
Slow cranking, from a weak battery or from thick cold oil, may never get it hot
enough to fire ([Engineman 3 & 2, p. 270](../library/navedtra-engineman-3-2-1979.html)).

Water is the danger on boats. On an engine whose cooling water is mixed into
the exhaust, long cranking without the engine firing lets the raw-water pump
fill the exhaust until water runs back into the cylinders. Water does not
compress. A diesel needs very little water to lock, and the starter can be
burned out or a connecting rod bent
([Wikipedia, "Hydrolock"](../library/wikipedia-en.html)). The Navy manual
gives a badly fitted silencer, or an engine below its exhaust outlet, as a way
for water to back up into the engine
([Engineman 3 & 2, pp. 272-273](../library/navedtra-engineman-3-2-1979.html)).

## Check that it worked

- With the electrical fault fixed, the starter spins the engine briskly and
  evenly, with the regular "chuff" of each compression stroke.
- When turning by hand, every cylinder comes up on compression and goes over.
- No water comes out of the injector or glow-plug holes when you turn it.

## If that fails

- **Hydraulic lock on a small diesel.** Large engines have test cocks on each
  cylinder, opened before turning the engine over
  ([Engineman 3, p. 451](../library/navpers-engineman-1957.html);
  [Engineman 3 & 2, p. 261](../library/navedtra-engineman-3-2-1979.html)).
  Small engines do not. The usual way is to remove the injectors or glow plugs
  and turn the engine by hand to push the water out
  ([Wikipedia, "Hydrolock"](../library/wikipedia-en.html)). Then find out where
  the water came from (exhaust, a leaking exhaust elbow, a head gasket) before
  you run it. Salt water left in a cylinder rusts it quickly: change the oil if
  it looks milky, see [Low oil pressure alarm](low-oil-pressure.html).
- **Engine seized and no water found.** A seized piston or a tight bearing
  needs a mechanic ([Engineman 3 & 2, pp. 261-262](../library/navedtra-engineman-3-2-1979.html);
  [TM 9-2815-254-24, malfunction 2, step 2](../library/tm-9-2815-254-24-isuzu-c240.html)).
- **Large engines with air starting.** Check that the jacking (turning) gear is
  disengaged, the air valve is open and the air receiver has pressure
  ([Engineman 3 & 2, pp. 263-265](../library/navedtra-engineman-3-2-1979.html)).
- **Cold weather.** Thick oil slows cranking; see the cold-start notes in
  [Engine turns over but won't start](engine-wont-start.html).
- If you cannot fix it, plan to sail, anchor or arrange a [tow](../run-the-boat/towing.html).
