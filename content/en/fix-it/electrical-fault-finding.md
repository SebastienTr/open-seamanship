---
title: Finding a 12 V electrical fault
summary: A light, pump, instrument or radio has stopped working, or a fuse keeps blowing. A step-by-step way to find the fault with a multimeter on a 12 V (or 24 V) boat system.
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
  - id: navedtra-neets
    locator: "Module 1 (NAVEDTRA 14173A), chapter 3, sections 3.7.2 (open circuit) and 3.7.3 (short circuit), pp. 3-61 to 3-62; chapter 2, section 2.4.3.4 (safety precautions with batteries), p. 2-28. Module 3 (NAVEDTRA 14175A), chapter 2, sections 2.3.1.5.1.3 to 2.3.1.6.2 (checking and replacing fuses, corroded fuseholders), pp. 2-25 to 2-28. Module 16 (NAVEDTRA 14188A), chapter 1, sections 1.6.1 to 1.6.2 (voltage and resistance measurements), pp. 1-25 to 1-27; chapter 3, caution list, p. 3-42; chapter 4, section 4.2.1.1 (never connect an ohmmeter to a live circuit), p. 4-2"
  - id: navedtra-electricians-mate-3-2-1981
    locator: "chapter 2, Safety precautions (no rings, watches or metal objects; tighten test leads), p. 2-12"
  - id: tm-9-8000-automotive-1985
    locator: "chapter 17, para. 17-2a (starting current 200 to 600 A), p. 17-1"
uncertain:
  - "The figure of 0.5 V as the most a healthy cable run or switch should lose is a common rule of thumb; no cleared source gives a number. Sensitive electronics may need less loss."
  - "Boats with AC shore power or an inverter also carry 230 V or 120 V, which can kill. This page covers only the low-voltage DC side. Isolate AC sources before touching any wiring you are not sure of."
  - "Some modern boats use networked (digital) switching. Its fault-finding depends on the maker's software and is not covered by any cleared source."
---

## Situation

Something electrical has stopped working, works only now and then, or blows
its fuse or trips its breaker. On a boat, most faults are a blown fuse, a
corroded or loose connection, or a chafed wire. This page shows how to find
which, using a multimeter. For charging problems, see
[Battery not charging](battery-not-charging.html).

## Do now

**Safety first.** Take off rings and your watch
([Electrician's Mate 3 & 2, ch. 2](../library/navedtra-electricians-mate-3-2-1981.html)).
A battery can deliver hundreds of amps (a starter motor alone draws 200 to
600 A, [TM 9-8000, para. 17-2](../library/tm-9-8000-automotive-1985.html)).
Through a short circuit, that is enough to melt a spanner, start a fire or
burn you. Never work near batteries with a flame or
spark ([NEETS Module 1, 2.4.3.4](../library/navedtra-neets.html)). If wiring
smells hot or smokes, switch off at the battery and go to
[Fire on board](../emergency/fire-on-board.html).

1. **Think about the whole circuit.** Current goes from the battery positive,
   through the main switch, a fuse or breaker, the panel switch, the
   positive wire, the load (lamp, pump), and back through the negative wire to
   the battery. A fault can be anywhere in that loop, including the negative
   return.
2. **Check the obvious.** Main battery switch on? Panel switch on? Breaker
   tripped? Is the bulb or device itself dead (try a spare or another
   socket)?
3. **Check the fuse.** Look at it, then test it. With the power on, measure
   from each end of the fuse to battery negative: voltage on both ends means
   the fuse is good. Or, with the load switched on, measure across the fuse:
   about 0 V means good, full battery voltage means blown
   ([NEETS Module 3, 2.3.1.5.1.3](../library/navedtra-neets.html)).
4. **Measure at the load.** Set the meter to its highest DC volts range,
   then step down
   ([NEETS Module 16, 1.6.1](../library/navedtra-neets.html)). With the
   switch on, put the probes on the load's positive and negative terminals.
   - Full battery voltage but the load does not work: the load is faulty.
   - No voltage: the break is upstream. Go to step 5.
   - Low voltage (more than about 0.5 V below the battery): a bad
     connection somewhere is losing voltage. Go to step 6.
5. **Find the break.** Keep the black probe on a known good negative (the
   battery negative or the negative bus bar). Move the red probe back along
   the positive side: load terminal, each joint, the switch output, the
   switch input, the fuse. The fault lies between the last point with no
   voltage and the first point with voltage. Then do the same on the
   negative side, with the red probe on a known good positive.
6. **Find a bad connection.** With the load switched on, measure across each
   joint, switch or fuse in turn (one probe each side). A good joint reads
   almost 0 V. A reading of several tenths of a volt or more shows the
   resistance is there. Clean, tighten or remake that joint.
7. **A fuse that blows again** means a short circuit or an overloaded
   circuit. **Never fit a larger fuse**
   ([NEETS Module 3, 2.3.1.6.1](../library/navedtra-neets.html)). Switch
   off, disconnect the load, and fit a new fuse. If it still blows, the short
   is in the wiring: look for chafe where cables pass through bulkheads,
   under floorboards, or near the engine. If it holds, reconnect the load:
   if it blows now, the load is at fault.
8. **Use the ohmmeter only on dead circuits.** Switch off, remove the fuse,
   and disconnect the wire you want to test. Never connect an ohmmeter to a
   live circuit
   ([NEETS Module 16, 4.2.1.1](../library/navedtra-neets.html)). A good wire
   reads close to 0 ohms end to end; a broken one reads infinite.

## Why

In an open circuit no current flows, so the whole battery voltage appears
across the break. That is why the voltmeter finds a break by "voltage on one
side, none on the other". In a short circuit, current takes an accidental
low-resistance path, for example through broken insulation, and rises until
something gets hot or the fuse melts
([NEETS Module 1, 3.7.2-3.7.3](../library/navedtra-neets.html)).

A fuse protects the wire, not the device. A larger fuse lets the wire
overheat before it blows, which is how electrical fires start. Corrosion at
a joint adds resistance, and resistance with current flowing makes heat and
drops voltage
([NEETS Module 3, 2.3.1.6.2](../library/navedtra-neets.html)). Salt air makes
corroded joints the most common fault on boats.

## Check that it worked

- The device works with the voltage at its terminals within about 0.5 V of
  the battery voltage.
- The new fuse holds with the device running for several minutes.
- No joint, wire or fuseholder is warm to the touch after running.

## If that fails

- **Intermittent fault:** wiggle each wire and connector with the circuit on
  and the meter connected; watch for the reading to jump.
- **No spare wire or connector:** a temporary cable from another circuit's
  fuse (of the same or lower rating) can run a vital item such as navigation
  lights or a bilge pump. Label it and fix it properly later.
- **Whole boat dead:** check the main battery switch, the main fuse near the
  battery, and both battery cables, then the battery itself. See
  [Batteries](../know-your-boat/batteries.html) and
  [12 V and 24 V systems on board](../know-your-boat/marine-electrical-systems.html).
- **Bilge pump will not run:** see
  [Bilge pump not working](bilge-pump-not-working.html).
- **Engine will not crank:** see
  [Engine won't turn over](engine-wont-crank.html).
- **Lost VHF or navigation lights at night:** use a hand-held VHF and a
  torch on the sails, and see
  [Navigation lights and day shapes](../run-the-boat/navigation-lights-and-shapes.html).
