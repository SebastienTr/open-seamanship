---
title: VHF channels
summary: Marine VHF channels 16, 70, 06, 13 and the others you will meet, with frequencies, what each is for, and where countries differ.
kind: explainer
section: tables
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
    locator: "Ch. 4, section 400D 'List of maritime frequencies', table of US maritime VHF channels, pp. 4-4 to 4-6 (PDF pp. 245-247); section 400E 'VHF, MF and HF digital selective calling', p. 4-10 (PDF p. 250); section 400C (AIS-SART frequencies), p. 4-4"
  - id: wikipedia-en
    locator: "Marine VHF radio, section 'Channels and frequencies' (frequency table and columns for the UK, CEPT Europe, and other countries)"
uncertain:
  - "This table gives the uses common to most countries. Each country sets its own channel plan within the ITU Radio Regulations (Appendix 18), which is not in our library. Port, marina and coastguard working channels differ from place to place: check the pilot book, harbour guide or official list of radio signals for the area."
  - "The official ITU and national tables were not available to us; the international uses here come from NGA Pub. 117 (2014, a US list) and the Wikipedia country columns. Channel plans change; Pub. 117 itself was re-issued in 2021."
  - "Channel 67 (UK small-craft safety), channel 9 (French marinas) and channel 10 (often used by HM Coastguard) are national uses reported by Wikipedia; confirm with the national authority."
  - "In the US many channels carry an 'A' suffix: they are simplex on the ship frequency where the rest of the world uses duplex. A radio set to the wrong region (USA / INT / CAN) will not work on these channels."
---

Marine VHF works by line of sight, so range depends mostly on the height of the
two antennas. Most channels are **simplex**: one person talks at a
time on one frequency. Public-correspondence channels are **duplex**: the
coast station transmits 4.6 MHz above the ship
([Pub. 117, section 400D](../library/nga-pub-117-2014.html);
[Marine VHF radio, wikipedia-en](../library/wikipedia-en.html)).

## The channels everyone must know

| Channel | Frequency (MHz) | Use |
| --- | --- | --- |
| **16** | 156.800 | International distress, safety and calling. Ships and coast stations keep a listening watch on it. |
| **70** | 156.525 | Digital selective calling (DSC) only. **No voice.** The red DISTRESS button sends an alert here. |
| **06** | 156.300 | Ship to ship, safety. Often used on scene between ships and search-and-rescue aircraft. |
| **13** | 156.650 | Bridge to bridge: safety of navigation between ships. Ships may also use it for port movements. |

Sources: Pub. 117 section 400D (channels 06, 13, 16, 70) and section 400E
(channel 70 for DSC distress); Wikipedia "Marine VHF radio" (06 ship-to-air).

How to call: see [VHF radio procedure](../run-the-boat/vhf-radio-procedure.html).
Distress: [Mayday distress call](../emergency/mayday-distress-call.html) and
[GMDSS and DSC](../run-the-boat/gmdss-and-dsc.html).

## Other channels you will meet

The frequency is the one the boat transmits on. For duplex channels the coast
station's frequency is in brackets.

| Channel | Frequency (MHz) | Common use (most countries) | Differences |
| --- | --- | --- | --- |
| 08 | 156.400 | Ship to ship | |
| 09 | 156.450 | Port operations; ship to ship | Europe (CEPT list): marinas. US: calling channel. |
| 10 | 156.500 | Port operations; ship to ship | UK: often used by HM Coastguard. US: commercial. |
| 11 | 156.550 | Port operations, vessel traffic services | |
| 12 | 156.600 | Port operations, vessel traffic services | |
| 14 | 156.700 | Port operations, vessel traffic services | |
| 15 | 156.750 | On-board communications, 1 watt | US: receive only. CEPT list: beach monitoring. |
| 17 | 156.850 | On-board communications, 1 watt | US: state and local government. CEPT list: port operations. |
| 67 | 156.375 | Varies by country | UK: small-craft safety channel with HM Coastguard. CEPT list: coastguard. |
| 72 | 156.625 | Ship to ship | |
| 77 | 156.875 | Ship to ship | |
| 24 to 28 | 157.200 to 157.400 (161.800 to 162.000) | Public correspondence (coast radio stations), duplex | |
| 84 to 86 | 157.225 to 157.325 (161.825 to 161.925) | Public correspondence (coast radio stations), duplex | |
| 87, 88 | 157.375, 157.425 | Simplex; use varies | Their old coast frequencies are now the two AIS channels. |
| AIS 1 | 161.975 | Automatic identification system (AIS), data only | |
| AIS 2 | 162.025 | AIS, data only | |
| WX | 162.400 to 162.550 | | US only: NOAA weather radio, receive only. |

Frequencies follow a fixed pattern: channels 01 to 28 step 50 kHz upward from
156.050 MHz, and channels 60 to 88 sit 25 kHz between them, from 156.025 MHz
([Marine VHF radio, wikipedia-en](../library/wikipedia-en.html)). AIS-SART
survival beacons also transmit on the two AIS frequencies
([Pub. 117, section 400C](../library/nga-pub-117-2014.html)).

## Good habits

- Keep 16 for distress, safety and calling, and move to a working channel to
  talk ([VHF radio procedure](../run-the-boat/vhf-radio-procedure.html)).
- Never speak on 70: it carries DSC data only.
- Some channels are limited to 1 watt (15 and 17 in several countries, 13 in
  the US); use low power for short-range calls.
- Coast stations announce safety and weather broadcasts on 16, then give them
  on a working channel. See
  [France: marine weather bulletins](../regions/france-weather-bulletins.html)
  and [UK: weather and safety broadcasts](../regions/uk-safety-information.html).
- Rescue services by country:
  [France: CROSS, SNSM and calling for help](../regions/france-search-and-rescue.html),
  [UK: HM Coastguard and the RNLI](../regions/uk-search-and-rescue.html).

## See also

- [Phonetic alphabet and numbers](phonetic-alphabet.html)
- [VHF radio procedure](../run-the-boat/vhf-radio-procedure.html)
- [GMDSS and DSC](../run-the-boat/gmdss-and-dsc.html)
