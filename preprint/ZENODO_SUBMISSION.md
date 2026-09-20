# Zenodo submission metadata - CGMP v1.1

## Required fields

**Resource type:** Publication -> Preprint

**Title:** Cost-Grounded Mobility Pricing (CGMP): A Cost-Grounded Fare, Progressive-Search and Exceptional-Dispatch Framework for Ride-Hailing

**Publication date:** 2026-09-20

**Version:** v1.1-preprint

**Creator:** CGMP Project

**Creator type:** Organization / project

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Access:** Open

**Project maintainer / publication custodian:** gihan-kanishka (not the formal creator)

**AI assistance disclosure:** OpenAI ChatGPT (GPT-5.6 Sol) was used extensively for formalization, technical and economic analysis, literature synthesis, reference-code development, documentation and manuscript drafting. Human contribution included conceptual direction, requirements, design decisions, review and authorization of the public release. The AI system is not an author; publication responsibility remains with the human project maintainer.

## Abstract / description

Cost-Grounded Mobility Pricing (CGMP) is an open ride-hailing pricing and dispatch framework that separates ordinary trip pricing, passenger-authorized search expansion, and exceptional scarcity resolution. Passenger distance rates are calibrated from representative ICE class economics and class-specific competitive headroom, while a 7% platform commission is explicitly grossed into the tariff. The current passenger time rate of Rs 12.90/minute targets approximately Rs 12/minute net driver labour after commission.

Dispatch begins with a deterministic 0-2 km search. If no match is obtained, the passenger can authorize search expansion in 2 km increments; expanded pickup remains deterministically priced at actual authorized distance. Sealed bidding is disabled during these stages. Only after the authorized deterministic expanded-search process fails can a private passenger ceiling and private automated driver offers be used. The first server-valid qualifying offer clears immediately.

Competitive passenger fares may tune class-specific vehicle headroom above the economic floor, but may not push the tariff below representative ICE operating cost, the published labour target, and disclosed platform economics. The framework is presented as a testable design proposal rather than a proven replacement for dynamic pricing.

## Keywords

- ride-hailing
- ride-sourcing
- transport economics
- mobility pricing
- market design
- progressive search
- pickup pricing
- sealed bidding
- dispatch
- driver incentives
- platform governance
- gig economy

## Related identifier

**Project repository:** https://github.com/gihan-kanishka/cgmp

## Recommended files

1. `CGMP_v1.1_preprint.pdf` - primary publication file
2. `CGMP_v1.1_preprint.docx` - editable source (optional)

The reference implementation remains separately licensed under Apache-2.0.

## DOI

Allow Zenodo to assign a DOI at publication. If a DOI is reserved in advance, it may be inserted into the final PDF before publication.

## Notes

- Design preprint; strategic simulation and live controlled-pilot validation pending.
- Preprint/documentation license: CC BY 4.0.
- Reference implementation license: Apache License 2.0.
