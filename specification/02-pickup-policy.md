# Pickup Policy

Pickup distance is charged at the published vehicle-class distance rate.

```text
pickup_charge = approved_pickup_distance * class_distance_rate
```

Pickup time is not separately charged in v1.0-draft.

## Passenger authorization

The reference modelling threshold is **2 km**, but CGMP does not require a separate approval screen every time a pickup exceeds 2 km.

Passengers should be able to configure standing authorization rules during signup or later in settings, including variables such as:

- maximum pickup distance;
- maximum pickup cost.

A pickup that satisfies the passenger's saved authorization may proceed automatically. The app should still disclose the actual pickup distance and pickup charge in the fare breakdown.

If the requested pickup exceeds the passenger's saved limits, explicit passenger approval is required before dispatch.

This preserves informed consent while avoiding unnecessary checkout friction.

## Distance integrity

The chargeable pickup distance should come from a reasonable server-calculated route rather than a driver-controlled distance counter.

Recommended sequence:

1. determine passenger and candidate-driver locations;
2. calculate a reasonable/legal pickup route server-side;
3. calculate the pickup charge;
4. compare distance and cost with the passenger's standing authorization;
5. request explicit approval only when the saved limits are exceeded;
6. freeze the approved pickup basis at dispatch/acceptance, subject to documented exception handling.

## Objective

The rule avoids both forcing drivers to subsidize significant pickup mileage and surprising passengers with pickup charges they did not authorize.

Standing limits also allow frequent users to choose their own balance between dispatch speed and pickup-cost control.
