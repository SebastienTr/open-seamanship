---
title: Engine overheating
summary: Temperature alarm, a high gauge, or steam and little water from the exhaust on a marine diesel. Cut the load, then check water flow from seacock to exhaust.
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
  - id: navpers-engineman-1957
    locator: "Engineman 3 (NAVPERS 10539): ch. 13, 'Pressures and temperatures', pp. 459-461; expansion-tank level and 'cold water should never be added until the engine has cooled', p. 468; precaution 'Water', p. 471; ch. 14, 'Care of zincs' (close sea connections before opening the sea-water side), p. 501; 'Cleaning of heat exchangers', pp. 503-504; ch. 15, 'Centrifugal pumps', insufficient discharge, clogged strainers, discharge obstructions, broken shaft, running dry, pp. 523-529"
  - id: tm-9-2815-252-24-dn2m
    locator: "Table 3-2 'Troubleshooting', malfunction 7 'Engine overheating', pp. 3-7 to 3-8"
  - id: tm-9-2815-254-24-isuzu-c240
    locator: "Table 3-2 'Troubleshooting', malfunction 7 'Engine overheating', p. 3-6"
  - id: navedtra-engineman-3-2-1979
    locator: "Ch. 13 'Troubleshooting': instruments, p. 260; thermostat test and 'check these items before removing a thermostatic control unit', p. 272; 'Obstruction in the exhaust system', pp. 272-273"
  - id: navedtra-construction-mechanic-3-2-1978
    locator: "Ch. 5 'Cooling and lubricating systems', 'Radiator pressure cap', caution on removing the cap, p. 126"
  - id: fm-55-501-marine-crewman
    locator: "Ch. 14, para 14-6 (check sea-water strainers and discharge when beaching), p. 14-4; para 14-14 (overheating or poor sea-water discharge when aground), p. 14-7"
uncertain:
  - "Normal temperatures are in your engine's manual. The only figures in the sources are a 1957 Navy rule for large engines when no maker's figure is available: fresh water leaving the engine 60 to 77 °C (140 to 170 °F), sea water at the discharge below 54 °C (130 °F). They may not suit a small yacht diesel."
  - "The Navy manuals describe bronze centrifugal sea-water pumps. Most small marine diesels use a rubber (flexible-vane) impeller pump. The checks are the same in principle; the impeller details are on the impeller page."
  - "Steam with little water at a wet exhaust outlet is a strong sign of lost raw-water flow on small boats. No cleared source states it in these words."
---

## Situation

The temperature alarm sounds, the gauge climbs above normal, or the exhaust
gives steam and little or no water. An engine that is not cooled properly can
suffer "extreme damage" to its block, liners and heads
([Engineman 3, p. 523](../library/navpers-engineman-1957.html)).

## Do now

1. **Cut the load at once.** Throttle back to idle. If you are clear of
   danger, stop the engine. If stopping would put you on rocks or in a
   channel, run at the lowest power that keeps you safe while someone gets the
   sails up or the anchor ready. See
   [Engine failure near danger](../emergency/engine-failure-near-danger.html).
   The Navy rule: when you cannot increase the cooling flow and temperatures
   are too high, stop the engine
   ([Engineman 3, p. 471](../library/navpers-engineman-1957.html)).
2. **Do not open a hot pressure cap.** On a heat-exchanger engine, wait until
   the engine has cooled before opening the header tank cap. Steam and coolant
   can burn you badly ([Construction Mechanic 3 & 2, p. 126](../library/navedtra-construction-mechanic-3-2-1978.html)).
   Never pour cold water into a hot engine: it can crack the head or liners
   ([Engineman 3, pp. 468 and 471](../library/navpers-engineman-1957.html)).
3. **Look at the exhaust.** On a wet-exhaust boat, a weak or missing water
   stream means the raw-water side is the problem: work through steps 4 to 8.
   If the water flow looks normal, go to step 9 and then "If that fails".
4. **Raw-water seacock.** Is it fully open? Was it closed for a job and
   forgotten?
