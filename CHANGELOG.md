# Changelog

## v1.2-preprint — 2026-09-20

v1.2 is a simplification/governance revision. Core fare values are unchanged from v1.1.

### Clarified core policy

- Explicitly retained **no pickup-time charge**.
- Documented the rationale: the passenger already bears pre-trip waiting, while pickup vehicle movement is compensated by distance.
- Defined billable passenger-trip time as server-validated trip-start to trip-end time, excluding pickup.
- Clarified that congestion may raise the deterministic fare through real trip time; the claim is **no automatic scarcity multiplier**, not "no multiplier of any kind."
- Defined upfront fares in the reference model as estimates and the final fare as metered using verified passenger-trip time.

### Calibration governance

- Kept representative ICE economics as the tariff basis.
- Added an explicit cost-component structure for fuel, tyres, servicing, routine repairs and wear.
- Marked the current aggregate ICE cost figures as provisional until a dated empirical component breakdown is published.
- Restricted competitive headroom tuning to **scheduled periodic review** using standardized ordinary/non-scarcity competitor fares.
- Prohibited real-time competitor-price following.

### Gross/net definitions

- Defined deterministic baselines, passenger ceilings and fallback bids as **gross passenger-facing values**.
- Defined driver-specific `F0_i` because pickup distance varies by candidate driver.
- Defined `M_i` as the passenger's private rule applied to `F0_i`.
- Applied 7% commission to distance, passenger-trip time and fallback premium.
- Allowed separately identified direct third-party/pass-through costs to be commission-exempt.

### Anti-over-engineering

- Removed preemptive corrective controls from the reference core.
- No automatic same-request rejecter ban.
- No fallback premium cap.
- No lowest-offer auction window.
- No latency handicap.
- These remain testable future controls only if evidence shows a material problem.
- Expanded monitoring to include total request-to-match time, abandonment by stage, premium distributions, ceiling proximity and reject-then-fallback behavior.

### Design Q&A

- Added `docs/DESIGN_QA.md` and **Appendix A: Frequently Raised Design Questions** to the v1.2 preprint.
- The Q&A explains recurring objections without introducing new pricing rules.
- Explicitly distinguishes Stage 3 as a final market-clearing opportunity rather than a guarantee of vehicle availability.
- Reiterates that 7% commission sustainability, pickup acceptance, premium drift and reject-and-wait behavior remain empirical questions.

### Independent-review clarifications

- Defined the vehicle-distance economic floor explicitly as `R_floor_c = C_c / (1 - gamma)`.
- Defined the published rate separately as `R_c = roundUp_0.50((C_c + H_c)/(1-gamma))`, making clear that competitive headroom `H_c` is **not** part of the floor.
- Stated the billing increment explicitly: rates round upward to the next **Rs 0.50/km**.
- Added **no platform-selected default fallback ceiling**; Stage 3 requires an explicit or saved passenger ceiling rule.
- Added post-acceptance driver cancellation and multi-homing-related reliability metrics to monitoring.

### Premium driver planning and scheduled trips

- Added optional premium-driver planning module with exactly two benefits: **advance demand-pattern forecasts** and **priority access to scheduled trips**.
- Explicitly kept ordinary live-trip fares, commission, dispatch priority and Stage 3 treatment identical for premium and regular drivers.
- Scheduled trips unclaimed during the premium-priority window are automatically forwarded to regular drivers.
- Added a configurable fairness rotation `L_fair` for qualifying high-value long-distance scheduled trips, with **7 days as the v1.2 reference default rather than a fixed rule**.
- Drivers with no qualifying long-distance trip in the configured lookback receive priority over recently served drivers; recently served drivers remain available as a fulfilment fallback.
- Required the effective fairness lookback to be published/versioned and added lookback sensitivity to validation.
- Added least-recently-served ordering within equivalent candidate pools.
- Added supply-aware forecast guidance and scheduled-commitment accounting as optional planning features.
- Added validation metrics for forecast accuracy, herding, scheduled-trip fill, allocation concentration and fairness overrides.

### Literature

- Restored paper-by-paper positioning in the v1.2 preprint.
- Corrected the Zhang et al. reference to the current INFORMS publisher citation status: *Marketing Science*, 0(0), published online 3 March 2026.

## v1.1-preprint — 2026-09-20

### Fare calibration

- Changed passenger time rate from Rs 12.00/min to **Rs 12.90/min**, targeting approximately Rs 12.00/min net driver labour after 7% commission.
- Recalibrated passenger distance rates from representative ICE routine-cost assumptions and class-specific net vehicle headroom:
  - Bike: **Rs 19.00/km**
  - Tuk: **Rs 37.00/km**
  - Mini: **Rs 51.50/km**
  - Compact: **Rs 53.00/km**
  - Sedan: **Rs 61.50/km**
- Current provisional net vehicle headroom targets after commission:
  - Bike Rs 3/km
  - Tuk Rs 12/km
  - Mini Rs 15/km
  - Compact Rs 15/km
  - Sedan Rs 21/km
- Defined class headroom as a **competitive calibration variable** that may be tuned against standardized competitor fares while preserving the economic floor.
- Defined representative ICE economics as the tariff benchmark; EV or unusually efficient vehicle costs do not set passenger rates.

### Minimum fare and pickup

- Set the minimum passenger-trip distance to **2 km**.
- Included the first **2 km pickup** in the minimum-fare structure.
- Set the initial search radius to **2 km**.
- Set search expansion to fixed **2 km increments**.
- Clarified that billing uses actual authorized pickup distance, not the search-band ceiling.
- Pickup time remains uncharged in the reference design.

### Dispatch

- Clarified the three-stage dispatch sequence:
  1. deterministic 0-2 km search;
  2. passenger-authorized deterministic search expansion in 2 km increments;
  3. exceptional sealed fallback only after authorized deterministic expansion fails.
- Explicitly prohibited activating sealed bidding merely because the search radius expands.
- Added passenger fallback-ceiling modes:
  - percentage above base;
  - fixed amount per passenger-trip km;
  - fixed fee by passenger-trip distance band.
- Retained **first-qualifying sealed offer wins** for the exceptional fallback stage.

### Validation and governance

- Added fallback activation rate as a system-health metric.
- Added strategic reject-and-wait behavior to simulation and pilot requirements.
- Added standardized competitor benchmark trips at 2, 5, 10, 13 and 20 km.
- Clarified that a 7% commission remains a working business assumption requiring platform-cost validation.

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
- Server-authoritative fallback offer ordering and dispatch-fairness requirements.
- Long-distance displacement policy with pre-trip passenger consent.
- Server-side integrity and repeated-abuse review principles.
- Reference simulator and deterministic tests.
