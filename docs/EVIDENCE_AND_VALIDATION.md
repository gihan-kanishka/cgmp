# Evidence and Validation Plan

CGMP v1.0-draft is a design framework, not a claim of proven superiority.

## Claims that are currently architectural

The following can be verified directly from the rules:

- normal fares are deterministic functions of published inputs;
- ordinary pricing does not require a supply-demand multiplier;
- pickup charges can be disclosed before dispatch;
- passengers can pre-authorize pickup distance/cost limits;
- long-distance provisions can be agreed before the trip;
- driver fallback offers can remain private;
- the passenger ceiling can remain private;
- the first qualifying sealed offer can clear immediately without waiting for an auction window.

## Claims that require empirical validation

A live pilot is required to determine whether CGMP:

- improves driver acceptance;
- reduces cancellations;
- improves driver net earnings after costs;
- keeps passenger fares competitive;
- reduces speeding or aggressive-driving complaints;
- creates deliberate slow-driving behaviour;
- improves long-distance trip completion;
- supports a sustainable platform at the chosen commission rate;
- produces acceptable fairness outcomes under first-qualifying dispatch;
- avoids material assignment bias from device/network latency.

## Recommended pilot design

Where operationally possible, use a randomized or carefully matched control design comparing the incumbent fare model with CGMP.

Pre-register primary metrics before evaluating outcomes.

Suggested metrics:

- passenger fare per trip and per km;
- driver net earnings per active hour after vehicle cost;
- acceptance rate;
- passenger cancellation rate;
- driver cancellation rate;
- time to match at normal baseline;
- time from fallback activation to assignment;
- share of trips clearing on the first qualifying fallback offer;
- distribution of fallback assignments across eligible drivers;
- relationship between measured network latency and fallback win rate;
- speeding events per 100 trips;
- speeding/aggressive-driving complaints per 1,000 trips;
- unexplained excess journey time;
- slow-driving complaints per 1,000 trips;
- pickup acceptance by pickup-distance band;
- percentage of pickups auto-authorized by standing passenger preferences;
- percentage of trips entering sealed fallback dispatch;
- fallback clearing premium relative to baseline;
- percentage of fallback requests that fail to clear;
- long-distance acceptance and completion rate.

## Calibration data

Before production use, collect market-specific data for:

- fuel and energy prices;
- real fleet fuel/energy economy;
- routine maintenance and wear per km;
- uninsured/irregular cost experience;
- fleet composition by vehicle class;
- trip-time distributions;
- pickup-distance distributions;
- long-distance route characteristics;
- driver utilization and idle time;
- platform operating costs;
- device/network latency distributions relevant to first-qualifying dispatch.

## Safety hypothesis

The design hypothesis is that explicit compensation for time reduces the financial penalty associated with lawful speeds and congestion.

This should not be described as a proven safety benefit until a controlled pilot produces supporting evidence.
