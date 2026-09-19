# Pickup Policy

Pickup distance is charged at the published vehicle-class distance rate.

```text
pickup_charge = approved_pickup_distance * class_distance_rate
```

Pickup time is not separately charged in v1.0-draft.

## Passenger consent threshold

Default modelling threshold: **2 km**.

- Pickup at or below the threshold may be incorporated automatically into the quoted fare.
- Pickup above the threshold requires explicit passenger consent before dispatch.

## Distance integrity

The chargeable pickup distance should come from a reasonable server-calculated route rather than a driver-controlled distance counter.

Recommended sequence:

1. determine passenger and candidate-driver locations;
2. calculate a reasonable/legal pickup route server-side;
3. calculate and disclose the pickup charge;
4. obtain consent if the configured threshold is exceeded;
5. freeze the approved pickup basis at dispatch/acceptance, subject to documented exception handling.

## Objective

The rule avoids both forcing drivers to subsidize significant pickup mileage and surprising passengers with unusually large pickup charges they did not approve.
