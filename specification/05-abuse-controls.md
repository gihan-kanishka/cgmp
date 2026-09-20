# Integrity and Monitoring Controls - v1.2

CGMP v1.2 prefers measurement over speculative rule accumulation.

## Server-authoritative inputs

Where practical, the platform should validate:

- pickup route and distance;
- passenger-trip route and distance;
- passenger-trip start/end timestamps;
- trip state;
- vehicle class;
- search stage and passenger authorization;
- long-distance provision;
- fallback eligibility;
- fallback offer order.

## Trip-time integrity

The time charge applies only to the passenger-trip interval.

Potential anomalies such as unexplained stops, route stretching, repeated excessive duration or impossible timestamps should be flagged for review.

A single unusual trip is not sufficient evidence of manipulation.

## Search integrity

Record each search stage and authorization so total matching delay can be measured from **initial request creation**, not only from fallback activation.

## Strategic rejection

v1.2 does not automatically bar a driver who rejected the deterministic request from later fallback participation.

Instead, measure:

- deterministic rejection;
- later participation on the same request;
- repeated reject-then-premium patterns;
- area/time clustering.

A same-request exclusion rule may be tested later if evidence shows material gaming.

## Post-acceptance cancellation and multi-homing

Drivers may use multiple platforms. A driver can therefore accept a CGMP request and later cancel if another opportunity becomes more attractive.

v1.2 does not add a platform-exclusivity rule. Instead, measure:

- post-acceptance driver cancellation rate;
- time from acceptance to driver cancellation;
- repeated cancellation patterns by driver, area and time;
- whether cancellations are concentrated in Stage 2 or Stage 3;
- passenger rematch and abandonment after driver cancellation.

These metrics can reveal reliability problems consistent with multi-homing without assuming the cause of every cancellation.

## First-qualifying latency

Use an authoritative server ordering rule and measure the relationship between network/device latency and fallback wins.

No latency correction is part of the v1.2 reference mechanism unless evidence shows material bias.

## Competitive-calibration integrity

Competitive headroom changes must be:

- scheduled rather than real-time;
- based on standardized ordinary/non-scarcity competitor observations;
- versioned;
- auditable;
- constrained by the economic floor.

## Publication principle

Adverse findings should be retained and reported. Monitoring is useful only if the project is willing to change the design when evidence contradicts its assumptions.
