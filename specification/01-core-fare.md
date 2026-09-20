# CGMP Core Fare Specification - v1.2

## 1. Objective

CGMP v1.2 deliberately keeps the fare mechanism small.

The core rule is:

> Distance pays for vehicle use; passenger-trip time pays for the human.

Potential behavioral problems are monitored before extra tariff rules are added.

## 2. Fare equation

Let:

- `d_t` = passenger-trip distance;
- `d_p` = actual authorized pickup distance;
- `D_min` = minimum passenger-trip distance;
- `P_min` = included pickup distance;
- `r_c` = passenger-facing distance rate for class `c`;
- `t` = verified passenger-trip minutes;
- `r_t` = passenger-facing time rate;
- `L` = pre-agreed long-distance provision.

Reference fare:

```text
F =
  [max(d_t, D_min) + max(d_p, P_min)] * r_c
  + t * r_t
  + L
```

Current reference values:

```text
D_min = 2 km
P_min = 2 km
r_t = Rs 12.90/min
commission = 7%
```

Pickup time is not billable.

## 3. Current passenger distance rates

| Class | Passenger distance rate |
|---|---:|
| Bike | Rs 19.00/km |
| Tuk | Rs 37.00/km |
| Mini | Rs 51.50/km |
| Compact | Rs 53.00/km |
| Sedan | Rs 61.50/km |

## 4. ICE cost basis

Current provisional routine ICE cost assumptions:

| Class | Routine ICE cost/km |
|---|---:|
| Bike | Rs 14.50 |
| Tuk | Rs 22.10 |
| Mini | Rs 32.80 |
| Compact | Rs 34.00 |
| Sedan | Rs 36.10 |

A production calibration must publish the dated underlying inputs used to derive these aggregates.

The intended component structure is:

```text
routine ICE cost/km =
    fuel cost/km
  + tyres/km
  + scheduled service/km
  + brakes/suspension/repairs/km
  + other defined routine wear/km
```

CGMP v1.2 does not invent a component breakdown where empirical data has not yet been collected.

EV and unusually efficient vehicle economics do not set passenger tariffs.

## 5. Competitive headroom

Current target net vehicle headroom after commission:

| Class | Target net headroom/km |
|---|---:|
| Bike | Rs 3 |
| Tuk | Rs 12 |
| Mini | Rs 15 |
| Compact | Rs 15 |
| Sedan | Rs 21 |

Let:

- `C_c` = representative ICE routine economic cost/km for class `c`;
- `H_c` = non-negative competitive headroom/km;
- `gamma` = platform commission rate.

The **vehicle-distance economic floor** is:

```text
R_floor_c = C_c / (1 - gamma)
```

The published passenger distance rate is:

```text
R_c = roundUp_0.50(
        (C_c + H_c) / (1 - gamma)
      )
```

where `roundUp_0.50` means round upward to the next **Rs 0.50/km** billing increment.

Therefore, **headroom is not part of the economic floor**. It is the competitive margin above the floor.

Headroom may be recalibrated against competitor fares, but only through a scheduled periodic review using standardized ordinary/non-scarcity observations.

It must not be adjusted continuously with demand, must remain non-negative, and must not push the published rate below `R_floor_c`.

## 6. Labour rate

Current target net driver labour compensation during the passenger trip is **Rs 12/minute**.

```text
12 / 0.93 ~= Rs 12.90/min passenger-facing
```

This is a **paid passenger-trip labour rate**, not a claim that a driver earns Rs 720 for every hour logged into the platform.

Actual online-hour earnings depend on utilization, pickup time, idle time, acceptance and market conditions and must be measured separately.

## 7. Verified passenger-trip time

Billable time:

- begins at the server-recorded passenger-trip start;
- ends at the server-recorded trip end;
- excludes pickup time;
- is checked against route/GPS/trip-state data;
- is flagged for review when implausible or disputed.

The reference implementation treats the upfront price as an estimate and the final fare as a metered fare using verified passenger-trip time.

A fixed-price implementation is a documented variant, not the v1.2 reference rule.

## 8. Congestion versus scarcity

Congestion may increase the fare because it increases paid passenger-trip time.

CGMP therefore does **not** claim that fares never increase with traffic conditions.

The narrower claim is:

> The ordinary tariff does not apply an automatic supply-demand scarcity multiplier.

## 9. Gross fare, commission and pass-through costs

Published rates and fallback offers are **gross passenger-facing amounts**.

The 7% commission applies to commissionable fare components, including:

- distance;
- passenger-trip time;
- fallback premium.

A direct third-party/pass-through expense may be marked commission-exempt when it is separately identified before acceptance, for example an actual toll or explicitly reimbursed accommodation expense.

## 10. Parameter governance

A production implementation should publish:

- current parameters;
- effective dates;
- cost-input methodology;
- competitive-review methodology;
- parameter-change history.

The mechanism should remain simple enough that a passenger, driver or auditor can reproduce the fare from the published inputs.
