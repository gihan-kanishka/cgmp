# First-Qualifying Sealed Dispatch

## Purpose

The sealed fallback is an exception path used when the published ordinary fare does not attract a willing driver.

It is designed for **fast market clearing within a passenger-chosen affordability limit**, not for waiting through an auction window to discover the mathematically lowest offer.

## Preconditions

1. The trip is first offered at the normal CGMP baseline.
2. No eligible driver accepts within the configured normal-dispatch process.
3. The passenger has either set a private maximum total fare or enabled a saved fallback ceiling.

## Privacy rules

During fallback dispatch:

- the passenger maximum is hidden from drivers;
- each driver's offer is hidden from other drivers;
- drivers cannot react to competitors' offers;
- the platform does not reveal a live clearing price;
- the platform does not expose the passenger's willingness-to-pay ceiling.

## Driver-side automation

Drivers should configure private fallback pricing rules during signup or while parked.

Those rules may use inputs such as:

- estimated arrival time to the passenger;
- pickup distance;
- trip distance;
- expected trip duration;
- road or terrain conditions;
- destination;
- time of day;
- the driver's own minimum acceptable earnings or margin.

When a fallback request arrives, the app or server may evaluate the driver's private rule and submit an offer automatically.

A production implementation should not require a driver to type or evaluate numerical bids while actively operating a vehicle.

## Selection rule

Let:

- `F0` = ordinary baseline fare;
- `M` = passenger's private maximum total fare;
- `b_i` = a server-valid driver offer received in authoritative order.

A bid qualifies when:

```text
F0 <= b_i <= M
```

The **first qualifying offer received under the platform's authoritative dispatch-order rule immediately clears the trip**.

```text
for each valid offer b_i in authoritative receipt order:
    if F0 <= b_i <= M:
        assign trip immediately
        charge b_i
        stop
```

The passenger pays the clearing offer, not automatically the maximum.

If no qualifying offer arrives within the fallback window, no match is produced. The passenger may voluntarily change the ceiling or try again.

## Dispatch fairness and latency

Because the first qualifying offer wins, dispatch-order integrity matters.

A production implementation should:

1. send the fallback opportunity to the relevant candidate group at effectively the same dispatch epoch where technically practical;
2. use server-controlled receipt timestamps or another documented authoritative ordering mechanism;
3. avoid intentionally advantaging selected drivers through staggered notification timing unless the dispatch policy explicitly requires it;
4. monitor network-latency effects and publish or internally audit the ordering policy.

The goal is to optimize matching speed without turning hidden notification ordering into an undisclosed allocation mechanism.

## Passenger-side automation

A passenger may choose to store a private fallback ceiling in advance.

When enabled, a failed baseline request can enter fallback dispatch immediately without requiring another passenger interaction, provided the resulting clearing fare stays within that private ceiling.

The app should still disclose the final fare and the fact that fallback dispatch was used.

## Anti-collusion monitoring

Sealed offers reduce direct price copying but do not eliminate collusion.

A deployment should monitor repeated coordinated baseline rejection, unusually synchronized pricing policies or offers, alternating-win patterns, and account/device relationships suggesting common control.

Enforcement should rely on repeatable evidence rather than a single high offer.

## Design objective

Scarcity affects price only after the ordinary baseline actually fails to clear the market.

The passenger chooses the affordability boundary, drivers privately define the economics under which they are willing to serve the trip, and the system prioritizes immediate matching once those two conditions overlap.
