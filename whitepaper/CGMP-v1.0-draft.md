# Cost-Grounded Mobility Pricing (CGMP)

## An open fare and market-clearing framework for ride-hailing

**Version:** 1.0-draft  
**Date:** 2026-09-20  
**Status:** Design and simulation stage

## Abstract

Cost-Grounded Mobility Pricing (CGMP) is an open ride-hailing fare framework that separates ordinary transport pricing from exceptional scarcity resolution.

Instead of continuously modifying passenger fares using opaque supply-demand multipliers, CGMP computes a baseline fare from published vehicle-distance, driver-time, pickup and necessary long-distance displacement components. If that baseline does not attract a driver, a sealed fallback allows the market to clear within a passenger-chosen private ceiling without exposing that ceiling or competing driver offers.

CGMP prioritizes dispatch speed in the fallback stage: the first server-valid private driver offer that satisfies the baseline and passenger ceiling immediately receives the trip. Driver offers can be generated automatically from private preferences configured while parked, and passengers can pre-authorize pickup and fallback limits to avoid unnecessary interaction.

The framework is intended to improve transparency, reduce arbitrary pricing discretion, make driver compensation more legible, and create a testable alternative to conventional surge-based pricing.

CGMP v1.0-draft is not yet empirically validated. Numerical parameters are modelling inputs that require local fleet and trip data before production deployment.

## 1. Problem statement

Ride-hailing pricing must balance several competing objectives:

- passengers need fares that are understandable and reasonably predictable;
- drivers need compensation for both vehicle use and active working time;
- pickups create real operating cost even before the passenger boards;
- long-distance trips can create unavoidable displacement;
- scarcity sometimes makes a normal fare insufficient to attract a driver;
- dispatch must remain fast enough for time-sensitive trips;
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

## 6. Pickup pricing and passenger preferences

Pickup distance is charged at the ordinary class distance rate.

The reference modelling threshold is **2 km**, but CGMP does not require a separate approval modal every time a pickup exceeds that distance.

Passengers may configure standing authorization rules using variables such as:

- maximum pickup distance;
- maximum pickup cost.

If a candidate pickup falls within the passenger's saved authorization, the request can proceed without another interaction. The app should still disclose the actual pickup distance and charge.

If the requested pickup exceeds the saved limits, explicit passenger approval is required before dispatch.

Pickup time is not separately charged under the draft.

The chargeable route should be server-calculated and not derived solely from a driver-controlled distance counter.

This design treats standing passenger preferences as prospective informed consent while reducing checkout friction.

## 7. Long-distance displacement

CGMP does not guarantee a driver full round-trip economics.

The ordinary fare compensates the outbound trip. A separate provision may be added only for necessary displacement created by the trip, such as accommodation or defined meal support where an immediate safe return is unreasonable.

Any such provision must be rule-derived, disclosed and accepted before the trip, either directly or under a valid pre-authorized rule.

CGMP does not automatically add hypothetical future wages, guaranteed round-trip profit, or an unrestricted empty-return allowance.

If the baseline remains unattractive after legitimate displacement costs are included, the trip proceeds to market clearing rather than receiving an arbitrary automatic multiplier.

## 8. First-qualifying sealed dispatch

Normal dispatch occurs first at the published baseline.

If no eligible driver accepts:

1. the passenger uses a private maximum total fare, either set for the trip or stored as an optional standing fallback ceiling;
2. eligible driver apps evaluate the request using their driver's private pricing preferences;
3. drivers cannot see the passenger's maximum;
4. drivers cannot see other drivers' offers;
5. the first server-valid offer satisfying `baseline <= bid <= passenger maximum` immediately clears the trip;
6. if no offer qualifies, no match occurs unless the passenger voluntarily changes the ceiling.

This produces:

```text
baseline <= clearing offer <= passenger maximum
```

The passenger pays the clearing offer, not automatically the ceiling.

