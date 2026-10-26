---
title: GMDSS and DSC
summary: The global distress system in plain words, the sea areas, digital selective calling, EPIRBs, PLBs, SARTs and NAVTEX, and what small boats and fishing boats need to know.
kind: explainer
section: run-the-boat
region: international
language: en
licence: CC-BY-SA-4.0
safety: normal
status: draft
authors: [claude]
reviewers: []
reviewed: null
sources:
  - id: nga-pub-117-2014
    locator: "Chapter 3, 300A 'GMDSS' definitions and 300B 'Local warnings (Sea Area A1)', p. 3-3; Chapter 4, 400A to 400C (EPIRB, SART, AIS-SART), pp. 4-3 to 4-4; 400D maritime satellite channels and 400E 'VHF, MF and HF Digital Selective Calling', p. 4-10; 400H 'Instructions for canceling inadvertent distress alerts', pp. 4-16 to 4-17"
  - id: mca-fishermens-safety-guide
    locator: "Section 6, 'GMDSS', 'Digital selective calling (DSC)', 'EPIRBs', 'PLBs', pp. 69-71"
  - id: mca-small-fishing-vessel-code-2024
    locator: "Section 7.10.2 (PLBs on single-handed vessels); Section 9.2.3 (VHF DSC as primary means of alerting); equipment tables in Chapter 7 (EPIRB or PLBs by length)"
  - id: cfr-46-part-28
    locator: "46 CFR 28.150 'Emergency Position Indicating Radio Beacons'; 46 CFR 28.140, Table 28.140 (monthly EPIRB test)"
  - id: wikipedia-en
    locator: "'Global Maritime Distress and Safety System', lead and sections 'History', 'Satellite', 'GMDSS sea areas'; 'Digital selective calling', sections 'Distress' and 'Other priorities'"
uncertain:
  - "Pub. 117 is the 2014 edition. Satellite services have changed since (Inmarsat B and Fleet 77 ended; Iridium was recognised in 2020 and sea area definitions were revised in 2024, according to Wikipedia). Check current equipment rules."
  - "The range of Sea Area A1 is given as about 20 to 30 miles by the MCA and 30 to 40 nautical miles by Pub. 117 and Wikipedia. It depends on the coast stations and is declared by each country."
  - "Carriage rules for small boats and fishing boats are national. This page gives the UK and US rules found in the cited sources; French rules (Division 240 and the fishing-vessel divisions) were not checked here."
  - "What a small-boat DSC set does after a distress alert (repeat interval, how it is acknowledged) varies by model. Read your set's manual and practise with a test call."
---

The **Global Maritime Distress and Safety System (GMDSS)** is the
international system, run through the IMO, that lets a vessel in trouble
raise the alarm automatically, by satellite and by radio, and that sends
navigation and weather warnings to ships
([Pub. 117, 300A, p. 3-3](../library/nga-pub-117-2014.html)). It moved
distress alerting from ship-to-ship to ship-to-shore, where rescue
coordination centres pick it up; it became fully required on SOLAS ships in
1999 ([Wikipedia, 'Global Maritime Distress and Safety System', History](../library/wikipedia-en.html)).

