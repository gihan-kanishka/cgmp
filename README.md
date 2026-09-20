# Cost-Grounded Mobility Pricing (CGMP)

**CGMP** is an open framework for transparent ride-hailing fare calibration and exceptional dispatch.

> Costs set the economic floor; competition may tune the margin above that floor; scarcity pricing is reserved for trips that fail deterministic dispatch.

## Status

**Version:** v1.1-preprint  
**Date:** 2026-09-20  
**Stage:** design preprint; simulation and live-pilot validation pending  
**Evidence status:** not yet validated by a live controlled pilot

All numerical values below are current modelling assumptions. Production deployment requires local fleet, platform-cost, trip and competitor-fare data.

## Current reference calibration

Passenger-facing rates are grossed up for a **7% platform commission**.

| Class | Representative ICE routine cost/km | Current target net vehicle headroom/km | Passenger distance rate |
|---|---:|---:|---:|
| Bike | Rs 14.50 | Rs 3 | **Rs 19.00/km** |
| Tuk | Rs 22.10 | Rs 12 | **Rs 37.00/km** |
| Mini | Rs 32.80 | Rs 15 | **Rs 51.50/km** |
| Compact | Rs 34.00 | Rs 15 | **Rs 53.00/km** |
| Sedan | Rs 36.10 | Rs 21 | **Rs 61.50/km** |

Passenger time rate: **Rs 12.90/minute**, yielding approximately **Rs 12.00/minute net to the driver after 7% commission**.

The current class headrooms are competitive calibration targets, not immutable constants. They may be adjusted against observed competitor passenger fares, but the underlying economic floor must not be crossed.

## Calibration rule

For vehicle class `c`:

```text
passenger_distance_rate_c =
    (representative_ICE_routine_cost_c + target_net_vehicle_headroom_c)
    / (1 - commission_rate)
```

The published rate may be rounded upward to a transparent billing increment.

For labour:

```text
passenger_time_rate =
    target_net_driver_labour_per_minute / (1 - commission_rate)
```

Current labour target: **Rs 12 net/minute**.

EVs and unusually efficient vehicles do **not** set the passenger tariff. CGMP calibrates the class rate from representative ICE economics; owners of more efficient vehicles retain their efficiency advantage.

## Minimum fare and pickup

The current reference policy is:

- minimum passenger-trip distance charged: **2 km**;
- initial pickup/search allowance: **2 km**;
- pickup time: **not charged**;
- search expansion: **2 km increments**;
- pickup beyond 2 km: charged at the **actual authorized pickup distance**, not the full search-band ceiling.

The ordinary fare is:

```text
F =
  [max(passenger_trip_km, 2) + max(actual_pickup_km, 2)] * class_rate
  + verified_passenger_trip_minutes * 12.90
  + pre-agreed_long_distance_provision
```

For a very short trip, the minimum distance component therefore represents **2 km passenger travel + 2 km pickup**.

## Dispatch architecture

### Stage 1 - normal nearby search

Search eligible drivers within **0-2 km** at the deterministic CGMP fare. No additional passenger confirmation is required for the included pickup band.

### Stage 2 - passenger-authorized expanded search

If no match is obtained, expand in **2 km increments**:

```text
0-2 km -> 2-4 km -> 4-6 km -> 6-8 km -> ...
```

The passenger can approve each expansion with one click or save standing preferences such as:

- automatically expand up to a chosen radius;
- maximum pickup cost;
- maximum pickup distance.

Expanded pickup is still deterministic CGMP pricing. **No bidding occurs merely because the search radius expanded.**

### Stage 3 - exceptional sealed dispatch

Sealed bidding is enabled only after the passenger-authorized deterministic expanded-search process fails to obtain a vehicle.

The passenger can define a private maximum willingness-to-pay allowance using:

- a percentage above the deterministic base fare;
- a fixed additional amount per passenger-trip kilometre;
- a fixed additional fee by trip-distance band.

The platform does not expose this ceiling to drivers.

Drivers configure private automatic fallback rules while parked. The first server-valid qualifying offer inside the passenger ceiling clears immediately.

