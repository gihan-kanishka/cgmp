# Sealed-Bid Market-Clearing Fallback

## Purpose

The sealed-bid mechanism is an exception path used when the published ordinary fare does not attract a willing driver. It is not part of normal fare calculation.

## Preconditions

1. The trip is first offered at the normal CGMP baseline.
2. No eligible driver accepts within the configured dispatch process.
3. The passenger elects to continue and may set a maximum total fare.

## Privacy rules

During a bidding round:

- the passenger maximum is hidden from drivers;
- each driver's bid is hidden from other drivers;
- drivers cannot react to competitors' bids;
- the platform does not reveal a live clearing price before the round closes.

## Selection rule

Let `M` be the passenger maximum and `B` the set of valid bids.

```text
eligible bids = { b in B | baseline <= b <= M }
winning bid = minimum eligible bid
```

If no eligible bid exists, no match is produced. The passenger may voluntarily raise the ceiling and open another round.

The passenger is charged the winning bid, not automatically the maximum.

## Driver display

Where practical, the bidding UI should show expected take-home after commission.

## Anti-collusion monitoring

A deployment should monitor repeated coordinated baseline rejection, unusually synchronized bids, alternating-win patterns, and account/device relationships suggesting common control.

Enforcement should rely on repeatable evidence rather than a single high bid.

## Design objective

Scarcity affects price only after the ordinary baseline actually fails to clear the market.
