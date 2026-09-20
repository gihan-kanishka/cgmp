# Cost-Grounded Mobility Pricing (CGMP)

CGMP is an open framework for transparent ride-hailing fare calibration, progressive pickup search and long-distance displacement compensation.

**Current version:** v1.4-preprint  
**Date:** 2026-09-21  
**Stage:** design preprint; controlled-pilot validation pending

## Current reference tariff

| Class | Rate |
|---|---:|
| Bike | **Rs 22/km** |
| Tuk | **Rs 37/km** |
| Mini | **Rs 52/km** |
| Compact | **Rs 57/km** |
| Sedan | **Rs 65/km** |

Passenger-trip time: **Rs 12.90/minute**  
Platform commission: **7%**  
Passenger minimum component: **2 km**  
Pickup minimum component: **2 km**  
Pickup time: **not charged**

```text
F_meter = [max(d_t, 2) + max(d_p, 2)] * r_c + t_b * 12.90
```

`t_b` excludes driver-personal-stop time that has been paused.

## Core v1.4 principles

- no automatic demand/supply surge multiplier;
- no discretionary driver bidding;
- passenger-authorized pickup search expands in 2 km steps;
- actual authorized pickup distance is billed above the 2 km minimum;
- passenger cancellation can settle validated pickup compensation to the driver;
- driver personal stops require a visible time-billing pause;
- individual vehicle efficiency savings remain with the driver;
- long-distance displacement treatment begins after **40 passenger km**;
- long-distance accrues progressively by published marginal bands and is reconciled at trip end;
- the passenger does not finance a guaranteed empty return;
- cash commission uses a driver ledger with a published settlement threshold.

## Reference examples

For a **13 km passenger trip + 2 km pickup**:

| Class | 25 km/h | 40 km/h |
|---|---:|---:|
| Bike | Rs 732.48 | Rs 581.55 |
| Tuk | Rs 957.48 | Rs 806.55 |
| Mini | Rs 1,182.48 | Rs 1,031.55 |
| Compact | Rs 1,257.48 | Rs 1,106.55 |
| Sedan | Rs 1,377.48 | Rs 1,226.55 |

Reference speeds are illustrations only. Production pricing uses verified actual passenger-trip time.

## Long distance

The first 40 passenger kilometres use the ordinary meter only. Beyond 40 km, a published progressive marginal schedule accrues a provisional displacement amount. At completion, the server reconciles the provisional amount against the authoritative final distance and eligibility. Exact marginal rates remain a calibration item before charging them in a live pilot.

## Validation priorities

- pickup acceptance by kilometres and minutes;
- passenger/driver cancellation and no-show behavior;
- personal-stop and meter-integrity outcomes;
- driver paid-trip versus online-hour earnings;
- platform sustainability at 7%;
- cash-ledger settlement behavior;
- long-distance provisional/final adjustments;
- 6/12/24-hour return-direction matching and postdropoff utilization.

## Repository layout

- `specification/` - normative design modules
- `simulator/cgmp.py` - reference calculator
- `tests/test_cgmp.py` - executable invariants
- `config/cgmp-v1.example.json` - machine-readable reference settings
- `docs/` - design Q&A and validation plan
- `preprint/CGMP-v1.4-preprint.md` - current publication source

Reference software is Apache-2.0. Documentation/specification/preprint is CC BY 4.0 unless otherwise stated.
