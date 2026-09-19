# Changelog

## v1.0-draft — 2026-09-20

Initial public design draft.

### Added

- Cost-grounded normal fare architecture.
- Published vehicle-class distance rates as configurable modelling inputs.
- Common driver-time component.
- Paid pickup distance with configurable passenger authorization.
- Separation of ordinary pricing from scarcity pricing.
- Sealed driver-offer fallback with hidden passenger ceiling.
- First-qualifying-bid immediate clearing rule.
- Driver-side automatic fallback pricing preferences configurable while parked.
- Passenger-side standing pickup distance/cost authorization.
- Optional saved private passenger fallback ceiling.
- Server-authoritative fallback offer ordering and dispatch-fairness requirements.
- Long-distance displacement policy with pre-trip passenger consent.
- Explicit treatment of efficient vehicles: efficiency gains remain with the owner.
- Server-side integrity and repeated-abuse review principles.
- Safety and economic claims explicitly classified as hypotheses pending pilot validation.
- Reference simulator and deterministic tests.

### Changed

- Replaced the earlier "lowest qualifying bid wins" auction-window design with **first qualifying sealed offer wins** to prioritize dispatch speed.
- Clarified that manual numerical bidding should not be required while a driver is operating a vehicle.
- Clarified that pickup consent can be provided prospectively through passenger-configured distance/cost limits instead of requiring a separate modal for every qualifying pickup.
