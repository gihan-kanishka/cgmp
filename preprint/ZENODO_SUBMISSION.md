# Zenodo submission metadata - CGMP v1.2

## Required fields

**Resource type:** Publication -> Preprint

**Title:** Cost-Grounded Mobility Pricing (CGMP): A Minimal Cost-Grounded Fare, Progressive-Search and Exceptional-Dispatch Framework for Ride-Hailing

**Publication date:** 2026-09-20

**Version:** v1.2-preprint

**Creator:** CGMP Project

**Creator type:** Organization / project

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Access:** Open

**Project maintainer / publication custodian:** gihan-kanishka (not the formal creator)

**AI assistance disclosure:** OpenAI ChatGPT (GPT-5.6 Sol) was used extensively for formalization, technical and economic analysis, literature synthesis, reference-code development, documentation and manuscript drafting. Human contribution included conceptual direction, requirements, design decisions, review and authorization of the public release. The AI system is not an author; publication responsibility remains with the human project maintainer.

## Abstract / description

Cost-Grounded Mobility Pricing (CGMP) is an open ride-hailing pricing and dispatch framework that separates ordinary trip pricing, passenger-authorized search expansion, and exceptional scarcity resolution. Passenger distance rates are calibrated from representative ICE class economics and class-specific competitive headroom, while passenger-trip time is priced explicitly. The reference calibration uses a 7% platform commission and a passenger time rate of Rs 12.90/minute, targeting approximately Rs 12/minute net during the passenger trip.

Dispatch begins with a deterministic 0-2 km search. If no match is obtained, the passenger may authorize search expansion in 2 km increments. Search bands determine candidate eligibility while actual authorized pickup distance determines billing. Pickup time is intentionally not monetized: the passenger already bears the pre-trip waiting cost and vehicle movement is compensated through pickup distance. Sealed bidding is disabled during deterministic expansion.

Only after authorized deterministic expanded search fails can a private passenger ceiling and private automated driver offers be used. Because pickup differs by candidate, the deterministic baseline `F0_i` and resulting private ceiling `M_i` may be driver-specific. The first server-valid gross passenger-facing offer satisfying `F0_i <= b_i <= M_i` clears immediately.

v1.2 deliberately avoids preemptive premium caps, rejecter bans, lowest-offer windows and latency handicaps. These remain monitoring and simulation questions unless empirical evidence demonstrates a material problem. Competitive headroom is adjusted only through scheduled review using standardized ordinary/non-scarcity competitor fares and may not cross the economic floor.

An optional premium-driver planning module provides only advance demand-pattern forecasts and priority access to scheduled trips. Unclaimed scheduled trips flow to regular drivers. Qualifying high-value long-distance scheduled trips use a configurable fairness lookback, with 7 days as the v1.2 reference default; recent recipients are deprioritized while other eligible drivers are available.

## Keywords

- ride-hailing
- ride-sourcing
- transport economics
- mobility pricing
- progressive search
- pickup pricing
- sealed bidding
- dispatch
- driver incentives
- platform governance
- market design
- gig economy

## Related identifier

**Project repository:** https://github.com/gihan-kanishka/cgmp

## Recommended files

1. `CGMP_v1.2_preprint.pdf`
2. `CGMP_v1.2_preprint.docx`

The reference implementation remains separately licensed under Apache-2.0.

## DOI

Allow Zenodo to assign a DOI at publication. If a DOI is reserved in advance, it may be inserted into the final PDF before publication.

## Notes

- The preprint includes **Appendix A: Frequently Raised Design Questions**, which explains recurring design objections without adding new fare or dispatch rules.

- Design preprint; focused strategic simulation and live controlled-pilot validation pending.
- Aggregate ICE cost inputs are provisional until dated component calibration is completed.
- Vehicle-distance economic floor and competitive headroom are explicitly separated; published distance rates round upward to Rs 0.50/km.
- Stage 3 has no platform-selected default premium or ceiling; a passenger rule must be explicitly chosen or saved.
- The long-distance scheduled-trip fairness lookback is a published, versioned deployment parameter; 7 days is the v1.2 reference default.
- Preprint/documentation license: CC BY 4.0.
- Reference implementation license: Apache License 2.0.
