---
title: "Mayday: calling for help"
summary: Send a DSC distress alert and a Mayday call on VHF channel 16, word for word, and what to do if no one answers.
kind: card
section: emergency
region: international
language: en
licence: CC-BY-SA-4.0
safety: critical
status: draft
authors: [claude]
reviewers: []
reviewed: null
sources:
  - id: mca-gmdss-small-boat-procedures
    locator: "'GMDSS VHF DSC procedures for small boat users', sections 'Distress alert' (DSC alert, then call and message on channel 16 after acknowledgement or about 15 seconds), 'Distress alert acknowledgement' and 'Urgency' (Pan-Pan format)"
  - id: nga-pub102
    locator: "chapter 4, section 3, Radiotelephone procedures: meaning of MAYDAY, PAN and SECURITE; distress call and distress message; plain language; letters with the phonetic alphabet and numbers figure by figure, p. 147; table 1, p. 148"
  - id: nga-pub-117-2014
    locator: "chapter 4, 400D (channel 16 distress, safety and calling; channel 70 DSC only), pp. 4-5 to 4-6; 400E (DSC distress channels; alert carries position and UTC time; connect GPS to the DSC radio), p. 4-10; 400H (cancelling an inadvertent distress alert, from IMO Resolution A.814(19)), p. 4-16; chapter 5, 500A (Pan-Pan call format with position), p. 5-3"
  - id: fm-55-501-marine-crewman
    locator: "chapter 9, paras 9-69 to 9-72 (distress call and message; repeat until answered; any frequency if no answer), p. 9-23; paras 9-95 to 9-98 (2182 kHz and channel 16; position as lat/long or bearing and distance from a widely known point, not local names; persons aboard, boat description), pp. 9-28 to 9-29"
  - id: wikipedia-en
    locator: "'Mayday', sections 'Mayday calls' (false distress calls are an offence in many countries) and 'Silencing other communications traffic' (Seelonce Mayday, Seelonce Feenee)"
uncertain:
  - "How long to hold the DSC distress button differs between radios (often about 3 to 5 seconds). Hold it until the screen says the alert has been sent; check your own radio's label before you need it."
  - "The 2003 International Code of Signals (Pub. 102) still describes a two-tone alarm signal before the voice call. Modern VHF sets replace it with the DSC alert, so it is left out here."
  - "Not every coast station still listens on MF 2182 kHz: the US Coast Guard stopped in the 2010s (Pub. 117, 2014). Check for your area."
  - "National emergency phone numbers and whether a mobile phone call reaches the coastguard differ by country; they are given on the regional pages, not here."
---

## Situation

A boat or a person is in **grave and imminent danger** and needs help now:
sinking, fire you cannot control, person overboard, about to be wrecked, a
life-threatening injury. If help is needed but no life is in immediate
danger, send **Pan-Pan** instead (see *Why*).

## Do now

1. **Press the red DISTRESS button** on the DSC radio (lift the cover) and
    hold it until the radio says the alert is sent. If there are a few
    seconds, choose the type of distress first.
2. **Wait** for an acknowledgement, or about 15 seconds.
3. **Channel 16, high power.** Press the microphone button and say slowly:

    > **MAYDAY, MAYDAY, MAYDAY.**
    >
    > **This is** *boat name, boat name, boat name*, *call sign*, *MMSI*.
    >
    > **MAYDAY** *boat name, call sign, MMSI*.
    >
    > **My position is** *latitude and longitude* (or bearing and distance from a well-known point).
    >
    > *What is wrong*: sinking / on fire / person overboard.
    >
    > **I require immediate assistance.**
    >
    > *Number* **persons on board.**
    >
    > *Anything else*: abandoning to liferaft, injuries, boat colour and type.
    >
    > **OVER.**

4. **Release the button and listen.** No answer within a minute or two:
    send it again. Keep repeating until someone answers.
5. **Lifejackets on everyone** while you wait.
6. **Stay by the radio on channel 16.** Answer questions; do what the
    rescue centre says.

Spell names with the [phonetic alphabet](../tables/phonetic-alphabet.html).
Say numbers digit by digit.

## Why

The DSC alert sends your identity and GPS position automatically to coast
stations and ships ([MCA](../library/mca-gmdss-small-boat-procedures.html);
[Pub. 117, 400E](../library/nga-pub-117-2014.html)). The voice message
tells them what is wrong and how many people are at risk
([Pub. 102, p. 147](../library/nga-pub102.html)).

**Pan-Pan** (urgent, not life-threatening): *Pan-Pan* ×3, *all stations*
×3, *this is* boat name ×3, call sign, MMSI, then position, problem and
help needed, *over*. The coastguard may move you to a working channel
([MCA](../library/mca-gmdss-small-boat-procedures.html);
[Pub. 117, 500A](../library/nga-pub-117-2014.html);
[FM 55-501, 9-97](../library/fm-55-501-marine-crewman.html)).

## Check that it worked

- The radio shows the alert *acknowledged*, or a station says
  **"Received Mayday"**.
- When you hear **"Seelonce Mayday"**, the channel is kept for your
  emergency ([Wikipedia, 'Mayday'](../library/wikipedia-en.html)).

## If that fails

- No answer on 16: try any channel, or MF 2182 kHz
  ([FM 55-501, 9-72](../library/fm-55-501-marine-crewman.html)).
- Radio without GPS: say your position by voice, from a well-known point,
  never a local name ([FM 55-501, 9-98](../library/fm-55-501-marine-crewman.html)).
- Switch on the EPIRB or PLB; use [distress signals](distress-signals.html).
- National numbers: [France](../regions/france-search-and-rescue.html),
  [UK](../regions/uk-search-and-rescue.html).
- **Sent by mistake?** If it is still sending, switch the radio off. Then
  switch it on again, set channel 16 and say: *All stations* ×3,
  *this is* name, call sign, MMSI, position, *cancel my distress alert of*
  date, time UTC. An EPIRB set off by mistake: leave it on until you have
  told a coast station or rescue centre, then switch it off
  ([Pub. 117, 400H](../library/nga-pub-117-2014.html)).
