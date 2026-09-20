# CGMP Preprints

This directory contains publication-oriented CGMP design preprints.

## Current version

**CGMP v1.2-preprint** is the current working publication version.

Primary source:

- `CGMP-v1.2-preprint.md`

Historical sources:

- `CGMP-v1.1-preprint.md`
- `CGMP-v1.0-preprint.md`

Zenodo submission metadata:

- `ZENODO_SUBMISSION.md`

## v1.2 focus

v1.2 keeps the v1.1 fare calibration and three-stage dispatch architecture but removes pressure to solve every hypothetical behavioral problem in advance.

It adds only the definitions needed to make the core reproducible:

- pickup time is explicitly not charged;
- ICE class costs require a dated component breakdown before production;
- competitive headroom is reviewed periodically using ordinary/non-scarcity competitor fares;
- billable passenger-trip time is operationally defined;
- `F0_i`, `M_i` and `b_i` are explicitly gross passenger-facing, driver-specific where pickup differs;
- commission treatment is explicit;
- uncertain strategic/latency/premium issues remain monitoring and simulation questions.

## Design Q&A appendix

The v1.2 preprint includes **Appendix A: Frequently Raised Design Questions**, covering pickup-time policy, first-qualifying fallback, reject-and-wait behavior, congestion versus scarcity, competitive headroom, EV treatment, paid-minute versus online-hour earnings, fallback premium drift, Stage 3 availability limits, 7% commission sustainability, and the anti-over-engineering principle.

The standalone repository version is available at `docs/DESIGN_QA.md`.

## Optional premium-driver planning module

v1.2 also documents an optional driver-planning module outside the core fare mechanism.

Premium membership provides only:

- advance demand-pattern forecasts; and
- priority access to scheduled trips.

It does not alter ordinary live-trip dispatch, fare, commission or Stage 3 treatment.

Unclaimed scheduled trips flow to regular drivers. Qualifying high-value long-distance scheduled trips use a 7-day fairness rotation so recent recipients are deprioritized while other eligible drivers are available.

## Recommended publication path

1. Run the focused v1.2 strategic simulation.
2. Complete the empirical ICE cost component table and labour-benchmark derivation.
3. Publish the v1.2 design preprint on Zenodo under CC BY 4.0.
4. Keep reference software under Apache-2.0.
5. Follow with controlled operator pilot evidence before making superiority or safety claims.
