# Cost-Grounded Mobility Pricing (CGMP)

**CGMP** is an open framework for ride-hailing fare design.

Its central idea is simple:

> Price ordinary transport from measurable vehicle use and driver time; use competitive price discovery only when the ordinary price cannot clear the market.

CGMP is intended as a transparent alternative to opaque, continuously supply-demand-driven surge pricing. It separates the normal fare from the exceptional market-clearing mechanism.

## Status

**Version:** v1.0-draft  
**Stage:** design and simulation  
**Evidence status:** not yet validated by a live controlled pilot

The numerical values in this repository are working assumptions for modelling. They are not claims that the listed values are universally correct. A production deployment should recalibrate them using local fleet, maintenance, energy, demand and trip data.

## Core architecture

A normal trip is priced using published inputs:

```text
normal fare =
    pickup distance charge
  + passenger-trip distance charge
  + passenger-trip time charge
  + pre-agreed necessary long-distance displacement provision
```

CGMP v1.0-draft uses the following Sri Lanka-oriented modelling parameters:

| Vehicle class | Distance rate |
|---|---:|
| Bike | Rs 30/km |
| Tuk | Rs 40/km |
| Mini | Rs 50/km |
| Compact | Rs 52.50/km |
| Sedan | Rs 55/km |

Common passenger-trip time rate: **Rs 12/minute**  
Illustrative platform commission: **7%**

These are configurable parameters, not immutable parts of the framework.

## Design principles

1. **Distance pays for the vehicle and its risks; time pays for the human.**
2. **Ordinary fares are cost-grounded, not automatically surge-multiplied by scarcity.**
3. **Traffic can increase a fare because it consumes more driver time, and the app should explain that cause explicitly.**
4. **Pickup distance is paid at the vehicle-class distance rate.**
5. **Pickup above the configured consent threshold requires passenger approval before dispatch.**
6. **Exceptional long-distance displacement charges are calculated and shown before the trip is accepted.**
7. **Efficient vehicles retain their efficiency advantage.** Passenger tariffs are based on service class rather than individual powertrain.
8. **When the published baseline does not attract a driver, the system uses a sealed-bid fallback rather than an automatic surge multiplier.**
9. **The passenger's maximum price is private. Driver bids are private. The lowest qualifying bid wins.**
10. **Fare-critical route, time and distance data should be computed or validated server-side.**

## Market-clearing fallback

Normal dispatch happens first at the published baseline.

If no driver accepts:

1. the passenger may set a private maximum total fare;
2. eligible drivers receive the trip details and submit private bids;
3. drivers do not see the passenger maximum;
4. drivers do not see competing bids;
5. the system chooses the lowest valid bid that does not exceed the passenger maximum;
6. if no bid qualifies, no match occurs unless the passenger voluntarily changes the ceiling.

This makes scarcity a market-discovered exception rather than a platform-imposed multiplier applied to every trip.

## Pickup policy

Pickup distance is charged at the normal class Rs/km rate.

In the v1.0-draft policy:

- pickup up to **2 km** may be incorporated automatically into the quoted fare;
- pickup above **2 km** requires explicit passenger approval before dispatch;
- pickup time is not separately charged;
- route distance should be determined from a reasonable server-calculated route and frozen at dispatch/acceptance according to implementation policy.

## Long-distance policy

CGMP does not guarantee a driver a profitable round trip.

The baseline should compensate the outbound trip fairly. Where the trip creates unavoidable displacement—such as a destination/time combination that makes an immediate safe return unreasonable—a pre-trip provision may cover necessary accommodation, meals, tolls or other defined displacement costs.

The passenger must see and agree to the rule-derived amount before the trip.

CGMP does **not** automatically compensate hypothetical future wages or guarantee full empty-return economics.

## Manipulation resistance

CGMP aims to reduce discretionary pricing surfaces:

- published rates and parameter history;
- server-side route/distance/time validation;
- private sealed bids;
- hidden passenger ceiling;
- lowest qualifying bid selection;
- pre-trip consent for exceptional charges;
- telemetry-assisted review of repeated route stretching, deliberate crawling or repeated speeding;
- two-sided review so unsupported chronic complaints can also be detected.

The framework should be described as **manipulation-resistant**, not manipulation-proof.

## Safety hypothesis

Time compensation may reduce the economic pressure to maximize kilometres travelled per working hour, because congestion and lawful journey time are no longer entirely uncompensated.

This is a **testable hypothesis**, not a proven safety outcome. A pilot should measure speeding events, complaints, excess journey time, cancellations, driver net earnings and passenger fares against a control system.

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
└── whitepaper/
    └── CGMP-v1.0-draft.md
```

## Licensing

The software/reference implementation is licensed under **Apache License 2.0**.

Unless a file states otherwise, the written specification, white paper, diagrams and documentation are made available under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

See [LICENSING.md](docs/LICENSING.md).

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff).

## Contributions and implementations

Independent research, criticism, recalibration, simulations and commercial implementations are welcome subject to the applicable licenses.

Implementations should not market themselves as empirically validated CGMP deployments unless they publish sufficient evidence for the claim.
