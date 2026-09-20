# Cost-Grounded Mobility Pricing (CGMP)

## A cost-grounded fare, progressive-search and exceptional-dispatch framework for ride-hailing

**Version:** 1.1-preprint  
**Date:** 2026-09-20  
**Status:** Design preprint; simulation and live-pilot validation pending  
**Creator:** CGMP Project  
**Project maintainer / publication custodian:** gihan-kanishka  
**AI assistance:** OpenAI ChatGPT (GPT-5.6 Sol)

## Abstract

Cost-Grounded Mobility Pricing (CGMP) is an open ride-hailing pricing and dispatch framework that separates ordinary trip pricing, passenger-authorized search expansion, and exceptional scarcity resolution.

The ordinary fare is calculated from published vehicle-distance, verified passenger-trip time, pickup, and rule-derived long-distance displacement components. Current passenger distance rates are calibrated from representative internal-combustion-engine (ICE) class economics and class-specific competitive headroom, while a 7% platform commission is explicitly grossed into the passenger-facing tariff. The current passenger time rate of Rs 12.90/minute targets approximately Rs 12/minute net driver labour after commission.

CGMP begins with a deterministic 0-2 km vehicle search. If no match is obtained, the passenger can authorize expansion in 2 km increments, either interactively or through saved preferences. Expanded pickup remains deterministically priced using actual authorized pickup distance. Sealed bidding remains disabled during these stages. Only after the passenger-authorized deterministic expanded-search process fails can a private passenger ceiling and private automated driver offers be used. The first server-valid qualifying offer clears immediately.

Competitive platform fares may be used to tune class-specific vehicle headroom, but not to push the tariff below the economic floor. EV or unusually efficient vehicle costs do not set the passenger tariff; efficient owners retain those savings.

CGMP is a design proposal, not a claim of proven superiority over surge pricing or incumbent systems. Strategic rejection, fallback frequency, platform sustainability at 7% commission, network-latency fairness, driver safety behaviour and passenger switching should be tested through simulation and controlled field pilots.

## Related literature

CGMP does not assume that conventional dynamic pricing is economically irrational. Empirical and structural research finds that surge pricing can affect market clearing, welfare, driver labour supply, and the distribution of gains across market participants. Castillo (2025), Miao et al. (2023), and Hall, Horton, and Knoepfle (2023) provide relevant evidence on these questions.

Auction and negotiated-pricing mechanisms are also established research topics. Buchholz et al. (2025) study auctioned cab rides in which drivers bid and riders choose among price/wait-time offers. Pueboobpaphan, Indra-Payoong, and Opasanon (2019) evaluate a taxi-service double-auction surcharge mechanism. Egan and Jakob (2016) study joint routing, scheduling, and pricing for on-demand transport, while Rammohan, Marathe, and Sudarsanam (2022) analyze a name-your-own-price channel for platform taxi services.

Driver acceptance and dispatch rules materially affect platform performance. Ashkrof et al. (2025) model the consequences of driver acceptance behavior, while Zhang et al. (2026) compare driver-accept and auto-accept centralized matching systems.

The CGMP safety rationale is intentionally framed as a hypothesis. Simulator evidence reports riskier driving under time pressure among taxi and non-professional drivers (Hussain and Alhajyaseen, 2025; Snober et al., 2024). These studies do not establish that CGMP will improve road safety; they support testing whether explicit time compensation changes economic pressure around journey duration.

CGMP's proposed contribution is therefore not distance-plus-time pricing by itself. It is the integration of published ICE-based calibration, explicit labour compensation, paid pickup, passenger-controlled progressive search, an economic floor protected from competitive undercutting, and last-resort private first-qualifying sealed dispatch.

## 1. Problem statement

Ride-hailing platforms must solve at least three distinct problems:

1. price an ordinary trip;
2. find a vehicle at an acceptable pickup distance;
3. clear exceptional trips when deterministic dispatch repeatedly fails.

CGMP separates these functions operationally.

Stage 1 searches within 2 km at the deterministic CGMP fare. Stage 2 expands the search in passenger-authorized 2 km increments while retaining deterministic pricing and charging actual authorized pickup distance. Stage 3, used only after those deterministic searches fail, allows a private passenger ceiling and private automated driver offers. The first qualifying sealed offer clears immediately.

