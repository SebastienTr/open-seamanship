---
title: Corrosion and anodes
summary: Why metals under water corrode faster when joined to other metals, how sacrificial anodes (zincs) protect them, which anode metal to use, and how stray electric current and crevices destroy fittings.
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
  - id: navpers-engineman-1957
    locator: "Engineman 3, ch. 11, 'Zincs' (dissimilar metals in sea water, zincs take the attack, metallic contact needed, locations in coolers), pp. 416-417; ch. 14, 'Care of zincs' (hardness and cleanliness of one metal can also set up a cell; clean zincs; inspect at least monthly; good metallic contact; close sea connections first), pp. 500-501"
  - id: wikipedia-en
    locator: "'Galvanic corrosion' (revision 2026-10-19): lead and sections 'Overview' (electrolyte and conducting path both needed), 'Examples' (galvanised steel, HMS Alarm copper and iron, aluminium hull with stainless steel water jets), 'Prevention' (insulate metals, coat the more noble metal, match metals, shore-power earth and marina 'batteries'), 'Anodic index', 'Electrolytic corrosion'. 'Galvanic anode' (revision 2026-05-10): sections 'Theory' (electron and ion path both needed; zinc bolted on in air gives no protection) and 'Anode materials' (zinc and aluminium in salt water, magnesium in fresh water). 'Cathodic protection': section 'Ships and boats' (yachts use anodes to protect outboards and other parts; solid electrical connection needed; aluminium hulls with steel fittings). 'Crevice corrosion' (revision 2025-12-03): sections 'Mechanism' (stainless steel's passive film breaks down in stagnant gaps)"
  - id: fao-small-fishing-vessel-inspection-2025
    locator: "Sec. 3.5 (steel vessels: inspect anodes on hull and stern gear; replace when more than 70 per cent depleted), pp. 21-22; sec. 3.6 (aluminium vessels: cathodic protection, replace anodes at 70 per cent depletion; pay attention to crevices and joints), p. 24"
  - id: mca-small-fishing-vessel-code-2024
    locator: "Sec. 4.8.1.15 (adequate cathodic protection; anodes efficiently connected to the system and the hull, and not painted over); 4.8.3.3 (hull earth plates connected and not painted over)"
  - id: knight-sailing
    locator: "Ch. IX 'Fitting Out', 'Ballast' (keep copper sheathing an inch or two away from an iron keel, galvanic action); Gutenberg text, unpaginated: cite by chapter and section heading"
uncertain:
  - "A full galvanic series for sea water (which metal is anodic to which, and by how much) is not included because no cleared copy was available while writing; the rough order given here (magnesium, zinc, aluminium, steel, bronze and copper alloys, stainless steel) is standard engineering knowledge. Check a published galvanic series before mixing metals."
  - "The 'Reading your anodes' signs, and dezincification (zinc leached out of brass, leaving it pink and weak), are common surveyor's knowledge, not taken from a cleared source."
  - "Galvanic isolators and isolation transformers on shore power are the usual cure for shore-power corrosion; no cleared source describes them."
  - "Using the wrong anode metal (for example zinc in fresh water, or magnesium in salt water) is widely reported to fail or to over-protect; the Wikipedia article supports the material choices but not detailed figures."
---

## A battery you did not mean to build

Put two different metals in sea water and join them with a wire, a bolt or the
engine's bonding cable, and you have built a battery. Current flows. The more
"active" metal (the **anode**) dissolves; the more "noble" one (the
**cathode**) is spared. Both an electrical path between the metals and the
water around them are needed; take away either and the attack stops
([Wikipedia, "Galvanic corrosion", "Overview"](../library/wikipedia-en.html);
[Engineman 3, p. 416](../library/navpers-engineman-1957.html)).

Even one piece of metal can corrode this way, if one part is harder or cleaner
than another ([Engineman 3, p. 500](../library/navpers-engineman-1957.html)).

Sailors have known this a long time. The Royal Navy found in the 1760s that
iron nails holding copper sheathing had "dissolved into a kind of rusty
Paste" ([Wikipedia, "Galvanic corrosion", "Examples"](../library/wikipedia-en.html)),
and 19th-century yachtsmen kept copper sheathing away from iron keels
([Knight, *Sailing*, ch. IX](../library/knight-sailing.html)).

## Which metal suffers

Roughly, from most active (eaten first) to most noble:

**magnesium, zinc, aluminium, mild steel and cast iron, bronze, brass and
copper, stainless steel (when passive)**

