# Core Fare - v1.4

## Ordinary meter

```text
F_meter = [max(d_t, 2) + max(d_p, 2)] * r_c + t_b * 12.90
```

`d_t` is passenger-trip distance, `d_p` is authorized pickup distance, and `t_b` is verified billable passenger-trip time after driver-personal-stop pauses.

Published class rates:

- Bike: Rs 22/km
- Tuk: Rs 37/km
- Mini: Rs 52/km
- Compact: Rs 57/km
- Sedan: Rs 65/km

Platform commission is 7% of passenger-paid CGMP components.

## Economic floor and headroom

```text
R_floor_c = C_c / (1 - gamma)
H_c = R_c * (1 - gamma) - C_c
```

Representative class cost sets the floor. Published headroom is a scheduled competitive/class-risk margin above the floor.

## Efficiency

The tariff is class-based. Individual fuel, maintenance, hybrid or EV efficiency savings remain with the driver.

## No surge and no driver bidding

The v1.4 reference core has no automatic demand/supply surge multiplier and no discretionary driver-bidding premium.
