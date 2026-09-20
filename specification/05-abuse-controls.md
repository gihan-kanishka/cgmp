# Integrity and Monitoring Controls - v1.4

## Server-authoritative meter

Validate pickup route/distance, passenger-trip route/distance, server timestamps, trip state, vehicle class, personal-stop pause events, destination changes and long-distance eligibility.

## Personal stops

A driver personal stop during an active passenger trip requires the time meter to be paused. Both driver and passenger apps must show a persistent pause notification and a resume notification. Clear non-service detour distance should be excluded at reconciliation.

## Meter farming

Flag repeated unexplained loops, route stretching, avoidable stationary time, impossible timestamps and systematic excess duration compared with comparable traffic conditions. A single unusual trip is not proof of abuse; repeated patterns carry more evidentiary weight.

## Cancellation integrity

Record acceptance, movement toward pickup, passenger cancellation, driver cancellation, no-show state, validated pickup distance and settlement amount. Repeated suspicious same-party cancellation patterns should be reviewable.

## Long-distance integrity

Record provisional accrual, final reconciliation, route/destination eligibility and immediate same-passenger/same-driver continuations. Driver-created lateness must not produce an extra long-distance reward on top of the time meter.

## Cash ledger integrity

Record cash commission debt, direct settlements, electronic offsets, warnings, threshold hits and cash-trip restrictions.