The framework also separates economic sustainability from market positioning. Representative ICE operating economics and the labour target define the floor. Class-specific headroom above that floor may be tuned against observed competitor passenger fares, provided the floor remains intact.

The objective is not to eliminate scarcity or competition. It is to confine scarcity price discovery to trips for which ordinary and expanded deterministic dispatch have demonstrably failed.

## 2. Core principle

The pricing principle is:

> Distance pays for the vehicle; time pays for the human.

The governance principle is:

> Costs set the floor; competition sets how far above the floor the tariff can reasonably sit.

Let:

- d_t = passenger-trip distance;
- d_p = actual authorized pickup distance;
- D_min = minimum passenger-trip distance;
- P_min = included initial pickup distance;
- r_c = passenger-facing distance rate for vehicle class c;
- t = verified legitimate passenger-trip duration;
- r_t = passenger-facing time rate;
- L = pre-agreed necessary long-distance displacement provision.

Then:

```text
F =
  [max(d_t, D_min) + max(d_p, P_min)] * r_c
  + t * r_t
  + L
```

The current reference settings are D_min = 2 km, P_min = 2 km, r_t = Rs 12.90/minute, and platform commission = 7%.

## 3. v1.1-preprint parameters

Current reference passenger distance rates:

| Class | Passenger distance rate |
|---|---:|
| Bike | Rs 19.00/km |
| Tuk | Rs 37.00/km |
| Mini | Rs 51.50/km |
| Compact | Rs 53.00/km |
| Sedan | Rs 61.50/km |

Passenger time rate: **Rs 12.90/minute**.

At 7% commission, Rs 12.90/minute leaves approximately Rs 12.00/minute net to the driver.

Current provisional representative routine ICE operating-cost assumptions and target net vehicle headroom are:

| Class | Routine ICE cost/km | Target net headroom/km |
|---|---:|---:|
| Bike | Rs 14.50 | Rs 3 |
| Tuk | Rs 22.10 | Rs 12 |
| Mini | Rs 32.80 | Rs 15 |
| Compact | Rs 34.00 | Rs 15 |
| Sedan | Rs 36.10 | Rs 21 |

The current passenger rate is derived from:

```text
(routine ICE cost + target net vehicle headroom) / (1 - commission)
```

and rounded upward to a transparent Rs 0.50 billing increment.

At the 25 km/h reference speed used for examples, the time component is equivalent to Rs 30.96 per passenger-trip kilometre. Effective trip rates before pickup are therefore approximately Rs 49.96/km for Bike, Rs 67.96/km for Tuk, Rs 82.46/km for Mini, Rs 83.96/km for Compact and Rs 92.46/km for Sedan.

For a 13 km passenger trip plus 2 km pickup at the same reference trip speed, the estimated passenger fares are Rs 687.48, Rs 957.48, Rs 1,174.98, Rs 1,197.48 and Rs 1,324.98 respectively.

## 4. Vehicle-cost calibration

CGMP v1.1 uses **representative ICE economics** to calibrate passenger tariffs. EV costs, unusually efficient hybrid costs, or a particular low-cost vehicle do not set the class rate. Efficient owners retain their operating-cost advantage.

The class-specific headroom above routine ICE cost is a **competitive calibration variable**, not an immutable economic constant. Standardized competitor-trip observations may be used to raise or lower that headroom so that CGMP remains commercially attractive.

Competitive tuning may not push the tariff below the economic floor. At minimum, the floor protects:

- representative ICE routine operating cost;
- the published net driver-labour target;
- the transparent commission required to operate the platform.

If future empirical loss data justify a mandatory insurance, repair or irregular-risk reserve, it should be added explicitly to the floor rather than hidden inside an arbitrary fare.

The current 7% commission is a working business parameter. Its sustainability must be tested against real payments, maps, support, fraud, communications, engineering, compliance and dispute-resolution costs.

## 5. Traffic and time

Traffic can increase a CGMP fare because legitimate passenger-trip time consumes driver labour.

