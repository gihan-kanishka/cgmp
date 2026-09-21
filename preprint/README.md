# CGMP Preprints

This directory contains publication-oriented CGMP design preprints.

## Current version

**CGMP v1.4-preprint** is the current working publication version.

Primary source:

- [`CGMP-v1.4-preprint.md`](./CGMP-v1.4-preprint.md)

Historical sources:

- `CGMP-v1.2-preprint.md`
- `CGMP-v1.1-preprint.md`
- `CGMP-v1.0-preprint.md`

Zenodo submission metadata:

- `ZENODO_SUBMISSION.md`

## v1.4 focus

v1.4 replaces the earlier reference tariff and fallback architecture with the current pre-pilot design:

- Bike **Rs 22/km**
- Tuk **Rs 37/km**
- Mini **Rs 52/km**
- Compact **Rs 57/km**
- Sedan **Rs 65/km**
- passenger-trip time **Rs 12.90/minute**
- platform commission **7%**
- **2 km** minimum passenger-trip component
- **2 km** minimum pickup component
- no pickup-time charge
- no automatic demand/supply surge multiplier
- no discretionary driver-bidding fallback
- passenger-authorized pickup search in 2 km increments
- passenger-cancellation pickup compensation under published grace/no-show rules
- visible billing pause for driver personal stops
- class-based tariffs where individual efficiency savings remain with the driver
- progressive long-distance displacement treatment beginning after **40 passenger km**
- end-of-trip reconciliation limited to the provisional long-distance component
- cash-commission ledger with a published settlement threshold

Exact long-distance marginal rates, cancellation grace/no-show timing and the cash settlement threshold remain pilot/deployment calibration items.

## Recommended validation path

1. Freeze the ordinary tariff for controlled pilot testing.
2. Publish the progressive post-40 km long-distance schedule before charging it.
3. Validate representative class-cost inputs with dated component evidence.
4. Measure pickup acceptance by both distance and time.
5. Measure driver paid-trip earnings and whole online-hour earnings separately.
6. Measure platform sustainability at 7% commission.
7. Measure return-direction matching and post-dropoff utilization at 6, 12 and 24 hours.
8. Validate meter-integrity, personal-stop, cancellation and cash-ledger controls before broad deployment.
9. Complete local legal/regulatory review before commercial deployment.

Reference software remains Apache-2.0. Documentation/specification/preprint remains CC BY 4.0 unless otherwise stated.
