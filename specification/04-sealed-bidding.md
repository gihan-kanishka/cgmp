# Exceptional First-Qualifying Sealed Dispatch - v1.1

## Purpose

The sealed mechanism is a **last-resort exceptional dispatch path**.

It is not activated merely because:

- demand is high;
- no vehicle exists inside the first 2 km;
- the search radius expands;
- a farther pickup costs more.

Those cases remain deterministic CGMP pricing.

## Preconditions

Sealed bidding is eligible only when all of the following are true:

1. normal deterministic search has failed;
2. the passenger has authorized one or more expanded-search stages, either interactively or through standing preferences;
3. the authorized deterministic expanded-search process has failed to obtain a vehicle;
4. the passenger has defined a private fallback affordability ceiling.

This distinction is central to CGMP.

## Passenger ceiling

The passenger, not the platform, defines the private maximum fallback allowance.

Supported forms may include:

1. **percentage above deterministic base**
   ```text
   M = F0 * (1 + p)
   ```
2. **fixed amount per passenger-trip km above base**
   ```text
   M = F0 + a * passenger_trip_km
   ```
3. **fixed additional fee by trip-distance band**
   ```text
   M = F0 + passenger_selected_band_fee
   ```

The platform should not reveal `M` to drivers.

## Driver-side automation

Drivers configure private fallback rules during signup or while parked.

Rules may consider:

- pickup ETA and distance;
- passenger-trip distance;
- expected trip duration;
- road/terrain conditions;
- destination;
- time of day;
- private minimum acceptable economics.

A production implementation should not require numerical bidding while the driver is moving.

## Privacy

During fallback:

- passenger ceiling is hidden from drivers;
- driver offers are hidden from other drivers;
- no live clearing price is revealed;
- competing driver offers are not exposed.

## Selection rule

Let:

- `F0` = deterministic CGMP base fare including authorized pickup and any rule-derived long-distance provision;
- `M` = passenger's private maximum fare;
- `b_i` = a server-valid private driver offer in authoritative receipt order.

A bid qualifies when:

```text
F0 <= b_i <= M
```

The first qualifying offer clears immediately:

```text
for each valid offer b_i in authoritative receipt order:
    if F0 <= b_i <= M:
        assign trip immediately
        charge b_i
        stop
```

The passenger pays the clearing offer, not automatically `M`.

## Why first-qualifying is retained

CGMP deliberately prioritizes dispatch speed only **after deterministic nearby and expanded searches have already failed**.

The mechanism therefore solves a recovery problem, not ordinary price discovery.

A later lower offer does not replace an already cleared assignment. The tradeoff should be measured empirically against latency, price and fairness outcomes.

## Dispatch fairness

Because timing determines the winner, the implementation should:

1. deliver fallback opportunities to the relevant candidate group at effectively the same dispatch epoch where practical;
2. use an authoritative server-side receipt/order mechanism;
3. retain auditable event logs;
4. measure whether network/device latency systematically affects win rates.

## Strategic rejection

A driver might theoretically reject deterministic work in hope of a later premium. CGMP does not assume this risk is zero.

The design relies on several counterforces:

- the deterministic fare is intended to provide viable economics;
- the same trip may be taken by another driver;
- the passenger may switch platforms or cancel;
- fallback is reached only after authorized expansion fails.

A production pilot should measure rejection patterns and fallback activation rather than assuming either benign or strategic behavior.

A deployment may additionally prevent a driver who rejected a specific deterministic request from later bidding on that same request if evidence shows reject-and-wait gaming is material.

## Health metric

```text
fallback activation rate =
  trips entering sealed fallback / all ride requests
```

CGMP intends this rate to remain low. A high or rising rate is a signal to investigate baseline calibration, supply, search policy or strategic behavior.
