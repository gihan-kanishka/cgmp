# Cost-Grounded Mobility Pricing (CGMP)

## A minimal cost-grounded fare, progressive-search and exceptional-dispatch framework for ride-hailing

**Version:** 1.2-preprint  
**Date:** 2026-09-20  
**Status:** Design preprint; focused strategic simulation and live-pilot validation pending  
**Creator:** CGMP Project  
**Project maintainer / publication custodian:** gihan-kanishka  
**AI assistance:** OpenAI ChatGPT (GPT-5.6 Sol)

## Abstract

Cost-Grounded Mobility Pricing (CGMP) is an open ride-hailing pricing and dispatch framework that separates ordinary fare calculation, passenger-authorized pickup-search expansion, and exceptional scarcity resolution.

The reference tariff combines a published vehicle-class distance rate with explicit passenger-trip time compensation. Current distance rates are calibrated from provisional representative internal-combustion-engine (ICE) class operating costs plus class-specific competitive headroom, grossed up for a 7% platform commission. Passenger-trip time is priced at Rs 12.90/minute, targeting approximately Rs 12/minute net to the driver after commission.

Dispatch begins with a deterministic 0-2 km search. If no match is obtained, the passenger may authorize expansion in 2 km increments. Search-band size controls candidate eligibility; actual authorized pickup distance determines billing. Pickup time is intentionally not monetized in the reference design. Sealed bidding remains disabled throughout deterministic expansion.

Only after authorized deterministic expanded search fails may a private passenger affordability rule and private automated driver offers be used. Because candidate pickup distances differ, the deterministic baseline `F0_i` and the corresponding private passenger ceiling `M_i` may be driver-specific. The first server-valid gross passenger-facing offer satisfying `F0_i <= b_i <= M_i` clears immediately.

v1.2 deliberately avoids adding preemptive premium caps, same-request rejecter bans, auction waiting windows, pickup-time fractions or latency handicaps. These are treated as empirical questions to be measured in simulation and pilots before additional complexity is introduced.

## 1. Design objective

Ride-hailing systems simultaneously need to price ordinary transport, locate an acceptable vehicle, and handle requests that fail to attract supply.

CGMP separates these functions:

1. **ordinary deterministic pricing**;
2. **passenger-authorized deterministic search expansion**;
3. **exceptional private market clearing only after deterministic search fails**.

The design principle is:

> Distance pays for vehicle use; passenger-trip time pays for the human.

The governance principle is:

> Costs set the economic floor; competition may tune the margin above that floor.

The v1.2 anti-over-engineering principle is:

> Measure uncertain behavioral problems before adding new pricing or dispatch rules.

## 2. Related literature and positioning

CGMP is not based on the claim that dynamic or surge pricing is economically irrational. Castillo (2025) estimates welfare effects of surge pricing in ride hailing, while Miao et al. (2023) document heterogeneous driver responses to surge incentives. Hall, Horton, and Knoepfle (2023) show that ride-hailing markets can re-equilibrate after fare changes, including changes in driver hours and utilization. These results motivate measuring equilibrium responses rather than assuming a posted tariff permanently determines hourly earnings.

Auction and negotiated-fare mechanisms are also established prior art. Buchholz et al. (2025) study auctioned cab rides in which riders choose among price and waiting-time offers. Pueboobpaphan, Indra-Payoong, and Opasanon (2019) experimentally evaluate a taxi auction in which passengers and drivers bid surcharges relative to a regular meter fare. Their mechanism is particularly relevant to CGMP because both designs preserve a regular fare as a reference point and add market-based adjustment. CGMP differs by keeping ordinary and expanded pickup search deterministic, keeping the passenger ceiling private, supporting automated private driver rules, and activating bidding only after passenger-authorized deterministic search has failed.

Egan and Jakob (2016) study market-mechanism design for profitable on-demand transport, while Rammohan, Marathe, and Sudarsanam (2022) analyze a name-your-own-price channel for platform taxi services. These papers demonstrate that market clearing and pricing rules can be designed jointly rather than treated as a single opaque price multiplier.

Driver acceptance is a central operational variable. Ashkrof et al. (2025) examine the consequences of driver ride-acceptance decisions for ride-sourcing operations. Zhang et al. (2026) analyze centralized driver-accept and auto-accept matching systems, emphasizing the tradeoff between driver autonomy and matching efficiency.