Ships of 300 gross tonnage and over, and some smaller vessels including some
fishing boats, must carry GMDSS equipment
([MCA Fishermen's Safety Guide, p. 69](../library/mca-fishermens-safety-guide.html)).
Leisure boats do not have to, but the parts that matter most for a small
boat, a DSC radio and a 406 MHz beacon, work with the same rescue system.

## Sea areas

What a ship must carry depends on where it goes
([MCA Fishermen's Safety Guide, p. 69](../library/mca-fishermens-safety-guide.html);
[Wikipedia, 'GMDSS sea areas'](../library/wikipedia-en.html)):

| Area | Meaning | Main equipment |
| --- | --- | --- |
| A1 | In range of a VHF coast station with DSC watch, typically 20 to 40 miles | VHF with DSC |
| A2 | Beyond A1, in range of an MF coast station with DSC watch, about 100 miles | MF with DSC |
| A3 | Beyond A2, within a recognised satellite system's coverage | Satellite terminal or HF |
| A4 | The rest: the polar regions (none for Iridium users) | HF |

## Digital selective calling (DSC)

A DSC radio sends a short digital message instead of a voice call. It is
programmed with your **MMSI**, a nine-digit number that identifies your
station ([Pub. 117, p. 3-3](../library/nga-pub-117-2014.html)). Connected to
a GPS, it sends your position too. The Coast Guard urges owners to make that
connection ([Pub. 117, 400E, p. 4-10](../library/nga-pub-117-2014.html)).

DSC distress channels: **VHF channel 70** (156.525 MHz), and on MF/HF
4207.5, 6312.0, 8414.5, 12577.0 and 16804.5 kHz (same page). Channel 70 is
data only; voice follows on channel 16. In the UK the coastguard treats VHF
DSC as the primary way to raise distress and urgency alerts
([UK small fishing vessel code, 9.2.3](../library/mca-small-fishing-vessel-code-2024.html)).
Small boats are advised to fit DSC, because many ships listen mainly for DSC
calls ([MCA Fishermen's Safety Guide, p. 70](../library/mca-fishermens-safety-guide.html)).

**Sending a distress alert**: the red DISTRESS button is under a cover so it
cannot be pressed by accident. Many sets let you choose the nature of
distress (fire, flooding, collision, grounding, listing, sinking, disabled
and adrift, abandoning ship, piracy, man overboard) before sending
([Wikipedia, 'Digital selective calling', Distress](../library/wikipedia-en.html)).
The alert should carry the last position and its time in UTC; if time
allows, add the nature of distress
([Pub. 117, p. 4-10](../library/nga-pub-117-2014.html)). Then make the voice
MAYDAY on channel 16: see [Mayday: calling for help](../emergency/mayday-distress-call.html)
and [Using a VHF radio](vhf-radio-procedure.html). The set repeats the alert
every few minutes, up to five times, until it is acknowledged; a coast
station waits a little under 3 minutes before acknowledging, so that nearby
ships also receive it
([Wikipedia, 'Digital selective calling', Distress](../library/wikipedia-en.html)).

DSC also sends urgency, safety and routine calls to one station or to all
ships, then moves both sets to a voice channel (same article, 'Other
priorities'). Test with a coast station no more than once a week
([Pub. 117, p. 4-10](../library/nga-pub-117-2014.html)).

## Beacons

- **EPIRB** (emergency position-indicating radio beacon) transmits on 406 MHz
  to the Cospas-Sarsat satellites, which pass the alert to a rescue centre.
  Category I beacons float free and switch on automatically, released by a
  hydrostatic unit; Category II are switched on by hand. A beacon with built-in
  GPS sends its position; 121.5 MHz is now only a homing signal for rescuers
  close by ([Pub. 117, 400B, p. 4-3](../library/nga-pub-117-2014.html)).
- **PLB** (personal locator beacon) is a small 406 MHz beacon worn on the
  person. Wear it on your lifejacket, not on a belt that may be under water
  ([MCA Fishermen's Safety Guide, pp. 70-71](../library/mca-fishermens-safety-guide.html)).
- **SART** (search and rescue transponder) answers a ship's 9 GHz (3 cm, X-band)
  radar with a line of 12 dots, out to about 8 nautical miles (15 km); it does
  not show on 3 GHz radar. An **AIS-SART** shows on AIS displays instead
  ([Pub. 117, 400C, p. 4-4](../library/nga-pub-117-2014.html)).
- **NAVTEX** is a small receiver that prints or displays navigation and weather
  warnings, broadcast on 518 kHz in English and on 490 kHz in some local
  languages ([Pub. 117, p. 3-3](../library/nga-pub-117-2014.html);
  [Wikipedia, 'GMDSS', NAVTEX](../library/wikipedia-en.html)). See also
  [UK: weather and safety broadcasts](../regions/uk-safety-information.html)
  and [France: marine weather bulletins](../regions/france-weather-bulletins.html).

**Register every 406 MHz beacon** and update the record if the boat's owner,
name or details change. Rescuers use the registration to identify you
([Pub. 117, 400B and 400H, pp. 4-3 and 4-17](../library/nga-pub-117-2014.html)).
In the UK registration with the MCA is required
([MCA Fishermen's Safety Guide, p. 71](../library/mca-fishermens-safety-guide.html)).
Never tie an EPIRB to the boat: it must be free to float up. Its lanyard is
for tying it to a liferaft or a person
([Pub. 117, p. 4-17](../library/nga-pub-117-2014.html)).

## What fishing boats must carry

- **UK**: every fishing vessel of 10 m and over must carry a float-free EPIRB
  with GPS; under 10 m, either a PLB for every crew member or an EPIRB
  ([MCA Fishermen's Safety Guide, p. 70](../library/mca-fishermens-safety-guide.html)).
  The current code lets a single-handed boat carry either, but the MCA
  recommends both ([UK small fishing vessel code, Chapter 7 tables and 7.10.2](../library/mca-small-fishing-vessel-code-2024.html)).
- **US**: each commercial fishing vessel must carry an EPIRB under 46 CFR
  part 25, subpart 25.26 ([46 CFR 28.150](../library/cfr-46-part-28.html)),
  tested monthly ([46 CFR 28.140, Table 28.140](../library/cfr-46-part-28.html)).
- **France and elsewhere**: see the national rules; for French leisure boats
  see [France: required safety equipment](../regions/france-safety-equipment.html).

## False alerts

Most false alerts come from human error. If you send one, cancel it at once
by voice: switch to channel 16 and tell all stations your name, call sign,
MMSI and position and that you cancel your distress alert of (date, time
UTC). If an EPIRB goes off by accident, leave it on and contact the
coastguard or rescue centre to cancel. Crews who report and cancel a false
alert are not normally penalised
([Pub. 117, 400H, pp. 4-16 to 4-17](../library/nga-pub-117-2014.html)).
