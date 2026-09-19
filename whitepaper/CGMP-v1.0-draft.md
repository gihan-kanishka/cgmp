# Cost-Grounded Mobility Pricing (CGMP)

## An open fare and market-clearing framework for ride-hailing

**Version:** 1.0-draft  
**Date:** 2026-09-20  
**Status:** Design and simulation stage

## Abstract

Cost-Grounded Mobility Pricing (CGMP) is an open ride-hailing fare framework that separates ordinary transport pricing from exceptional scarcity resolution.

Instead of continuously modifying passenger fares using opaque supply-demand multipliers, CGMP computes a baseline fare from published vehicle-distance, driver-time, pickup and necessary long-distance displacement components. If that baseline does not attract a driver, a sealed-bid fallback allows the market to discover an exceptional clearing price without exposing the passenger's maximum willingness to pay or competing driver bids.

The framework is intended to improve transparency, reduce arbitrary pricing discretion, make driver compensation more legible, and create a testable alternative to conventional surge-based pricing.

CGMP v1.0-draft is not yet empirically validated. Numerical parameters are modelling inputs that require local fleet and trip data before production deployment.

## 1. Problem statement

Ride-hailing pricing must balance several competing objectives:

- passengers need fares that are understandable and reasonably predictable;
- drivers need compensation for both vehicle use and active working time;
- pickups create real operating cost even before the passenger boards;
- long-distance trips can create unavoidable displacement;
- scarcity sometimes makes a normal fare insufficient to attract a driver;
- pricing systems can create behavioural incentives, including incentives related to speed, route choice and trip duration.

A pricing system that relies heavily on dynamic scarcity multipliers can clear markets, but it can also make the reason for a fare change difficult to distinguish from the platform's own pricing discretion.

CGMP therefore separates two questions:

1. What should an ordinary trip cost under published rules?
2. What should happen when that ordinary price fails to attract supply?

## 2. Core principle

The framework uses the following design principle:

> Distance pays for the vehicle and its risks; time pays for the human.

Ordinary pricing is therefore composed from measurable trip inputs.

Let:

- d_p = chargeable pickup distance;
- d_t = passenger-trip distance;
- r_c = vehicle-class distance rate;
- t = passenger-trip duration;
- r_t = driver-time rate;
- L = pre-agreed necessary long-distance displacement provision.

Then:

```text
F = (d_p + d_t) * r_c + t * r_t + L
```

The equation is simple by design. Complexity should live in transparent parameter calibration and integrity controls rather than in an opaque willingness-to-pay algorithm.

## 3. v1.0-draft parameters

For Sri Lanka-oriented modelling, the current draft uses:

| Class | Distance rate |
|---|---:|
| Bike | Rs 30/km |
| Tuk | Rs 40/km |
| Mini | Rs 50/km |
| Compact | Rs 52.50/km |
| Sedan | Rs 55/km |

Common time rate: **Rs 12/minute**.

Illustrative platform commission: **7%**.

These values are provisional. The architecture is intended to survive recalibration.

## 4. Vehicle-cost calibration

A production deployment should estimate routine fleet operating costs from observed market data rather than from a single representative vehicle.

The current calibration concept is:

> routine maintenance allowance should be based on approximately 120% of the median routine/expected maintenance cost per kilometre among the majority fleet in each class.

This is intended to avoid allowing unusually expensive or unusually old vehicles to determine the tariff while still leaving a margin above the central fleet-cost estimate.

Irregular/uninsured risk may be handled through a distinct per-kilometre reserve rather than being hidden inside ordinary maintenance assumptions.

Whole-vehicle market-value depreciation need not be included directly where resale values are heavily distorted by taxes, import rules, exchange rates or policy shocks. A deployment should explicitly state how it represents measurable physical wear and replacement cost.

## 5. Traffic and time

Traffic can increase a CGMP fare because the trip consumes more driver time.

This is conceptually different from increasing the fare merely because many passengers are requesting rides at once.

A passenger-facing interface should explain the cause directly, for example:

```text
Distance component
Expected time component
Pickup component
Long-distance provision
Estimated total
```

If congestion adds expected journey time, the platform can show that additional time and its price effect before acceptance.

## 6. Pickup pricing

Pickup distance is charged at the ordinary class distance rate.

The v1.0-draft consent rule is:

- up to 2 km: pickup cost may be incorporated automatically;
- over 2 km: the passenger must explicitly approve the additional pickup distance/cost before dispatch.

Pickup time is not separately charged under the draft.

The chargeable route should be server-calculated and not derived solely from a driver-controlled distance counter.

## 7. Long-distance displacement

CGMP does not guarantee a driver full round-trip economics.

