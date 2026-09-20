# Long-Distance Displacement Policy - v1.4

## Threshold

The ordinary meter applies through the first 40 passenger kilometres. Long-distance displacement accrual begins only beyond 40 km.

```text
eligible_long_distance_km = max(d_t - 40, 0)
```

## Progressive marginal schedule

A deployment publishes contiguous marginal bands beginning at 40 km. Only kilometres inside a band earn that band's displacement amount.

```text
eligible_km_b = max(0, min(d_t, U_b) - L_b)
I_progressive = sum_b(lambda_b * eligible_km_b)
```

Exact v1.4 marginal values remain a calibration item. Before charging them, the deployment must publish the bands and rates.

The schedule must be monotonic and boundary-safe: adding distance must never reduce fare, and crossing a boundary must not retrospectively surcharge earlier kilometres.

## Progressive display and reconciliation

The live long-distance amount is provisional. At trip completion the server determines the authoritative final amount from final distance and published route/destination eligibility rules.

```text
A_L = I_final - I_live
F_final = F_meter + I_final
```

Only the provisional long-distance component may be adjusted. Legitimate ordinary distance and time are not clawed back.

Driver-created lateness must not increase the long-distance treatment in a way that rewards delay on top of the time charge.

## One-day displacement principle

The incentive does not guarantee empty-return economics. It compensates temporary displacement for up to one day while preserving the possibility of destination-area work or a paid return-direction trip.

Measure return-direction matches at 6, 12 and 24 hours, paid/unpaid postdropoff kilometres, and productive/idle postdropoff time.

## Continuation integrity

Immediate same-passenger/same-driver continuation must not trivially avoid the 40 km threshold. A deployment must publish a continuity rule for economically continuous journeys.
