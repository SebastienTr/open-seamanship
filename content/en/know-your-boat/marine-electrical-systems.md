---
title: 12 V and 24 V systems on board
summary: How a boat's low-voltage DC system is put together (batteries, switches, fuses, cables, charging), why bad connections cause most faults, why bigger boats use 24 V, and the rules that keep it from starting a fire.
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
    locator: "Ch. 11 'Electricity': para. 11-10 'Resistance' (length, size, material, temperature) and 11-11 'Ohm's Law' (most electrical troubles come from increased resistance at bad connections, broken strands, dirty contacts; a failed regulator raises voltage and current), pp. 11-10 to 11-12; ch. 12, para. 12-11 two 12 V batteries in series for 24 V, p. 12-10; ch. 13, para. 13-23 'The Automotive Alternator' and 13-26 'AC Generator Regulation' (rectifier stops back-flow; regulator limits voltage)"
  - id: navedtra-neets
    locator: "Module 1 (NAVEDTRA 14173A), ch. 3, power P = E x I, p. 3-17. Module 3 (NAVEDTRA 14175A, 2013), ch. 2: protection devices in series, fuses melt before the conductor they protect, pp. 2-4 to 2-5; fuse rating 125 per cent of normal current for overload, 150 per cent for short circuit only, p. 2-11. Module 4 (NAVEDTRA 14176A), ch. 1, 1.5 'Factors governing the current rating' (excess current heats the wire, burns the insulation and can start a fire; confined wires carry less), pp. 1-14 to 1-15"
  - id: mca-small-fishing-vessel-code-2024
    locator: "Sec. 4.8.1.8 to 4.8.1.15 (switchboards marked and fuse ratings checked; every circuit except the starter supply protected against overload and short circuit; unprotected cables kept short; cables not run below floor plates, correct current capacity, not secured with plastic clips in machinery spaces; anodes connected and not painted); 4.8.3 'D.C. Systems Up To 24 volts' (two-wire systems, double-pole cut-off switch at each battery or bank, bilge pumps before the switch); 4.8.4 'A.C. Systems' (AC kept separate from DC)"
  - id: fao-small-fishing-vessel-inspection-2025
    locator: "Sec. 4, 'Electrical systems inspection' (connections secure, no exposed wires, correct fuses and breakers, insulation resistance, shore power with appropriate breakers), p. 42"
uncertain:
  - "Recommended voltage-drop limits and cable sizes for boats are set by standards (ISO and others) that are not openly licensed. No figure is given here. Size cables from a current table for the actual length of the run, or ask a marine electrician."
  - "That 24 V is common on larger yachts and workboats is general knowledge; the cleared sources show 24 V only on military vehicles (two 12 V batteries in series)."
  - "Typical alternator charging voltages (about 14 to 14.4 V on a 12 V system) depend on battery type and are not given in a cleared source."
  - "Shore power (230 V or 120 V AC) can kill and is not covered here beyond the separation rule; have AC work done by a qualified electrician."
---

## The parts of a DC system

Most boats under about 15 m (50 ft) run on **12 V DC**; many larger yachts and
workboats use **24 V**. The parts are the same:

1. **Batteries**: a starting battery and often a separate house bank. See
   [Batteries](batteries.html).
2. **Battery switches** (isolators) to cut each battery or bank off.
3. **Main fuse** close to the battery on the big positive cable.
4. **Distribution panel**: a fuse or circuit breaker for each circuit.
5. **Cables**: a positive and a negative wire to every device.
6. **Charging sources**: the engine's alternator, a shore-power charger, solar
   panels, a wind or water generator.

A UK code for small fishing vessels sets out the same backbone: systems "two
wire"; a double-pole cut-off switch at each battery or bank, with automatic
bilge pumps wired before it; every circuit except the battery-to-starter cable
protected against overload and short circuit; switchboards clearly marked; AC
wiring kept separate from DC
([MCA code, 4.8.1.8-4.8.1.9, 4.8.3, 4.8.4](../library/mca-small-fishing-vessel-code-2024.html)).

"Two wire" means each device has its own return wire to the battery negative.
The metal of the engine or hull is not used to carry current back.

## Volts, amps and resistance

