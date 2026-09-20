# Exceptional First-Qualifying Sealed Dispatch - v1.2

## Purpose

Sealed dispatch is a last-resort recovery mechanism.

It is not part of ordinary pricing and is not activated merely because the initial 2 km search fails.

## Preconditions

Fallback is eligible only after:

1. the initial deterministic search fails;
2. the passenger authorizes expanded deterministic search;
3. the authorized deterministic expansions fail;
4. the passenger has a private fallback affordability rule.

## Driver-specific baseline

Pickup distance differs by driver, so the deterministic baseline may also differ by driver.

For candidate driver `i`:

- `F0_i` = gross passenger-facing deterministic fare using that candidate's actual authorized pickup distance and any pre-agreed provision;
- `M_i` = private passenger maximum produced by applying the passenger's chosen ceiling rule to `F0_i`;
- `b_i` = gross passenger-facing fallback offer from candidate `i`.

This makes the passenger's **rule** common while allowing the rupee value of the ceiling to reflect legitimate pickup differences.

## Passenger ceiling modes

The reference implementation supports:

- percentage above base;
- fixed additional amount per passenger-trip km;
- fixed additional fee by trip-distance band.

The passenger ceiling is private.

## Driver offers

Driver offers are private and may be generated automatically from preferences configured while parked.

A moving driver should not be required to type a numerical bid.

## Selection rule

An offer qualifies when:

```text
F0_i <= b_i <= M_i
```

The first server-valid qualifying offer in authoritative order clears immediately.

The passenger pays `b_i`, not automatically `M_i`.

The offer is a **gross passenger-facing fare**. The platform commission is taken from commissionable fare after clearing.

## v1.2 simplicity rule

The reference core does **not** preemptively add:

- a rejecter ban;
- a premium cap;
- a lowest-bid waiting window;
- a network-latency handicap;
- adaptive bidding restrictions.

Those are possible future controls only if simulation or pilot evidence demonstrates a material problem.

## Monitoring

The system should measure:

- fallback activation rate;
- fallback premium distribution;
- clearing-offer distance from the passenger ceiling;
- reject-then-fallback participation;
- total request-to-fallback time;
- passenger abandonment by stage;
- device/network latency versus fallback win rate.

A high fallback rate or persistent premium drift is a diagnostic signal, not a reason to silently convert fallback into normal pricing.
