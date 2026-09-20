# Cost-Grounded Mobility Pricing (CGMP)

**CGMP** is an open framework for ride-hailing fare design.

Its central idea is simple:

> Price ordinary transport from measurable vehicle use and driver time; use competitive price discovery only when the ordinary price cannot clear the market.

CGMP is intended as a transparent alternative to opaque, continuously supply-demand-driven surge pricing. It separates the normal fare from the exceptional market-clearing mechanism.

## Status

**Version:** v1.0-preprint  
**Stage:** design preprint; simulation and live-pilot validation pending  
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
5. **Passengers can pre-authorize pickup distance/cost limits; requests outside those saved limits require explicit approval before dispatch.**
6. **Exceptional long-distance displacement charges are calculated and shown before the trip is accepted.**
7. **Efficient vehicles retain their efficiency advantage.** Passenger tariffs are based on service class rather than individual powertrain.
8. **When the published baseline does not attract a driver, the system uses a sealed fallback rather than an automatic surge multiplier.**
9. **The passenger's maximum price is private. Driver offers are private. The first valid offer within the passenger's ceiling clears the trip immediately.**
10. **Drivers can configure automatic private bidding rules while parked, avoiding manual numerical bidding while driving.**
11. **Fare-critical route, time and distance data should be computed or validated server-side.**

## Fast market-clearing fallback

Normal dispatch happens first at the published baseline.

If no driver accepts:

1. the passenger may use a saved private maximum total fare or set one for that request;
2. eligible driver apps evaluate the request using private, preconfigured bidding rules;
3. driver rules may consider pickup ETA, pickup distance, trip distance, expected trip duration, road/terrain conditions, destination, time of day and the driver's own minimum acceptable economics;
4. drivers do not see the passenger maximum;
5. drivers do not see competing offers;
6. the first server-valid offer satisfying `baseline <= bid <= passenger maximum` immediately clears the trip;
7. if no offer qualifies, no match occurs unless the passenger voluntarily changes the ceiling.

The objective is **fast market clearing within a passenger-chosen affordability limit**, not waiting for an auction window to find the mathematically lowest offer.

To reduce dispatch bias, an implementation should send a fallback request to the relevant candidate group at effectively the same dispatch epoch and use authoritative server receipt/order rules.

## Automated preferences

### Driver side

Drivers should be able to configure private bidding preferences during signup or while parked. The app can then submit qualifying fallback offers automatically without requiring the driver to type a price while operating the vehicle.

A production implementation should not require manual numerical bidding from a moving driver.

### Passenger side

Passengers should be able to configure standing pickup authorization using variables such as:

- maximum pickup distance;
- maximum pickup cost.

For example, a passenger may authorize pickup automatically when both the distance and cost are within their saved limits. The app should still disclose the actual pickup distance and charge.

The same principle can be used for a saved private fallback ceiling if the passenger chooses to enable it.

## Pickup policy

Pickup distance is charged at the normal class Rs/km rate.

In the v1.0-draft policy:

- a default pickup consent threshold may be configured by the deployment;
- the reference modelling threshold is **2 km**;
- passengers may set their own standing auto-approval limits based on pickup distance and/or pickup cost;
- if the requested pickup falls within those saved limits, separate interaction is unnecessary;
- if it falls outside the saved limits, explicit passenger approval is required before dispatch;
- pickup time is not separately charged;
- route distance should be determined from a reasonable server-calculated route and frozen at dispatch/acceptance according to implementation policy.

Standing preferences are intended to preserve informed consent without adding a confirmation screen to every qualifying request.

## Long-distance policy

CGMP does not guarantee a driver a profitable round trip.

The baseline should compensate the outbound trip fairly. Where the trip creates unavoidable displacement—such as a destination/time combination that makes an immediate safe return unreasonable—a pre-trip provision may cover necessary accommodation, meals, tolls or other defined displacement costs.

The passenger must see and agree to the rule-derived amount before the trip, either directly or through an applicable pre-authorized rule.

CGMP does **not** automatically compensate hypothetical future wages or guarantee full empty-return economics.

## Manipulation resistance

CGMP aims to reduce discretionary pricing surfaces:

- published rates and parameter history;
- server-side route/distance/time validation;
- private sealed driver offers;
- hidden passenger ceiling;
- first-qualifying server-side clearing;
- pre-authorized or explicit consent for exceptional charges;
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

## Preprint

A publication-oriented design preprint with literature review and references is available in [preprint/CGMP-v1.0-preprint.md](preprint/CGMP-v1.0-preprint.md).

The accompanying [Zenodo submission metadata](preprint/ZENODO_SUBMISSION.md) is prepared for a Publication / Preprint deposit.

## Licensing

The software/reference implementation is licensed under **Apache License 2.0**.

Unless a file states otherwise, the written specification, white paper, diagrams and documentation are made available under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

See [LICENSING.md](docs/LICENSING.md).

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff).

## Contributions and implementations

Independent research, criticism, recalibration, simulations and commercial implementations are welcome subject to the applicable licenses.

Implementations should not market themselves as empirically validated CGMP deployments unless they publish sufficient evidence for the claim.