- **Voltage** pushes; **current** (amps) flows; **resistance** (ohms) holds it
  back. Volts = amps x ohms (Ohm's law)
  ([TM 9-8000, para. 11-11](../library/tm-9-8000-automotive-1985.html)).
- **Power** (watts) = volts x amps
  ([NEETS 1, p. 3-17](../library/navedtra-neets.html)). A 60 W device draws
  5 A at 12 V but only 2.5 A at 24 V.

That second point is why larger boats use 24 V. For the same power, half the
current flows, so cables can be thinner and less is lost as heat in long runs.
Two 12 V batteries in series make 24 V
([TM 9-8000, para. 12-11](../library/tm-9-8000-automotive-1985.html)). Never
connect a 12 V device straight to a 24 V supply.

## Why most faults are bad connections

A wire's resistance rises with its length, falls with its thickness, and
rises with heat ([TM 9-8000, para. 11-10](../library/tm-9-8000-automotive-1985.html)).
The Army's own summary: "A great majority of electrical troubles on automotive
vehicles result from increased resistance in circuits due to bad connections,
deteriorated wiring, dirty or burned contacts in switches, or other such
problems" ([TM 9-8000, para. 11-11](../library/tm-9-8000-automotive-1985.html)).
At sea, add salt and damp. A corroded joint lets less current through, so a
light glows dim, a pump runs slow, a starter clicks but will not turn.

Two consequences for fault finding:

- **Measure voltage at the device while it is switched on.** A good voltage at
  the battery and a low one at the device means resistance in between.
- **A bad connection gets hot.** Feel (carefully) for a warm terminal, fuse
  holder or switch after a load has run.

Step by step: [Finding a 12 V electrical fault](../fix-it/electrical-fault-finding.html).

## Fuses and breakers protect the wire

If more current flows through a wire than it is rated for, it heats up, the
insulation burns and a fire can start. A wire in a bundle or conduit runs
hotter and can carry less than one in free air
([NEETS 4, pp. 1-14 to 1-15](../library/navedtra-neets.html)).

A fuse or breaker is there to protect the **wire**. It must be in series with
the circuit, and it must open before the wire is harmed; the earliest fuses
were simply a thinner piece of wire than the one they protected
([NEETS 3, pp. 2-4 to 2-5](../library/navedtra-neets.html)). So:

- Put the fuse **close to the source of power**, so the whole length of wire
  is protected.
- Never replace a blown fuse with a bigger one, a bolt or foil. If a fuse
  blows again, there is a fault: find it.
- A fuse sized at about 125 per cent of the normal current protects against
  overload; at 150 per cent it protects only against short circuits
  ([NEETS 3, p. 2-11](../library/navedtra-neets.html)).

Check fuse ratings regularly; the MCA code asks for it
([MCA code, 4.8.1.8](../library/mca-small-fishing-vessel-code-2024.html)).
The heavy cable from battery to starter usually has no fuse, so keep it short,
well supported and protected from chafe
([MCA code, 4.8.1.9 and 4.8.1.11](../library/mca-small-fishing-vessel-code-2024.html)).

## Cables on a boat

- Use cable rated for the current, for the length of the run, and for the
  heat of the engine room ([MCA code, 4.8.1.14](../library/mca-small-fishing-vessel-code-2024.html)).
- Keep cables high, out of the bilge water; where they must run low, use
  conduit (same section).
- Support them well, protect them where they pass through bulkheads, and keep
  them clear of fuel tanks and hot exhausts.
- Connections should be secure, with no exposed bare wire
  ([FAO 2025, p. 42](../library/fao-small-fishing-vessel-inspection-2025.html)).

## Charging

The engine's **alternator** makes alternating current, which diodes inside it
turn into DC. The diodes also stop the battery from discharging back through
the alternator when the engine stops. A **voltage regulator** holds the output
voltage within limits
([TM 9-8000, paras. 13-23 and 13-26](../library/tm-9-8000-automotive-1985.html)).
If the regulator fails high, too much current is forced through every circuit,
batteries boil and equipment is damaged
([TM 9-8000, para. 11-11](../library/tm-9-8000-automotive-1985.html)).

Different battery types need different charge voltages. If you change from
lead-acid to lithium, the alternator regulator, chargers and solar controllers
must all suit the new battery. See [Batteries](batteries.html).

Signs of a charging fault: the charge lamp stays on, the voltmeter shows no
rise when the engine runs, or batteries go flat however long you motor. See
[Battery not charging](../fix-it/battery-not-charging.html).

## Shore power and AC

Shore power and inverters bring mains-voltage AC on board. It can kill. Keep
AC wiring and switchgear separate from DC
([MCA code, 4.8.4](../library/mca-small-fishing-vessel-code-2024.html)), use
proper breakers ([FAO 2025, p. 42](../library/fao-small-fishing-vessel-inspection-2025.html)),
and leave AC work to someone qualified. Stray currents from faulty wiring also
eat underwater metal: see [Corrosion and anodes](corrosion-and-anodes.html).

## In an emergency

Electrical smoke or a smell of hot insulation: switch off at the battery
switch at once, then see [Fire on board](../emergency/fire-on-board.html).
