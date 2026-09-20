# Cost-Grounded Mobility Pricing (CGMP)

**CGMP** is an open framework for transparent ride-hailing fare calibration and exceptional dispatch.

> Costs set the economic floor; competition may tune the margin above that floor; scarcity price discovery is reserved for trips that fail deterministic dispatch.

## Status

**Version:** v1.2-preprint  
**Date:** 2026-09-20  
**Stage:** design preprint; strategic simulation and live-pilot validation pending  
**Evidence status:** not yet validated by a live controlled pilot

v1.2 deliberately keeps the operational core small. Potential behavioral problems are measured before new pricing rules are added.

## Current reference calibration

Passenger-facing rates are grossed up for a **7% platform commission**.

| Class | Representative ICE routine cost/km | Current target net vehicle headroom/km | Passenger distance rate |
|---|---:|---:|---:|
| Bike | Rs 14.50 | Rs 3 | **Rs 19.00/km** |
| Tuk | Rs 22.10 | Rs 12 | **Rs 37.00/km** |
| Mini | Rs 32.80 | Rs 15 | **Rs 51.50/km** |
| Compact | Rs 34.00 | Rs 15 | **Rs 53.00/km** |
| Sedan | Rs 36.10 | Rs 21 | **Rs 61.50/km** |

Passenger-trip time rate: **Rs 12.90/minute**, yielding approximately **Rs 12.00/minute net to the driver after 7% commission**.

The current routine ICE cost figures are provisional aggregate modelling assumptions. A production calibration must publish the dated component inputs used to derive them.

## Core fare

```text
F =
  [max(passenger_trip_km, 2) + max(actual_pickup_km, 2)] * class_rate
  + verified_passenger_trip_minutes * 12.90
  + pre-agreed_long_distance_provision
```

Reference policy:

- minimum passenger-trip distance: **2 km**;
- included initial pickup/search distance: **2 km**;
- pickup time: **not charged**;
- search expansion: **2 km increments**;
- expanded pickup: billed at actual authorized distance, not the search-band ceiling.

### Why pickup time is not charged

Pickup time is intentionally not monetized in v1.2. Before the ride starts, the passenger already bears the service cost of waiting for the vehicle. CGMP compensates the vehicle movement through the pickup-distance charge but does not add a second passenger charge for pickup minutes.

Whether this reduces driver acceptance of distant pickups is a **pilot metric**, not a reason to add another tariff component before evidence exists.

## ICE cost calibration

The class cost input should ultimately be derived from dated, auditable ICE operating-cost components such as:

```text
routine_ICE_cost_per_km =
    fuel_cost_per_km
  + tyres_per_km
  + scheduled_service_per_km
  + brakes_suspension_repairs_per_km
  + other_defined_routine_wear_per_km
```

The repository does **not** invent a component breakdown for the current provisional aggregate figures. That empirical breakdown is required before production deployment.

EV and unusually efficient vehicle costs do not set the passenger tariff. Their owners retain the efficiency saving.

## Competitive calibration

Class-specific vehicle headroom is a competitive tuning variable **above the economic floor**.

Competitive recalibration must be:

- **periodic and scheduled**, not real-time;
- based on standardized comparable **ordinary/non-scarcity competitor fares**;
- versioned and auditable;
- prohibited from pushing the tariff below the economic floor.

CGMP therefore does not use competitor surge observations as an input to immediate fare changes.

## Trip-time measurement

The reference fare is metered on legitimate passenger-trip time.

- billable time begins when the passenger trip starts after pickup;
- billable time ends when the passenger trip ends;
- pickup time is excluded;
- server timestamps, route/GPS data and trip state are used to validate the interval;
- implausible or disputed intervals are flagged for review rather than silently accepted.

An upfront fare shown before acceptance is an **estimate** based on expected route and time. The final v1.2 reference fare uses verified actual passenger-trip time. A deployment that legally or commercially guarantees a fixed upfront price is a documented implementation variant.

CGMP therefore claims **no automatic scarcity multiplier**, not "no multiplier of any kind": congestion can increase the fare because it increases legitimate paid trip time.

## Dispatch architecture

### Stage 1 - deterministic nearby search

Search eligible drivers within **0-2 km** at the published CGMP fare.

### Stage 2 - passenger-authorized deterministic expansion

If unmatched, expand in **2 km increments**:

```text
0-2 km -> 2-4 km -> 4-6 km -> 6-8 km -> ...
```

The passenger can approve expansion directly or save automatic limits.

No bidding occurs during Stage 2.

### Stage 3 - exceptional sealed fallback

Only after authorized deterministic expanded search fails may the request enter sealed fallback.

For candidate driver `i`:

- `F0_i` = gross passenger-facing deterministic fare using that driver's actual authorized pickup;
- `M_i` = private passenger maximum produced by the passenger's saved/selected ceiling rule applied to `F0_i`;
- `b_i` = gross passenger-facing fallback offer.

A valid offer satisfies:

```text
F0_i <= b_i <= M_i
```

The first server-valid qualifying offer clears immediately.

No automatic rejecter ban, premium cap, latency correction or alternative auction window is part of the v1.2 core. Those are possible controls only if simulation or pilot evidence shows a material problem.

## Commission treatment

The **7% commission applies to commissionable passenger fare**, including:

- distance charges;
- passenger-trip time charges;
- any fallback premium.

Direct third-party/pass-through expenses such as an actual toll or explicitly reimbursed accommodation cost may be designated **commission-exempt**. They must be separately identified in the fare breakdown.

## What is monitored instead of over-engineered

v1.2 measures before adding corrective rules:

- deterministic acceptance/rejection;
- acceptance by pickup-distance band;
- total request-to-match time;
- passenger abandonment at each stage;
- fallback activation rate;
- fallback premium distribution;
- proximity of clearing offers to passenger ceilings;
- repeated reject-then-fallback participation;
- device/network latency versus fallback win rate;
- driver net earnings and utilization;
- platform sustainability at 7%;
- speeding/aggressive-driving indicators;
- unexplained excess journey time.

## Reference examples

At **25 km/h**, Rs 12.90/min is equivalent to **Rs 30.96 per passenger-trip km**.

| Class | Distance component/km | Time equivalent/km | Effective trip rate/km |
|---|---:|---:|---:|
| Bike | Rs 19.00 | Rs 30.96 | **Rs 49.96** |
| Tuk | Rs 37.00 | Rs 30.96 | **Rs 67.96** |
| Mini | Rs 51.50 | Rs 30.96 | **Rs 82.46** |
| Compact | Rs 53.00 | Rs 30.96 | **Rs 83.96** |
| Sedan | Rs 61.50 | Rs 30.96 | **Rs 92.46** |

For a **13 km trip + 2 km pickup** at the same 25 km/h reference trip speed:

| Class | Estimated passenger fare |
|---|---:|
| Bike | **Rs 687.48** |
| Tuk | **Rs 957.48** |
| Mini | **Rs 1,174.98** |
| Compact | **Rs 1,197.48** |
| Sedan | **Rs 1,324.98** |

The 25 km/h figure is an estimation benchmark, not a production pricing speed.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── LICENSE-DOCS.md
├── NOTICE
├── CITATION.cff
├── CHANGELOG.md
├── config/
│   └── cgmp-v1.example.json
├── docs/
│   ├── EVIDENCE_AND_VALIDATION.md
│   └── LICENSING.md
├── specification/
│   ├── 01-core-fare.md
│   ├── 02-pickup-policy.md
│   ├── 03-long-distance.md
│   ├── 04-sealed-bidding.md
│   └── 05-abuse-controls.md
├── simulator/
│   └── cgmp.py
├── tests/
│   └── test_cgmp.py
├── preprint/
│   ├── CGMP-v1.0-preprint.md
│   ├── CGMP-v1.1-preprint.md
│   ├── CGMP-v1.2-preprint.md
│   └── ZENODO_SUBMISSION.md
└── whitepaper/
    ├── CGMP-v1.0-draft.md
    ├── CGMP-v1.1-draft.md
    └── CGMP-v1.2-draft.md
```

## Project attribution

**Formal creator:** CGMP Project  
**Project maintainer / publication custodian:** gihan-kanishka  
**AI assistance:** OpenAI ChatGPT (GPT-5.6 Sol)

## Preprint

The current publication-oriented source is [preprint/CGMP-v1.2-preprint.md](preprint/CGMP-v1.2-preprint.md).

Reference software is licensed under **Apache License 2.0**. Documentation/specification/preprint unless otherwise stated is **CC BY 4.0**.