This is conceptually different from increasing the fare merely because many passengers are requesting rides at once.

The current passenger-facing time rate is Rs 12.90/minute, which produces approximately Rs 12.00/minute net driver labour after 7% commission.

A passenger-facing interface should explain the causal components directly:

```text
Passenger distance
Passenger time
Pickup distance
Long-distance provision
Estimated/final total
```

The 25 km/h reference speed used in examples is an estimation benchmark, not a forced production speed. Production charging uses verified legitimate passenger-trip time.

Time pricing also creates an opposing slow-driving incentive. CGMP therefore treats both speeding and deliberate crawling as empirical risks requiring repeated-pattern telemetry analysis.

## 6. Pickup pricing and passenger preferences

CGMP first searches within **0-2 km**. The first 2 km of pickup is represented in the minimum-fare structure, so no separate passenger confirmation is required for this initial band.

If no match is obtained, the search expands in **2 km increments**:

```text
0-2 km -> 2-4 km -> 4-6 km -> 6-8 km -> ...
```

The passenger may authorize each expansion with one click or save standing preferences such as maximum automatic search radius, maximum pickup distance or maximum pickup charge.

Search bands determine which drivers are considered; they do not determine billing distance. A 3.2 km pickup is billed as 3.2 km, not 4 km.

Expanded search remains deterministic CGMP pricing. **Bidding is not activated merely because the search radius expands.**

Pickup time is not separately charged in the current reference design.

## 7. Long-distance displacement

CGMP does not guarantee a driver full round-trip economics.

The ordinary fare compensates the outbound trip. A separate provision may be added only for a necessary, rule-defined displacement cost such as accommodation, a defined meal allowance, unavoidable tolls, or another published route-specific category.

Any such provision must be rule-derived, disclosed and accepted before trip dispatch. CGMP does not automatically add hypothetical future wages, guaranteed round-trip profit or unrestricted empty-return cost.

Long-distance trips still follow the same dispatch sequence: deterministic nearby search, passenger-authorized deterministic expanded search, and only then sealed fallback if those searches fail.

A legitimate long-distance provision is part of the deterministic base fare before any sealed offer is considered.

## 8. Exceptional first-qualifying sealed dispatch

The sealed mechanism is a **last-resort recovery path**.

It becomes eligible only after:

1. the initial deterministic 0-2 km search fails;
2. the passenger authorizes one or more 2 km search expansions, directly or through saved preferences;
3. those deterministic expanded searches also fail;
4. the passenger defines a private fallback affordability ceiling.

The passenger ceiling may be expressed as:

- a percentage above deterministic base fare;
- a fixed additional amount per passenger-trip kilometre;
- a fixed additional fee by passenger-trip distance band.

The platform does not expose this ceiling to drivers.

Drivers configure private automatic fallback rules while parked or during signup. The rules may consider pickup ETA, pickup distance, trip distance, expected duration, road or terrain conditions, destination, time of day, and private minimum acceptable economics.

Let F0 be the deterministic base including actual authorized pickup and any rule-derived long-distance provision, M the passenger's private maximum, and b_i a valid private driver offer.

A bid qualifies when:

```text
F0 <= b_i <= M
```

The first qualifying offer in authoritative server order clears immediately. The passenger pays that offer, not M. A later cheaper offer does not replace an already cleared assignment.

CGMP retains first-qualifying clearing because the bid stage occurs only after deterministic nearby and expanded searches have already failed. The mechanism therefore solves a recovery problem rather than ordinary price discovery.

A driver could theoretically reject deterministic work in hope of a later premium. CGMP does not assume this risk is zero. Rejection patterns, fallback activation and passenger switching should be measured. If reject-and-wait behavior becomes material, an implementation may prevent a driver who rejected a specific deterministic request from bidding on that same request.

The intended fallback activation rate is low. A high or rising rate is a diagnostic signal that baseline calibration, supply, search policy or strategic behavior requires investigation.

## 9. Manipulation resistance

No pricing system is manipulation-proof.

CGMP constrains manipulation surfaces by making fare-critical route, pickup distance, passenger-trip distance, time, vehicle class, authorization state, deterministic-search state, fallback state and offer order server-authoritative or server-validated.