CGMP's safety rationale is intentionally limited. Hussain and Alhajyaseen (2025) and Snober et al. (2024) report riskier driving behavior under experimentally induced time pressure. These studies support testing whether explicit passenger-trip time compensation changes incentives; they do not establish that CGMP will improve real-world safety.

The proposed contribution of CGMP is therefore not distance-plus-time pricing by itself. It is the combination of published ICE-based cost calibration, explicit passenger-trip labour compensation, paid pickup distance, passenger-controlled progressive search, protected economic floors, and exceptional private first-qualifying market clearing.

## 3. Core fare

Let:

- `d_t` = passenger-trip distance;
- `d_p` = actual authorized pickup distance;
- `D_min` = minimum passenger-trip distance;
- `P_min` = included pickup distance;
- `r_c` = passenger-facing distance rate for class `c`;
- `t` = verified passenger-trip duration;
- `r_t` = passenger-facing time rate;
- `L` = pre-agreed long-distance provision.

The reference fare is:

```text
F =
  [max(d_t, D_min) + max(d_p, P_min)] * r_c
  + t * r_t
  + L
```

Current settings are:

```text
D_min = 2 km
P_min = 2 km
r_t = Rs 12.90/minute
platform commission = 7%
```

### 3.1 Current distance calibration

| Class | Provisional routine ICE cost/km | Target net headroom/km | Passenger distance rate |
|---|---:|---:|---:|
| Bike | Rs 14.50 | Rs 3 | Rs 19.00/km |
| Tuk | Rs 22.10 | Rs 12 | Rs 37.00/km |
| Mini | Rs 32.80 | Rs 15 | Rs 51.50/km |
| Compact | Rs 34.00 | Rs 15 | Rs 53.00/km |
| Sedan | Rs 36.10 | Rs 21 | Rs 61.50/km |

The passenger distance rate is derived from:

```text
(routine ICE cost/km + target net vehicle headroom/km)
/
(1 - commission)
```

and rounded upward to the published billing increment.

At the 25 km/h reference speed used only for examples, the Rs 12.90/minute time component equals Rs 30.96 per passenger-trip kilometre.

For a 13 km passenger trip plus 2 km pickup at that reference trip speed, estimated passenger fares are:

| Class | Estimated fare |
|---|---:|
| Bike | Rs 687.48 |
| Tuk | Rs 957.48 |
| Mini | Rs 1,174.98 |
| Compact | Rs 1,197.48 |
| Sedan | Rs 1,324.98 |

The 25 km/h value is not a production pricing speed.

## 4. Economic calibration without hidden complexity

The current ICE cost figures are provisional aggregate modelling assumptions.

A production deployment should publish the dated inputs used to derive:

```text
routine ICE cost/km =
    fuel cost/km
  + tyres/km
  + scheduled service/km
  + brakes/suspension/repairs/km
  + other defined routine wear/km
```

The project should not invent a detailed component table before appropriate fleet evidence is collected.

EV and unusually efficient vehicle costs do not set the class passenger tariff. Owners of lower-cost vehicles retain their efficiency advantage.

The class-specific headroom is a competitive calibration variable above the economic floor. It may be reviewed against standardized competitor fares, but the review must be scheduled and versioned rather than dynamic. Competitor scarcity/surge observations should not be used to change CGMP rates in real time.

The current Rs 12/minute net labour target is a passenger-trip labour benchmark, not a guarantee of Rs 720 per online hour. Actual hourly earnings depend on passenger-carrying utilization, pickup time, idle time and market equilibrium. Those outcomes require measurement.

## 5. Pickup and progressive deterministic search

Stage 1 searches within **0-2 km**.

If unmatched, Stage 2 expands in fixed **2 km increments**:

```text
0-2 km -> 2-4 km -> 4-6 km -> 6-8 km -> ...
```

The passenger may authorize each expansion directly or use saved limits.

Search bands determine candidate eligibility, not billed distance. A candidate 3.2 km away produces a 3.2 km pickup charge rather than a 4 km charge.

### 5.1 Pickup time policy

Pickup time is intentionally not monetized.

The passenger already bears a real pre-trip cost through waiting. CGMP compensates vehicle deployment through pickup distance but does not additionally charge the passenger for pickup minutes before the service begins.

This policy does not assume pickup time is valueless to the driver. Its practical effect must be measured using pickup-distance acceptance, total match time, abandonment and fallback activation.

v1.2 does not add a pickup-time fraction before evidence shows that such complexity is required.

## 6. Passenger-trip time

