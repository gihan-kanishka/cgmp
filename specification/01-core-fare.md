# CGMP Core Fare Specification

## 1. Purpose

This document defines the ordinary fare calculation in CGMP.

The design objective is to derive a trip price from published, measurable inputs rather than continuously changing the price as a function of platform-estimated scarcity.

## 2. Variables

Let:

- `d_p` = chargeable pickup distance in km
- `d_t` = passenger-trip distance in km
- `r_c` = published distance rate for vehicle class `c`, in currency/km
- `t` = chargeable passenger-trip duration in minutes
- `r_t` = published time rate in currency/minute
- `L` = any pre-agreed necessary long-distance displacement provision
- `F` = passenger fare before optional taxes or legally required external charges

The ordinary fare is:

```text
F = d_p * r_c + d_t * r_c + t * r_t + L
```

or equivalently:

```text
F = (d_p + d_t) * r_c + t * r_t + L
```

## 3. v1.0-draft modelling parameters

| Vehicle class | r_c |
|---|---:|
| bike | Rs 30/km |
| tuk | Rs 40/km |
| mini | Rs 50/km |
| compact | Rs 52.50/km |
| sedan | Rs 55/km |

`r_t = Rs 12/minute`

These are modelling parameters for the Sri Lanka-oriented draft. They are not universal constants.

## 4. Economic interpretation

CGMP deliberately separates the distance and time components.

- The distance component is intended to recover vehicle-use economics and vehicle-related risk.
- The time component is intended to compensate active driver labour/time.

A short statement of the design principle is:

> Distance pays for the vehicle and its risks; time pays for the human.

## 5. Transparency

The platform should expose the major fare components before acceptance whenever practical.

For example:

```text
Distance                    Rs 504
Expected passenger time     Rs 516
Pickup                      Rs  60
Long-distance provision     Rs   0
Estimated total             Rs1080
```

When traffic increases expected journey time, the UI should explain that the expected time component has increased. It should not describe this as scarcity pricing unless a separate market-clearing process is actually being used.

## 6. Commission

Platform commission is not part of the fare equation itself.

For modelling, v1.0-draft uses a 7% commission:

```text
driver_receipt = fare * (1 - commission_rate)
```

Operators may choose a different transparent commission rate.

## 7. Parameter governance

A production implementation should:

1. publish current rates;
2. retain a public or auditable parameter-change history;
3. state the data and methodology used for recalibration;
4. avoid changing rates on a passenger-by-passenger willingness-to-pay basis;
5. avoid silently using scarcity multipliers inside the ordinary fare calculation.

## 8. Calibration concept

The draft proposes that routine maintenance benchmarks be calibrated around **120% of the median routine/expected maintenance cost per kilometre among the majority fleet in each class**, with irregular/uninsured risk accounted for separately where appropriate.

This is a proposed calibration rule and requires empirical fleet data before production use.

## 9. Depreciation treatment

CGMP does not require market-value depreciation to be embedded directly in the fare.

In markets where vehicle resale values are heavily influenced by taxes, import rules, foreign-exchange conditions or policy shocks, a deployment may instead represent measurable physical wear using maintenance and replacement reserves.

Any deployment should state its depreciation/wear methodology explicitly.