The platform should log every 2 km search stage, whether expansion was interactively or automatically authorized, actual pickup distance and charged pickup distance. Search-band ceilings must not substitute for actual pickup distance.

Strategic rejection should be monitored using deterministic-offer rejection rates, fallback activation, repeated rejection followed by premium participation, synchronized behavior and regional/time-of-day patterns.

Competitive tariff tuning is also a governance surface. Only declared competitive variables should move. The economic floor, labour target, commission disclosure, search policy and scarcity mechanism should not be silently rewritten to chase competitor prices.

## 10. Behavioural and safety hypothesis

Explicit time compensation may reduce the direct financial penalty associated with lawful speeds and congestion. Experimental driving research makes that hypothesis worth testing, but does not establish that CGMP will reduce crashes or speeding in live ride-hailing markets.

Time pricing also creates an opposing incentive to prolong trips. CGMP therefore requires telemetry-based analysis of both speeding/aggressive-driving patterns and repeated unexplained excess journey time.

The net safety effect is empirical.

## 11. Efficient vehicles and ICE tariff benchmark

CGMP prices service classes from representative ICE economics rather than from the lowest-cost drivetrain available in the class.

An EV, hybrid or unusually efficient combustion vehicle may deliver the same service at lower operating cost. That does not automatically reduce the passenger tariff. The owner retains the efficiency saving.

EV economics may still be studied for fleet strategy and driver profitability, but they do not set the published passenger rate in the current reference design.

## 12. Governance

A credible implementation should publish or make auditable:

- representative ICE cost methodology;
- class distance rates;
- class target net headroom;
- labour target and passenger time rate;
- platform commission;
- minimum trip and included pickup distance;
- 2 km search-expansion rule;
- long-distance rules;
- passenger ceiling modes;
- fallback activation rule;
- first-qualifying ordering method;
- parameter-change history;
- competitor-benchmark methodology.

Ordinary fares should not change secretly based on inferred individual willingness to pay.

Competitive observations may tune declared vehicle headroom, but the economic floor must remain intact.

## 13. Validation requirements

CGMP should not be claimed as superior without simulation and real-world evidence.

Strategic simulation should precede a live pilot and include heterogeneous drivers, reject-and-wait behavior, multi-homing to competitor platforms, passenger switching, thin and dense markets, different fallback ceiling distributions and network-latency effects.

A pilot should pre-specify metrics including:

- passenger fare per trip and per kilometre;
- standardized 2, 5, 10, 13 and 20 km competitor comparisons;
- driver net earnings per active hour after representative routine vehicle cost;
- platform contribution under 7% commission;
- deterministic acceptance and rejection;
- initial 0-2 km match rate;
- match rate after each 2 km expansion;
- expansion approval and standing-preference usage;
- actual pickup-distance distribution;
- fallback activation rate;
- fallback premium relative to deterministic base;
- fallback assignment latency and failure rate;
- relationship between device/network latency and fallback win rate;
- evidence of reject-and-wait strategies;
- passenger cancellation and switching;
- speeding/aggressive-driving events;
- unexplained excess journey time and slow-driving complaints;
- long-distance acceptance and completion.

A high fallback activation rate should be treated as evidence that ordinary calibration, supply, search policy or strategic behavior needs investigation.

Adverse results should be published alongside favorable results.

## References

