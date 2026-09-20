# CGMP Preprints

This directory contains publication-oriented CGMP design preprints.

## Current version

**CGMP v1.1-preprint** is the current working publication version.

Primary source:

- `CGMP-v1.1-preprint.md`

Historical source:

- `CGMP-v1.0-preprint.md`

Zenodo submission metadata is maintained in:

- `ZENODO_SUBMISSION.md`

## Status

CGMP remains a design and simulation framework. It has not yet been validated by a live controlled pilot.

v1.1 materially revises fare calibration and dispatch sequencing:

- representative ICE economics set the tariff benchmark;
- passenger time rate is Rs 12.90/min;
- minimum trip and initial pickup allowance are both 2 km;
- search expands in 2 km increments;
- expanded search remains deterministic;
- sealed bidding is enabled only after authorized deterministic expanded search fails;
- class-specific vehicle headroom may be competitively tuned without crossing the economic floor.

## Recommended publication path

1. Run strategic simulation using the v1.1 reference implementation.
2. Publish the v1.1 design preprint on Zenodo under CC BY 4.0 when ready.
3. Keep reference software under Apache-2.0.
4. Use the Zenodo DOI in later citations and versions.
5. Follow with controlled operator pilot evidence before making superiority or safety claims.
