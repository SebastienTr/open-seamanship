---
title: Bilge pump not working
summary: The electric bilge pump does not run, runs but moves no water, or the manual pump has lost its suction. How to find the fault quickly, starting with the most likely causes.
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
  - id: wikipedia-en
    locator: "'Bilge pump', lead section (spark-proof pumps, float switches, primary and backup pumps); 'Float switch', two-stage switches"
  - id: navedtra-damage-controlman-3-2-1986
    locator: "chapter 5, P-250 portable pumps (tight suction connections and gaskets, strainer fully under water and clear of mud, air leaks on the suction side stop the pump drawing), pp. 5-45 to 5-48"
  - id: navedtra-neets
    locator: "Module 3 (NAVEDTRA 14175A), chapter 2, checking and replacing fuses, corroded fuseholders, pp. 2-25 to 2-28"
  - id: mca-fishermens-safety-guide
    locator: "Section 3, engine room ('Do not ignore the engine': install a bilge level alarm and check it works; sea inlet valves that can be closed even under water), PDF pp. 29-30"
uncertain:
  - "No cleared source covers small diaphragm (manual) bilge pumps, their flap valves or their servicing. The advice on them is general."
  - "Electronic (sensor) level switches, and pumps with built-in sensors that run a short test cycle, behave differently from float switches. Check the maker's sheet."
  - "Whether a discharge hose needs a vented loop or a non-return valve depends on how it is installed; no cleared source covers this for small craft."
---

## Situation

Water is collecting in the bilge and the pump does not clear it: the pump
does not run, runs but moves no water, or the manual pump handle moves but
nothing comes out. **If water is coming in faster than you can bail, go to
[Taking on water](../emergency/taking-on-water.html) now.** Use buckets
while you work on the pump.

## Do now

1. **Find out where the water is coming from**, and stop it if you can.
   Taste it: salt water means a leak from the sea; fresh water usually means
   a tank, pipe or rain. Check the stern gland, seacocks, cockpit drains,
   engine hoses and the toilet. See
   [Leaking stern gland](leaking-stern-gland.html) and
   [Through-hulls and seacocks](../know-your-boat/through-hulls-and-seacocks.html).
2. **Electric pump does not run:** switch it to "manual" or "on" at the panel.
   - Runs on manual but not on auto: the **float switch** is stuck or
     failed. Lift the float by hand (or with a boathook); clear any rag,
     hair or debris that holds it down. Bilge pumps are often fitted with a
     float switch that starts the pump at a set level
     ([Wikipedia, 'Bilge pump'](../library/wikipedia-en.html)).
   - Does not run at all: check the battery switch, then the fuse or
     breaker. A blown fuse means find the cause before fitting a new one of
     the same rating, never a larger one
     ([NEETS Module 3, ch. 2](../library/navedtra-neets.html)). Then check
     the connections near the pump: they live in the wet and corrode. See
     [Finding a 12 V electrical fault](electrical-fault-finding.html).
   - Hums but does not pump, or gets hot: the impeller is jammed with
     debris. Switch off, lift the pump, clear it.
3. **Pump runs but no water comes out:**
   - Clear the strainer or the pump inlet. Debris is the most common cause.
   - Check the pump is under water and the inlet is not in mud or sludge.
   - Check the discharge hose is not kinked, crushed or blocked, and that
     its outlet seacock (if any) is open.
4. **Manual pump has no suction:**
   - Clear the strainer at the end of the suction hose; make sure it sits
     in clear water.
   - Tighten every hose clip on the suction side. A small air leak there
     stops a pump drawing water
     ([Damage Controlman 3 & 2, ch. 5](../library/navedtra-damage-controlman-3-2-1986.html)).
   - If the handle has no resistance, the diaphragm may be split or a flap
     valve stuck open with debris. Open the pump and clean or replace the
     valves; spares are small and worth carrying.
5. **Run the backup pump** if you have one. It is normally mounted higher
   than the main pump so it stays clear of debris
   ([Wikipedia, 'Bilge pump'](../library/wikipedia-en.html)).

## Why

Bilge pumps fail in a few simple ways: no power, a stuck float, or a blocked
inlet. The bilge is where all the boat's debris ends up: wood shavings, hair,
labels, rags, sludge. These block strainers, jam floats and wrap round
impellers. The wiring sits in salt water and corrodes. On the suction side, a
pump can only pull water if the hose is airtight; any leak lets it suck air
instead
([Damage Controlman 3 & 2, pp. 5-45 to 5-48](../library/navedtra-damage-controlman-3-2-1986.html)).

Electric bilge pumps are designed not to make sparks, because petrol or gas
vapour can collect in the bilge
([Wikipedia, 'Bilge pump'](../library/wikipedia-en.html)). Replace a failed
pump with one made for bilges, not any 12 V pump.

## Check that it worked

- The pump starts when you lift the float and stops when you let it drop.
- A strong, steady stream comes out of the discharge outlet.
- The bilge alarm (if fitted) sounds when the water rises, and stops when the
  pump clears it. The MCA asks fishing boats to fit one and test it
  regularly ([MCA guide, PDF p. 30](../library/mca-fishermens-safety-guide.html)).
- After a few hours, the bilge level is where it normally sits.

## If that fails

- Bail with buckets. Two people with buckets move a lot of water.
- If water is still rising, call for help early and ask for a pump to be
  brought out. See [Mayday: calling for help](../emergency/mayday-distress-call.html)
  and [Taking on water](../emergency/taking-on-water.html).
- **Pump keeps running on its own:** water is still coming in from
  somewhere, or the float switch has stuck on. Find out which; a pump that
  runs dry for hours will burn out and drain the battery. See
  [Battery not charging](battery-not-charging.html).