1. Castillo, J. C. (2025). Who Benefits From Surge Pricing? *Econometrica*, 93(5), 1811-1854. https://doi.org/10.3982/ECTA19106
2. Miao, W., Deng, Y., Wang, W., Liu, Y., & Tang, C. S. (2023). The effects of surge pricing on driver behavior in the ride-sharing market: Evidence from a quasi-experiment. *Journal of Operations Management*, 69(5), 794-822. https://doi.org/10.1002/joom.1223
3. Hall, J. V., Horton, J. J., & Knoepfle, D. T. (2023). Ride-Sharing Markets Re-Equilibrate. NBER Working Paper 30883. https://doi.org/10.3386/w30883
4. Buchholz, N., Doval, L., Kastl, J., Matejka, F., & Salz, T. (2025). Personalized Pricing and the Value of Time: Evidence From Auctioned Cab Rides. *Econometrica*, 93(3), 929-958. https://doi.org/10.3982/ECTA18838
5. Pueboobpaphan, S., Indra-Payoong, N., & Opasanon, S. (2019). Experimental analysis of variable surcharge policy of taxi service auction. *Transport Policy*, 76, 134-148. https://doi.org/10.1016/j.tranpol.2017.12.002
6. Egan, M., & Jakob, M. (2016). Market mechanism design for profitable on-demand transport services. *Transportation Research Part B: Methodological*, 89, 178-195. https://doi.org/10.1016/j.trb.2016.04.020
7. Rammohan, S., Marathe, R. R., & Sudarsanam, N. (2022). Profitable market mechanism for platform-based aggregator taxi services. *Transportation Research Interdisciplinary Perspectives*, 16, 100687. https://doi.org/10.1016/j.trip.2022.100687
8. Ashkrof, P., Ghasemi, F., Kucharski, R., Homem de Almeida Correia, G., Cats, O., & van Arem, B. (2025). The implications of drivers' ride acceptance decisions on the operations of ride-sourcing platforms. *Transportation Research Part A: Policy and Practice*, 192, 104362. https://doi.org/10.1016/j.tra.2024.104362
9. Zhang, X., Miao, W., Chu, J., & Png, I. (2026). The Design of Centralized Matching Systems on Two-Sided Platforms: Evidence from the Ride-Hailing Market. *Marketing Science*, 45(4), 816-843. https://doi.org/10.1287/mksc.2023.0561
10. Hussain, Q., & Alhajyaseen, W. K. M. (2025). Driving against the clock: Investigating the impacts of time pressure on taxi and non-professional drivers' safety and compliance. *Accident Analysis & Prevention*, 210, 107864. https://doi.org/10.1016/j.aap.2024.107864
11. Snober, H., Al-Malki, A., Elias, M., Saqallah, M., Badran, M., Kutmawi, Y., Alhajyaseen, W. K. M., & Hussain, Q. (2024). Time Pressure's Impact on Taxi Drivers' Driving Speed: A Driving Simulator Study. *Procedia Computer Science*, 231, 96-102. https://doi.org/10.1016/j.procs.2023.12.180

## 14. Open implementation

CGMP is intended for unrestricted practical adoption under open licenses.

The reference software is published under Apache License 2.0. Documentation, specification text and this preprint are published under CC BY 4.0 unless otherwise stated.

Operators may adapt parameters to local conditions. Material deviations from the reference architecture should be identified, especially changes to the economic floor, search progression, fallback activation or passenger-ceiling privacy.

## 15. Conclusion

CGMP v1.1 separates ordinary pricing, progressive search and exceptional market clearing.

Ordinary pricing is built from representative ICE vehicle economics, an explicit labour component and published commission. The economic floor is protected; class-specific headroom may be tuned against competitor fares above that floor.

Dispatch begins with a deterministic 0-2 km search. If unmatched, the passenger may authorize 2 km search expansions while actual pickup distance remains deterministically priced. Sealed bidding stays disabled throughout those stages. Only after authorized deterministic expansion fails can the passenger's private fallback ceiling and drivers' private automated offers become active.

The first qualifying fallback offer then clears immediately. Because this rule is intentionally speed-oriented rather than minimum-price-oriented, fallback frequency, strategic rejection, price outcomes and network-latency fairness must be measured.

The framework's next stage should be strategic simulation followed by a controlled operator pilot.

## Attribution and AI-use disclosure

**Formal creator:** CGMP Project. **Project maintainer and publication custodian:** gihan-kanishka. When citing this preprint, CGMP Project should be used as the creator name.

OpenAI ChatGPT (GPT-5.6 Sol) was used extensively for formalization of the pricing and dispatch architecture, technical and economic analysis, literature synthesis, reference-code development, documentation, and manuscript drafting. Human contribution included conceptual direction, requirements, design decisions, review, and authorization of the public release.

The AI system is not an author and cannot assume responsibility for the work; publication responsibility remains with the human project maintainer.