```text
baseline <= first qualifying offer <= passenger ceiling
```

The fallback is intended to be exceptional. A high fallback-activation rate is a signal to investigate fare calibration, supply conditions or strategic rejection.

## Competitive calibration and the hard floor

CGMP may compare standardized benchmark trips with competitor platforms and tune the **vehicle headroom** to keep passenger fares commercially attractive.

Competition is not allowed to push the tariff below the economic floor:

```text
actual published rate =
    max(economic-floor rate, competitively calibrated rate)
```

The hard floor protects:

- representative ICE routine operating cost;
- the published net driver-labour target;
- the transparent commission required by the platform.

The current 7% commission is a working business parameter and should be validated against payments, maps, support, fraud, communications, engineering, compliance and dispute-resolution costs.

## Reference examples

At the **25 km/h reference speed**, Rs 12.90/min is equivalent to **Rs 30.96 per passenger-trip km** of time compensation.

Effective passenger-trip rate at that reference speed, before pickup:

| Class | Distance component/km | Time equivalent/km | Effective trip rate/km |
|---|---:|---:|---:|
| Bike | Rs 19.00 | Rs 30.96 | **Rs 49.96** |
| Tuk | Rs 37.00 | Rs 30.96 | **Rs 67.96** |
| Mini | Rs 51.50 | Rs 30.96 | **Rs 82.46** |
| Compact | Rs 53.00 | Rs 30.96 | **Rs 83.96** |
| Sedan | Rs 61.50 | Rs 30.96 | **Rs 92.46** |

A **13 km trip + 2 km pickup** at the same 25 km/h reference trip speed (31.2 passenger minutes) gives:

| Class | Estimated passenger fare |
|---|---:|
| Bike | **Rs 687.48** |
| Tuk | **Rs 957.48** |
| Mini | **Rs 1,174.98** |
| Compact | **Rs 1,197.48** |
| Sedan | **Rs 1,324.98** |

These are estimates for comparison. Production fares use verified legitimate trip time.

## Design principles

1. **Distance pays for the vehicle; time pays for the human.**
2. **Economic floors are protected before competitive tuning.**
3. **Ordinary and expanded-search fares remain deterministic.**
4. **Search radius and billing distance are separate:** search expands by bands, billing uses actual authorized pickup distance.
5. **Scarcity price discovery is a last-resort mechanism, not a normal fare multiplier.**
6. **Passengers control their private fallback affordability ceiling.**
7. **Drivers control their private automated willingness-to-serve rules.**
8. **Efficient drivetrains retain their savings; ICE class economics set the tariff benchmark.**
9. **Fare-critical route, time, distance and fallback ordering should be server authoritative.**
10. **Safety, strategic rejection, latency fairness and economic sustainability are empirical questions for simulation and pilots.**

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
│   └── ZENODO_SUBMISSION.md
└── whitepaper/
    └── CGMP-v1.0-draft.md
```

## Project attribution

**Formal creator:** CGMP Project  
**Project maintainer / publication custodian:** gihan-kanishka  
**AI assistance:** OpenAI ChatGPT (GPT-5.6 Sol)

CGMP was developed through iterative human-AI collaboration. OpenAI ChatGPT was used extensively for formalization, analysis, literature synthesis, reference-code development, documentation and manuscript drafting. Human contribution included conceptual direction, requirements, design decisions, review and authorization of the public release.

The AI system is not an author and cannot assume responsibility for the work. Publication responsibility remains with the human project maintainer. For citation purposes, use **CGMP Project** as the creator.

## Preprint

The current publication-oriented source is [preprint/CGMP-v1.1-preprint.md](preprint/CGMP-v1.1-preprint.md).

Zenodo metadata is maintained in [preprint/ZENODO_SUBMISSION.md](preprint/ZENODO_SUBMISSION.md).

## Licensing

Reference software: **Apache License 2.0**.  
Documentation/specification/preprint unless otherwise stated: **CC BY 4.0**.

See [LICENSING.md](docs/LICENSING.md).
