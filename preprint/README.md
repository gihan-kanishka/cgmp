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

## Recommended publication path

1. Run the focused v1.2 strategic simulation.
2. Complete the empirical ICE cost component table and labour-benchmark derivation.
3. Publish the v1.2 design preprint on Zenodo under CC BY 4.0.
4. Keep reference software under Apache-2.0.
5. Follow with controlled operator pilot evidence before making superiority or safety claims.