Unlike a conventional sealed auction, CGMP does not wait for a bidding window to close and then search for the lowest offer. Once the passenger has already chosen the maximum they are willing to pay, the fallback objective is **fast dispatch within that affordability boundary**.

### 8.1 Driver-side automatic pricing

Drivers should configure fallback pricing preferences during signup or while parked.

A private pricing function may consider:

- estimated arrival time to the passenger;
- pickup distance;
- trip distance;
- expected trip duration;
- road or terrain conditions;
- destination;
- time of day;
- minimum acceptable earnings or margin.

When a fallback request arrives, the app or platform can evaluate those saved rules and submit the driver's private offer automatically.

A production implementation should not require manual numerical bidding while the driver is actively operating a vehicle.

### 8.2 Passenger-side automatic limits

Passengers may configure standing preferences such as:

- maximum pickup distance;
- maximum pickup charge;
- optional maximum fallback total fare.

If the relevant conditions remain inside those private limits, dispatch can proceed without an additional confirmation step.

The final pickup charge, fallback use and clearing fare should still be visible to the passenger.

### 8.3 Dispatch-order fairness

Because the first qualifying offer wins, authoritative ordering is important.

A production implementation should send the fallback opportunity to the relevant candidate group at effectively the same dispatch epoch where practical, use server-controlled receipt timestamps or another documented ordering rule, and monitor whether device/network latency systematically advantages particular drivers.

This is a measurable implementation risk rather than a reason to delay every fallback transaction.

## 9. Manipulation resistance

No pricing system is manipulation-proof.

CGMP instead attempts to minimize and constrain manipulation surfaces.

Recommended controls include:

- published pricing parameters;
- server-side route and distance calculation;
- timestamp and movement validation;
- standing passenger authorization with auditable preference versions;
- pre-trip approval of exceptional charges where standing authorization does not apply;
- hidden passenger ceiling;
- sealed private driver offers;
- first-qualifying server-side clearing;
- authoritative offer-order records;
- repeated-pattern analysis for deliberate route stretching or crawling;
- repeated-pattern analysis for speeding/aggressive driving;
- complaint review supported by telemetry rather than automatic punishment;
- detection of chronic unsupported passenger complaints;
- monitoring for coordinated baseline rejection or bid behaviour.

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
- fallback-dispatch rules;
- dispatch-order methodology;
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
- normal-dispatch match time;
- fallback activation-to-assignment latency;
- percentage of fallback requests clearing on the first qualifying offer;
- distribution of fallback assignments among eligible drivers;
- relationship between network latency and fallback win rate;
- speeding events;
- aggressive-driving complaints;
- unexplained excess journey time;
- slow-driving complaints;
- pickup acceptance by distance;
- percentage of pickups handled by standing passenger authorization;
- share of trips entering sealed fallback dispatch;
- fallback clearing premium relative to baseline;
- fallback failure rate;
- long-distance acceptance and completion.

A randomized or carefully matched control design is preferable.

## 14. Open implementation

CGMP is intended for unrestricted practical adoption under open licenses.

The reference software is published under Apache License 2.0. Documentation and specification text are published under CC BY 4.0 unless otherwise stated.

Operators may adapt parameters to local conditions. Material deviations from the reference rules should be identified so users and researchers can distinguish a modified implementation from the reference CGMP specification.

## 15. Conclusion

CGMP is best understood as a hybrid of cost-grounded ordinary pricing and market-based exceptional clearing.

Its central architecture is:

```text
published cost/time baseline
        ↓
normal dispatch
        ↓
if baseline fails
        ↓
private passenger ceiling
+
private automated driver pricing rules
        ↓
first qualifying sealed offer
        ↓
immediate assignment
```

The framework's value does not depend on any single rupee-per-kilometre figure. Its contribution is the separation of ordinary trip economics from scarcity resolution, combined with configurable consent, auditable pricing inputs, private willingness limits and fast market clearing.

Whether this architecture performs better than incumbent models is a question for empirical testing.
