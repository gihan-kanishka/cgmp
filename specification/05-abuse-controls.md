# Abuse and Integrity Controls

CGMP reduces discretionary pricing but remains vulnerable to falsified inputs and strategic behaviour. Fare integrity should therefore be treated as a server-side systems problem.

## Fare-critical data

Where feasible, the server should validate or calculate:

- legal/reasonable route geometry;
- pickup distance;
- passenger-trip distance;
- timestamps;
- vehicle movement plausibility;
- start/end state;
- vehicle class;
- long-distance eligibility;
- bid-round state.

Client telemetry is evidence, not sole authority.

## Deliberate trip stretching

A single slow or unusual trip is not sufficient evidence of abuse.

The system should look for repeated patterns such as materially longer journey times than comparable trips, unnecessary detours, repeated passenger complaints supported by telemetry, and unexplained divergence from reasonable routes.

## Speed manipulation

The same framework should identify both repeated deliberate crawling intended to inflate time charges and repeated speeding/aggressive driving.

The pricing objective is not to reward either behaviour.

## Passenger complaint integrity

Passenger reports should contribute to review, not automatically determine guilt.

Users who repeatedly submit unsupported complaints across many drivers can be identified and their reports routed for additional verification.

> Reports establish patterns; objective trip data validates them.

## Long-distance claims

Long-distance provisions are rule-derived and accepted before the trip; they are not discretionary after-the-fact driver claims.

## Platform governance

A deployment should publish fare parameters, commission, pickup rules, long-distance rules, bidding rules, and major parameter revisions.

This does not make manipulation impossible, but it makes discretionary changes more visible and auditable.
