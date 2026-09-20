# Pickup and Search Policy - v1.2

## 1. Initial search

CGMP first searches for eligible vehicles within **0-2 km**.

The minimum-fare structure already includes 2 km of pickup distance.

## 2. Search expansion

If no match is obtained, search expands in fixed **2 km increments**:

```text
0-2 km -> 2-4 km -> 4-6 km -> 6-8 km -> ...
```

The passenger can approve expansion directly or store standing limits such as maximum automatic search radius or pickup cost.

## 3. Pickup billing

Search radius and billing distance are separate.

```text
chargeable pickup km = max(actual authorized pickup km, 2)
```

A 3.2 km pickup is billed as 3.2 km, not 4 km.

## 4. Pickup time

**Pickup time is intentionally not charged in v1.2.**

The passenger already bears the non-monetary cost of waiting before the service begins. CGMP compensates the vehicle movement through pickup distance but does not add a second monetary charge for pickup minutes.

This is an explicit policy choice, not an assumption that pickup time has no value to the driver.

The practical effect is measured through:

- acceptance rate by pickup-distance band;
- total request-to-match time;
- passenger abandonment;
- fallback activation rate.

If evidence later shows a material problem, the policy can be revisited. No pickup-time fraction is added preemptively.

## 5. Expanded search remains deterministic

A farther search radius does not activate bidding.

The ordinary CGMP fare remains in force during every passenger-authorized expansion stage.

Sealed fallback becomes available only after authorized deterministic expansion fails.

## 6. Integrity

The platform should record:

- search stage;
- authorization state;
- candidate pickup route;
- actual pickup distance;
- billed pickup distance.

Server-calculated route distance, rather than a driver-controlled odometer value, should be the authoritative basis where practical.