The ordinary fare compensates the outbound trip. A separate provision may be added only for necessary displacement created by the trip, such as accommodation or defined meal support where an immediate safe return is unreasonable.

Any such provision must be rule-derived, disclosed and accepted before the trip.

CGMP does not automatically add hypothetical future wages, guaranteed round-trip profit, or an unrestricted empty-return allowance.

If the baseline remains unattractive after legitimate displacement costs are included, the trip proceeds to market price discovery rather than receiving an arbitrary automatic multiplier.

## 8. Sealed-bid market clearing

Normal dispatch occurs first at the published baseline.

If no eligible driver accepts:

1. the passenger may set a private maximum total fare;
2. drivers receive the trip details and submit private bids;
3. drivers cannot see the passenger's maximum;
4. drivers cannot see other drivers' bids;
5. the system selects the lowest valid bid not exceeding the passenger maximum;
6. if no bid qualifies, no match occurs unless the passenger voluntarily raises the ceiling.

This produces:

```text
baseline <= winning bid <= passenger maximum
```

The passenger pays the winning bid, not automatically the ceiling.

The mechanism allows supply and demand to influence exceptional trips while preventing the platform from needing to invent a universal surge multiplier.

## 9. Manipulation resistance

No pricing system is manipulation-proof.

CGMP instead attempts to minimize and constrain manipulation surfaces.

Recommended controls include:

- published pricing parameters;
- server-side route and distance calculation;
- timestamp and movement validation;
- pre-trip approval of exceptional charges;
- hidden passenger ceiling;
- sealed driver bids;
- lowest-valid-bid selection;
- repeated-pattern analysis for deliberate route stretching or crawling;
- repeated-pattern analysis for speeding/aggressive driving;
- complaint review supported by telemetry rather than automatic punishment;
- detection of chronic unsupported passenger complaints;
- monitoring for coordinated bid/rejection behaviour.

The framework should therefore be described as manipulation-resistant, not immune to manipulation.

## 10. Behavioural and safety hypothesis

A mostly distance-based fare can create an economic incentive to complete more kilometres per working hour.

CGMP explicitly compensates active trip time. The design hypothesis is that this reduces the financial penalty associated with lawful speeds, congestion and reasonable journey times.

However, time-based compensation can also create an opposite incentive to prolong trips.

CGMP therefore treats both speeding and deliberate crawling as measurable behavioural risks requiring repeated-pattern analysis.

The net safety effect is an empirical question and must be tested.

## 11. Efficient vehicles

CGMP prices service classes, not individual drivetrains.

An efficient petrol vehicle, hybrid or electric vehicle can therefore retain its lower operating cost as an ownership advantage rather than automatically passing the entire saving through to the passenger.

This creates a market incentive to adopt more efficient vehicles without requiring an EV-specific passenger subsidy.

## 12. Governance

A credible implementation should publish:

- class distance rates;
- time rate;
- platform commission;
- pickup policy;
- long-distance rules;
- bidding rules;
- parameter-change history;
- calibration methodology.

Ordinary fares should not change secretly based on inferred passenger willingness to pay.

## 13. Validation requirements

CGMP should not be claimed as superior without a real-world pilot.

A pilot should compare it with an existing pricing system using predefined metrics such as:

- passenger fare per trip and per kilometre;
- driver net earnings after operating costs;
- acceptance rate;
- cancellation rate;
- match time;
- speeding events;
- aggressive-driving complaints;
- unexplained excess journey time;
- slow-driving complaints;
- pickup acceptance by distance;
- share of trips entering sealed bidding;
- sealed-bid clearing premium;
- bidding failure rate;
- long-distance acceptance and completion.

A randomized or carefully matched control design is preferable.

## 14. Open implementation

CGMP is intended for unrestricted practical adoption under open licenses.

The reference software is published under Apache License 2.0. Documentation and specification text are published under CC BY 4.0 unless otherwise stated.

Operators may adapt parameters to local conditions. Material deviations from the reference rules should be identified so users and researchers can distinguish a modified implementation from the reference CGMP specification.

## 15. Conclusion

CGMP is best understood as a hybrid of cost-grounded ordinary pricing and market-based exceptional price discovery.

Its central architecture is:

```text
published cost/time baseline
        ↓
normal dispatch
        ↓
if baseline fails
        ↓
private passenger ceiling + sealed driver bids
        ↓
lowest qualifying bid
```

The framework's value does not depend on any single rupee-per-kilometre figure. Its contribution is the separation of ordinary trip economics from scarcity resolution, combined with explicit consent, auditable pricing inputs and a competitive fallback.

Whether this architecture performs better than incumbent models is a question for empirical testing.
