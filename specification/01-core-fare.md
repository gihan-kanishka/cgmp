# CGMP Core Fare Specification - v1.1

## 1. Purpose

This document defines the ordinary CGMP fare and its calibration rules.

CGMP separates three things that should not be silently mixed:

1. representative vehicle operating economics;
2. driver labour compensation;
3. competitive margin tuning above the economic floor.

Scarcity does not alter the ordinary fare merely because demand is high.

## 2. Ordinary fare

Let:

- `d_t` = passenger-trip distance in km;
- `d_p` = actual authorized pickup distance in km;
- `D_min` = minimum passenger-trip distance;
- `P_min` = included initial pickup distance;
- `r_c` = passenger-facing distance rate for vehicle class `c`;
- `t` = verified legitimate passenger-trip duration in minutes;
- `r_t` = passenger-facing time rate;
- `L` = pre-agreed long-distance displacement provision.

The v1.1 ordinary fare is:

```text
F =
  [max(d_t, D_min) + max(d_p, P_min)] * r_c
  + t * r_t
  + L
```

Current reference settings:

```text
D_min = 2 km
P_min = 2 km
r_t   = Rs 12.90/min
commission = 7%
```

Pickup time is not separately charged.

## 3. Current passenger distance rates

| Class | Passenger distance rate |
|---|---:|
| Bike | Rs 19.00/km |
| Tuk | Rs 37.00/km |
| Mini | Rs 51.50/km |
| Compact | Rs 53.00/km |
| Sedan | Rs 61.50/km |

These are modelling outputs from the current cost and competitive-headroom assumptions, not permanent constants.

## 4. ICE-based calibration

Passenger tariffs are calibrated from **representative ICE economics for each service class**.

EV or unusually efficient vehicle costs do not set the passenger tariff. Owners of more efficient vehicles retain the efficiency saving.

Current provisional routine ICE cost assumptions:

| Class | Representative routine ICE cost/km |
|---|---:|
| Bike | Rs 14.50 |
| Tuk | Rs 22.10 |
| Mini | Rs 32.80 |
| Compact | Rs 34.00 |
| Sedan | Rs 36.10 |

These inputs require empirical fleet validation.

## 5. Competitive vehicle headroom

The current target net vehicle headroom above routine ICE cost, **after commission**, is:

| Class | Target net headroom/km |
|---|---:|
| Bike | Rs 3 |
| Tuk | Rs 12 |
| Mini | Rs 15 |
| Compact | Rs 15 |
| Sedan | Rs 21 |

The calibration equation is:

```text
raw passenger distance rate =
  (routine ICE cost/km + target net vehicle headroom/km)
  / (1 - commission)
```

The reference implementation rounds upward to a transparent Rs 0.50 billing increment.

These headrooms are **competitive calibration variables**. They may move as competitor passenger fares and market conditions change, but competitive tuning must not violate the economic floor.

## 6. Economic floor

Competition may determine how much room exists above cost. It does not determine whether CGMP is allowed to price below sustainable economics.

At minimum, the calibration must preserve:

- representative ICE routine operating cost;
- the published net labour target;
- the transparent platform commission required to operate the service.

A deployment may add explicitly defined mandatory reserves to that floor once supported by empirical loss/repair data.

The governance principle is:

> Costs set the floor; competition sets how far above the floor the tariff can reasonably sit.

## 7. Labour rate

Current target net driver labour compensation is:

```text
Rs 12.00/minute after commission
```

Therefore:

```text
passenger time rate = 12 / 0.93 = approximately Rs 12.90/minute
```

At the 25 km/h reference speed used for examples:

```text
time equivalent per passenger-trip km
= (60 / 25) * 12.90
= Rs 30.96/km
```

This 25 km/h value is an estimation benchmark, not a forced production travel speed.

## 8. Benchmark examples

For a 13 km passenger trip with a 2 km pickup, reference trip time at 25 km/h is 31.2 minutes.

| Class | Estimated passenger fare |
|---|---:|
| Bike | Rs 687.48 |
| Tuk | Rs 957.48 |
| Mini | Rs 1,174.98 |
| Compact | Rs 1,197.48 |
| Sedan | Rs 1,324.98 |

For a 2 km passenger trip with up to 2 km pickup, the 25 km/h reference time is 4.8 minutes:

| Class | Estimated minimum fare |
|---|---:|
| Bike | Rs 137.92 |
| Tuk | Rs 209.92 |
| Mini | Rs 267.92 |
| Compact | Rs 273.92 |
| Sedan | Rs 307.92 |

Production fares use verified legitimate trip time.

## 9. Competitive benchmarking

Operators may compare standardized benchmark trips against competitor platforms, for example 2, 5, 10, 13 and 20 km trips under clearly stated time/pickup assumptions.

Competitive observations may tune the class headroom, but they must not silently alter:

- the underlying cost methodology;
- the labour target;
- commission disclosure;
- minimum-distance or pickup rules;
- scarcity rules.

## 10. Transparency

The passenger interface should make the causal components understandable:

```text
Passenger distance
Passenger time
Pickup distance
Long-distance provision
Estimated/final total
```

Traffic may increase the time component because it consumes legitimate driver time. That is different from a scarcity multiplier.