5. **Raw-water strainer.** With the engine stopped (running it with the
   seacock shut destroys the impeller), close the seacock first, then open the strainer and
   clear weed, plastic, shells or sand. Clogged strainers are "most often the
   source of the trouble" ([Engineman 3, p. 524](../library/navpers-engineman-1957.html)).
   Refit it so it seals, open the seacock.
6. **Something over the intake.** A plastic bag or weed over the hull inlet
   gives the same symptom. In shallow water or aground, sand and mud get drawn
   in ([FM 55-501, paras 14-6 and 14-14](../library/fm-55-501-marine-crewman.html)).
7. **Pump drive.** With the engine stopped, if the raw-water pump is
   belt-driven, check the belt is there and tight. A broken pump shaft also stops the flow
   ([Engineman 3, p. 525](../library/navpers-engineman-1957.html)).
8. **Impeller.** If water reaches the pump but does not come out, the
   impeller has probably failed. See
   [Changing a raw-water pump impeller](changing-a-raw-water-impeller.html).
9. **Coolant level (heat-exchanger engines), once cool.** If low, look for the
   leak before refilling ([TM 9-2815-252-24, malfunction 7, step 1](../library/tm-9-2815-252-24-dn2m.html)).

Restart only when you have found a cause. Then watch the gauge and the
exhaust water closely.

## Why

On most small marine diesels, a pump draws sea water through a seacock and a
strainer. It cools the engine directly (raw-water cooling) or cools a closed
fresh-water circuit in a heat exchanger. Then it is mixed into the exhaust.
Anything that cuts the sea-water flow shows first as rising temperature
([Engineman 3, p. 523](../library/navpers-engineman-1957.html)). See
[Diesel cooling systems](../know-your-boat/diesel-cooling-systems.html).

Slow overheating over weeks is different from sudden overheating. Scale, weed
or old impeller pieces in the heat-exchanger tubes give a *gradual* rise in
temperature ([Engineman 3, pp. 503-504](../library/navpers-engineman-1957.html)).

## Check that it worked

- A strong, steady stream of water from the exhaust within seconds of
  starting.
- The temperature gauge comes back to its normal reading and stays there under
  load.

## If that fails

Work through the next causes, in this order:

1. **The gauge or sender may be wrong.** Compare with the other signs
   (exhaust water, steam, a hot smell) before you take things apart
   ([Engineman 3 & 2, pp. 260 and 272](../library/navedtra-engineman-3-2-1979.html)).
2. **Thermostat stuck.** Both Army tables put the thermostat next, after the
   coolant level ([TM 9-2815-254-24, malfunction 7](../library/tm-9-2815-254-24-isuzu-c240.html)).
   It can be tested in a pan of heated water with a thermometer
   ([Engineman 3 & 2, p. 272](../library/navedtra-engineman-3-2-1979.html)).
3. **Heat exchanger blocked** with scale, weed or rubber from an old impeller.
   Close the seacocks before you open the sea-water side, or you may flood the
   boat ([Engineman 3, p. 501](../library/navpers-engineman-1957.html)).
4. **Fresh-water (coolant) pump** worn or its belt slipping
   ([TM 9-2815-252-24, malfunction 7, step 3](../library/tm-9-2815-252-24-dn2m.html)).
5. **Overload.** A fouled propeller or a dirty hull makes the engine work
   harder and run hot ([Engineman 3, p. 459](../library/navpers-engineman-1957.html)).
   See [Rope or net round the propeller](fouled-propeller.html).
6. **Blocked exhaust** (silencer, mixing elbow) raises exhaust temperature and
   cuts power ([Engineman 3 & 2, pp. 272-273](../library/navedtra-engineman-3-2-1979.html)).
7. **Injection timing** is the last item in both Army tables: a job for a
   mechanic ([TM 9-2815-252-24, malfunction 7, step 4](../library/tm-9-2815-252-24-dn2m.html)).

**Larger engines.** A steadily rising difference between inlet and outlet
pressure across a cooler shows that it is clogging; the sea-water strainer,
over-greased sea-water pump bearings and oil leaking from an oil cooler can
all foul cooler tubes ([Engineman 3, pp. 503-504](../library/navpers-engineman-1957.html)).

If you saw milky oil after overheating, see [Low oil pressure alarm](low-oil-pressure.html).
