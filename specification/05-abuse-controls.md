# Abuse and Integrity Controls - v1.1

CGMP is designed to be manipulation-resistant, not manipulation-proof.

## Fare-critical data

Where feasible, the server should validate or calculate:

- legal/reasonable route geometry;
- pickup distance and search band;
- passenger-trip distance;
- passenger-trip timestamps;
- vehicle movement plausibility;
- vehicle class;
- long-distance eligibility;
- passenger authorization state;
- deterministic-search state;
- fallback activation state;
- authoritative fallback offer receipt/order.

Client telemetry is evidence, not sole authority.

## Time manipulation

The current fare explicitly compensates legitimate passenger-trip time.

A single slow trip is not evidence of abuse. Review should focus on repeated patterns such as:

- materially longer times than comparable trips;
- unnecessary detours;
- repeated supported passenger reports;
- unexplained divergence from reasonable route/time distributions.

The same system should detect repeated speeding/aggressive-driving patterns.

## Passenger complaint integrity

Passenger reports should trigger review rather than automatic guilt.

Chronic unsupported complaint patterns may themselves be flagged for verification.

> Reports establish patterns; objective trip data validates them.

## Search and pickup integrity

The platform should log:

- initial 0-2 km search;
- each 2 km expansion authorization;
- actual pickup distance;
- charged pickup distance;
- whether the authorization was interactive or a saved preference.

Search-band boundaries must never be used as billing distance when actual pickup is lower.

## Strategic rejection and fallback

Monitor:

- deterministic-offer rejection rates;
- fallback activation rate;
- repeated rejection immediately followed by fallback participation;
- synchronized rejection/offer behavior;
- unusual account/device relationships;
- regional/time-of-day clusters.

The existence of competitive alternatives and viable deterministic fares may limit gaming, but this should be measured rather than assumed.

If material reject-and-wait behavior appears, the implementation may lock a rejecting driver out of premium bidding on the same request.

## First-qualifying integrity

Because the first qualifying sealed offer clears the trip, authoritative ordering is allocation-critical.

The platform should:

- use server-authoritative receipt/order;
- monitor abnormal latency advantages;
- retain sufficient event data for audit;
- publish or document the ordering policy.

## Calibration integrity

Competitive tuning may adjust only declared competitive variables.

It must not silently push the fare below the economic floor or alter the labour target, commission, minimum-distance rule or scarcity mechanism.

Parameter changes should be versioned and auditable.

## Long-distance claims

Long-distance provisions are rule-derived and accepted before the trip. They are not discretionary after-the-fact driver claims.