Billable time begins at the server-recorded passenger-trip start and ends at the server-recorded trip end.

Pickup time is excluded.

The platform should validate the interval using server timestamps, trip state and route/GPS evidence. Implausible or disputed intervals are flagged for review.

The reference v1.2 model is metered: the upfront display is an estimate using expected route/time, while the final fare uses verified actual passenger-trip time. A deployment that guarantees a fixed upfront price is a documented implementation variant.

Congestion can therefore increase the deterministic fare because it consumes legitimate passenger-trip time. CGMP's claim is **no automatic supply-demand scarcity multiplier**, not that traffic can never affect price.

## 7. Exceptional first-qualifying sealed dispatch

Stage 3 becomes eligible only after passenger-authorized deterministic expanded search fails.

Because pickup varies by candidate, define:

- `F0_i`: gross passenger-facing deterministic fare for candidate driver `i`;
- `M_i`: private passenger maximum produced by applying the passenger's chosen rule to `F0_i`;
- `b_i`: candidate `i`'s gross passenger-facing fallback offer.

Supported passenger ceiling rules may include:

- percentage above base;
- fixed additional amount per passenger-trip kilometre;
- fixed additional fee by trip-distance band.

An offer qualifies when:

```text
F0_i <= b_i <= M_i
```

The first server-valid qualifying offer in authoritative order clears immediately.

The passenger pays the clearing offer, not automatically the ceiling.

Driver rules may be automated from preferences configured while parked. A moving driver should not be required to type a numerical bid.

### 7.1 What v1.2 does not add

The reference mechanism does not preemptively include:

- a same-request rejecter ban;
- a maximum fallback premium;
- a lowest-offer waiting window;
- a network-latency handicap.

These are possible experimental controls if evidence later shows a material problem.

## 8. Gross/net and commission treatment

Published rates, deterministic baselines and fallback offers are gross passenger-facing values.

The 7% commission applies to commissionable fare components:

- distance;
- passenger-trip time;
- fallback premium.

A separately identified direct third-party/pass-through expense may be commission-exempt, for example an actual toll or explicitly reimbursed accommodation cost.

This distinction prevents an expense reimbursement from being treated automatically as platform revenue.

## 9. Long-distance displacement

CGMP compensates the outbound service but does not guarantee a profitable round trip.

A pre-agreed long-distance provision may cover a defined unavoidable cost such as an actual toll, accommodation when immediate safe return is unreasonable, a published stay allowance or another defined route-specific expense.

CGMP does not automatically add full empty-return economics, hypothetical future wages or guaranteed round-trip profit.

Any provision must be disclosed before acceptance and incorporated into the candidate-specific deterministic baseline before fallback.

## 10. Monitoring instead of speculative controls

v1.2 treats the following as measurement questions:

- deterministic acceptance and rejection;
- acceptance by pickup-distance band;
- total request-to-match time;
- passenger abandonment by stage;
- fallback activation rate;
- fallback premium distribution;
- clearing-offer proximity to the passenger ceiling;
- repeated reject-then-fallback participation;
- network/device latency versus fallback win rate;
- driver paid-trip earnings versus online-hour earnings;
- passenger-carrying utilization;
- platform sustainability at 7%;
- speeding/aggressive-driving indicators;
- unexplained excess passenger-trip time.

A high fallback activation rate is not a success metric. It signals that baseline calibration, supply, search design or strategic behavior should be investigated.

If a hypothesized problem is not materially present, no corrective rule should be added merely because it is theoretically possible.

## 11. Focused simulation and pilot design

The first simulation should compare only a small number of material uncertainties:

1. baseline acceptance versus reject-and-wait strategies;
2. fallback with and without same-request rejecter exclusion;
3. first-qualifying clearing versus a short lowest-offer window;
4. unpaid pickup-time effects on expanded-search acceptance;
5. passenger abandonment as total matching time increases.

A pilot should separately report paid passenger-trip earnings and online-hour earnings. This is necessary because a passenger-trip labour rate does not determine utilization.

Competitor benchmarking should use standardized trip distances across observed traffic/time-of-day conditions rather than only the 25 km/h illustration.

## 12. Limitations

The reference class cost values have not yet been backed by a published dated component dataset.

The Rs 12/minute net labour target remains a working benchmark rather than a demonstrated equilibrium wage.

The sustainability of a 7% commission remains unproven.

First-qualifying fallback may create premium drift or latency-related allocation differences.

Pickup time may reduce driver willingness to accept expanded pickups even though it is intentionally not charged.

