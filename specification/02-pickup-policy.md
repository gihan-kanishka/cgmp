# Pickup and Search-Expansion Policy - v1.1

## 1. Initial search

CGMP first searches for an eligible vehicle within **2 km**.

The first 2 km of pickup is already represented in the minimum-fare structure, so no separate passenger confirmation is required for the initial 0-2 km search band.

Pickup time is not separately charged in the current reference design.

## 2. Search expansion

If no match is obtained within the current search radius, the search expands in fixed **2 km increments**:

```text
0-2 km -> 2-4 km -> 4-6 km -> 6-8 km -> ...
```

A passenger may:

- approve the next expansion with one click; or
- preconfigure automatic expansion up to a chosen radius and/or pickup-cost limit.

Example:

```text
No nearby vehicle found.
Expand search up to 4 km?
Additional pickup distance may increase the fare.
```

## 3. Billing rule

Search bands control **which drivers are considered**, not how pickup is billed.

The passenger is charged the actual authorized pickup distance, subject to the included 2 km minimum:

```text
chargeable pickup km = max(actual authorized pickup km, 2)
```

A driver 3.2 km away is billed as 3.2 km pickup, not 4 km.

## 4. Standing passenger authorization

Passengers may save preferences such as:

- maximum automatic search radius;
- maximum pickup distance;
- maximum pickup charge.

If a candidate pickup satisfies the saved preferences, expansion may continue without another confirmation. The actual pickup distance and charge should still be disclosed.

## 5. Deterministic pricing during expansion

Expanded-search trips remain priced using the ordinary deterministic CGMP fare.

**Search expansion does not activate bidding.**

The platform should continue attempting deterministic dispatch at the published fare, including the actual pickup charge and any legitimate pre-agreed long-distance provision.

## 6. Transition to sealed fallback

Sealed bidding becomes eligible only after the passenger-authorized deterministic expanded-search process fails to obtain a vehicle.

This makes sealed market clearing a last-resort recovery mechanism rather than a normal pricing stage.

## 7. Integrity

Pickup distance should be server-calculated from a reasonable/legal route and frozen or otherwise auditable at dispatch/acceptance.

The system should distinguish clearly between:

- search-radius ceiling;
- actual pickup distance;
- chargeable pickup distance;
- passenger authorization state.