The further apart two metals are, the faster the active one goes. In a salty
environment, engineers try to keep joined metals within about 0.15 V of each
other ([Wikipedia, "Galvanic corrosion", "Anodic index"](../library/wikipedia-en.html)).
Examples that matter at sea:

- **Aluminium next to stainless steel or bronze.** The aluminium is eaten.
  This damaged the aluminium hull of a modern US warship around its stainless
  water jets ([Wikipedia, "Galvanic corrosion", "Examples"](../library/wikipedia-en.html)).
  Outboard legs, aluminium masts and aluminium hulls need care with stainless
  fittings and copper-based antifouling.
- **Galvanised steel.** The zinc coating corrodes first and protects the
  steel until the zinc is gone (same section).
- **A large noble area and a small active one** is the worst case. If you can
  paint only one metal, paint the more noble one
  ([Wikipedia, "Galvanic corrosion", "Prevention"](../library/wikipedia-en.html)).

## Sacrificial anodes

An anode ("zinc") is a lump of a more active metal, fixed so it is in good
electrical contact with the metal you want to protect and in the same water.
It corrodes instead. Zincs "do not prevent electrolysis but, instead, provide
a surface for the attack"; they "centralize electrolysis" in a part that can
be replaced ([Engineman 3, pp. 416-417](../library/navpers-engineman-1957.html)).

Anodes are fitted on the hull of metal boats, on propeller shafts and
propellers, on outboard and saildrive legs, on rudders, and inside engine heat
exchangers ([Wikipedia, "Cathodic protection", "Ships and boats"](../library/wikipedia-en.html);
[Diesel cooling systems](diesel-cooling-systems.html)).

Rules that follow from how they work:

- **Electrical contact is everything.** Zinc bolted to steel in air, or a zinc
  with a corroded or painted contact face, protects nothing
  ([Wikipedia, "Galvanic anode", "Theory"](../library/wikipedia-en.html)).
- **Never paint an anode**, nor the hull earth plate
  ([MCA code, 4.8.1.15 and 4.8.3.3](../library/mca-small-fishing-vessel-code-2024.html)).
- **Keep it clean.** The Navy cleaned engine zincs back to bright metal and
  inspected them at least monthly
  ([Engineman 3, p. 501](../library/navpers-engineman-1957.html)).
- **Replace before it is gone.** Renew hull anodes when they are about
  70 per cent used ([FAO 2025, pp. 21 and 24](../library/fao-small-fishing-vessel-inspection-2025.html)).

## Which anode metal

([Wikipedia, "Galvanic anode", "Anode materials"](../library/wikipedia-en.html))

| Water | Anode | Notes |
| --- | --- | --- |
| Salt | Zinc or aluminium alloy | Zinc reliable; aluminium alloy lighter, longer-lasting |
| Brackish | Aluminium alloy usually | Check the maker's advice |
| Fresh | Magnesium | Dissolves fast in salt water; can over-protect |

## Reading your anodes

- **Anode barely used after a season**: it may not be connected, may be
  painted, or may be the wrong metal for the water.
- **Anode gone in weeks**: something is driving current: a stray current, a
  shore-power earth fault, or a new noble fitting nearby.
- **Pink, spongy brass or bronze fittings**: zinc being leached out of the
  alloy. See [Through-hulls and seacocks](through-hulls-and-seacocks.html).

## Stray-current corrosion

Current from outside, not from the metals themselves, does the same damage
much faster ("electrolytic corrosion")
([Wikipedia, "Galvanic corrosion", "Electrolytic corrosion"](../library/wikipedia-en.html)).
Causes on boats include a wire or pump with poor insulation touching bilge
water, and shore power. A boat plugged into shore power has its underwater
metal joined, through the earth wire, to every other boat on the pontoon and to
the marina's buried copper earth, making a set of batteries that can eat your
propeller or a steel hull
([Wikipedia, "Galvanic corrosion", "Prevention"](../library/wikipedia-en.html)).
See [12 V and 24 V systems on board](marine-electrical-systems.html).

## Stainless steel is not stainless everywhere

Stainless steel resists corrosion because of a very thin oxide film. Where
sea water sits still in a narrow gap, under a washer, a seal, a clamp or inside
a rigging terminal, the film can break down and the steel corrodes from inside
the gap ([Wikipedia, "Crevice corrosion", "Mechanism"](../library/wikipedia-en.html)).
This is why stainless fittings that look bright can fail suddenly. See
[Sails and rigging](sails-and-rigging.html).

## Related pages

- [Hull materials](hull-materials.html)
- [Engine maintenance routine](engine-maintenance.html)