Explicit trip-time pricing may reduce some time pressure while creating an incentive to prolong journeys.

These are empirical limitations, not claims resolved by the specification.

## 13. Conclusion

CGMP v1.2 retains a small operational core:

1. published class distance rates;
2. explicit passenger-trip time compensation;
3. 2 km minimum trip and included pickup;
4. passenger-controlled 2 km search expansion;
5. actual pickup-distance billing;
6. no pickup-time charge;
7. protected economic floor;
8. periodic rather than dynamic competitive calibration;
9. exceptional first-qualifying fallback only after deterministic search fails;
10. transparent 7% commission treatment.

The purpose of v1.2 is not to anticipate every possible strategic response. It is to make the core mechanism reproducible and leave uncertain behavior to simulation and pilot evidence.

## References

1. Castillo, J. C. (2025). Who Benefits From Surge Pricing? *Econometrica*, 93(5), 1811-1854. https://doi.org/10.3982/ECTA19106
2. Miao, W., Deng, Y., Wang, W., Liu, Y., & Tang, C. S. (2023). The effects of surge pricing on driver behavior in the ride-sharing market: Evidence from a quasi-experiment. *Journal of Operations Management*, 69(5), 794-822. https://doi.org/10.1002/joom.1223
3. Hall, J. V., Horton, J. J., & Knoepfle, D. T. (2023). Ride-Sharing Markets Re-Equilibrate. NBER Working Paper 30883. https://doi.org/10.3386/w30883
4. Buchholz, N., Doval, L., Kastl, J., Matejka, F., & Salz, T. (2025). Personalized Pricing and the Value of Time: Evidence From Auctioned Cab Rides. *Econometrica*, 93(3), 929-958. https://doi.org/10.3982/ECTA18838
5. Pueboobpaphan, S., Indra-Payoong, N., & Opasanon, S. (2019). Experimental analysis of variable surcharge policy of taxi service auction. *Transport Policy*, 76, 134-148. https://doi.org/10.1016/j.tranpol.2017.12.002
6. Egan, M., & Jakob, M. (2016). Market mechanism design for profitable on-demand transport services. *Transportation Research Part B: Methodological*, 89, 178-195. https://doi.org/10.1016/j.trb.2016.04.020
7. Rammohan, S., Marathe, R. R., & Sudarsanam, N. (2022). Profitable market mechanism for platform-based aggregator taxi services. *Transportation Research Interdisciplinary Perspectives*, 16, 100687. https://doi.org/10.1016/j.trip.2022.100687
8. Ashkrof, P., Ghasemi, F., Kucharski, R., Homem de Almeida Correia, G., Cats, O., & van Arem, B. (2025). The implications of drivers' ride acceptance decisions on the operations of ride-sourcing platforms. *Transportation Research Part A: Policy and Practice*, 192, 104362. https://doi.org/10.1016/j.tra.2024.104362
9. Zhang, X., Miao, W., Chu, J., & Png, I. (2026). The Design of Centralized Matching Systems on Two-Sided Platforms: Evidence from the Ride-Hailing Market. *Marketing Science*, 0(0), published online 3 March 2026. https://doi.org/10.1287/mksc.2023.0561
10. Hussain, Q., & Alhajyaseen, W. K. M. (2025). Driving against the clock: Investigating the impacts of time pressure on taxi and non-professional drivers' safety and compliance. *Accident Analysis & Prevention*, 210, 107864. https://doi.org/10.1016/j.aap.2024.107864
11. Snober, H., Al-Malki, A., Elias, M., Saqallah, M., Badran, M., Kutmawi, Y., Alhajyaseen, W. K. M., & Hussain, Q. (2024). Time Pressure's Impact on Taxi Drivers' Driving Speed: A Driving Simulator Study. *Procedia Computer Science*, 231, 96-102. https://doi.org/10.1016/j.procs.2023.12.180

## Attribution and AI-use disclosure

**Formal creator:** CGMP Project. **Project maintainer and publication custodian:** gihan-kanishka.

OpenAI ChatGPT (GPT-5.6 Sol) was used extensively for formalization of the pricing and dispatch architecture, technical and economic analysis, literature synthesis, reference-code development, documentation and manuscript drafting. Human contribution included conceptual direction, requirements, design decisions, review and authorization of the public release.

The AI system is not an author and cannot assume responsibility for the work; publication responsibility remains with the human project maintainer. For citation purposes, use **CGMP Project** as the creator.
