# Cost-Grounded Mobility Pricing (CGMP)

## A transparent metered-fare, progressive-search and long-distance displacement framework for ride-hailing

**Version:** 1.4-preprint  
**Date:** 2026-09-21  
**Status:** Design preprint; empirical calibration and live-pilot validation pending  
**Creator:** CGMP Project  
**Project maintainer / publication custodian:** gihan-kanishka  
**AI assistance:** OpenAI ChatGPT (GPT-5.6 Sol)

## Abstract

Cost-Grounded Mobility Pricing (CGMP) is an open ride-hailing pricing and dispatch framework built around a published digital taxi meter rather than an upfront quoted fare.

The ordinary tariff combines a vehicle-class distance rate with explicit passenger-trip time compensation. Pickup distance is compensated at the same vehicle-class distance rate, while pickup time is not separately charged. The current working class rates are Bike Rs 22/km, Tuk Rs 37/km, Mini Rs 52/km, Compact Rs 57/km and Sedan Rs 65/km. The passenger-trip time rate is Rs 12.90/minute and the platform commission is 7% of passenger-paid fare components.

CGMP does not show a platform-generated final-fare estimate in the reference design. Before booking, the passenger sees the published Rs/km and Rs/min tariff, the pickup rule, and any applicable long-distance incentive percentage. During the passenger trip, a server-validated live meter accumulates the charge from actual distance and verified passenger-trip time.

For passenger trips beyond 40 km, CGMP adds a deterministic **long-distance displacement component**. It accrues progressively per qualifying passenger kilometre under published distance bands and is shown as provisional during the trip. At completion the server reconciles only this long-distance component against the authoritative final distance, destination and eligible route/arrival conditions. The ordinary distance and legitimate passenger-time meter is not clawed back. The displacement component is not described as fuel, food, accommodation, lost wages, or guaranteed empty-return reimbursement.

Ordinary dispatch remains deterministic and progressively expands the pickup search with passenger authorization. The v1.4 reference framework does not use a discretionary driver-bidding premium or a demand/supply surge multiplier.

## 1. Design objective

Ride-hailing pricing should distinguish the economic reasons for payment instead of combining them inside an opaque multiplier.

CGMP therefore separates four functions:

1. **vehicle use**, compensated by distance;
2. **driver productive passenger-trip time**, compensated by minute;
3. **vehicle deployment to the passenger**, compensated by pickup distance; and
4. **exceptional destination displacement**, compensated by a published long-distance incentive when applicable.

The core design principle is:

> Distance pays for vehicle use; passenger-trip time pays for the human; long-distance incentive compensates temporary destination displacement.

The governance principle is:

> Costs set the economic floor; competition may tune the margin above that floor, but the published tariff is not changed dynamically because demand is temporarily high.

The long-distance objective is deliberately bounded:

> Trip length should not create a systematic economic penalty for the driver, but one passenger should not be required to finance a guaranteed empty return journey.

CGMP therefore targets economic comparability on average, not a guaranteed identical profit for every trip.

## 2. Related literature and positioning

CGMP is not based on the claim that dynamic or surge pricing is economically irrational. Castillo (2025) estimates welfare effects of surge pricing in ride hailing, while Miao et al. (2023) document heterogeneous driver responses to surge incentives. Hall, Horton, and Knoepfle (2023) show that ride-hailing markets can re-equilibrate after fare changes, including changes in driver hours and utilization. These results motivate measuring equilibrium responses rather than assuming that a posted tariff permanently determines hourly earnings.

Auction and negotiated-fare mechanisms are established prior art. Buchholz et al. (2025), Pueboobpaphan, Indra-Payoong, and Opasanon (2019), Egan and Jakob (2016), and Rammohan, Marathe, and Sudarsanam (2022) demonstrate that market-clearing mechanisms can be designed in different ways. CGMP v1.4 deliberately does **not** use driver bidding as the reference fallback. The framework instead keeps the ordinary price deterministic and treats persistent unmatched demand as an operational supply/search problem to be measured.

Driver acceptance remains a central operational variable. Ashkrof et al. (2025) examine the consequences of driver ride-acceptance decisions for ride-sourcing operations, while Zhang et al. (2026) analyze centralized driver-accept and auto-accept matching systems.

CGMP's safety rationale is intentionally limited. Hussain and Alhajyaseen (2025) and Snober et al. (2024) report riskier driving behavior under experimentally induced time pressure. These studies support testing whether explicit passenger-trip time compensation changes incentives; they do not establish that CGMP will improve real-world safety.

The proposed contribution of CGMP is therefore the combination of published cost-grounded class rates, explicit passenger-trip labour compensation, paid pickup distance, a live digital meter, passenger-controlled progressive search, no automatic scarcity multiplier, deterministic cancellation and pause-state handling, and progressive long-distance displacement compensation beginning after 40 km.

## 3. Core metered fare

Let:

- `d_t` = passenger-trip distance;
- `d_p` = actual authorized pickup distance;
- `D_min` = minimum passenger-trip distance;
- `P_min` = minimum billed pickup component;
- `r_c` = passenger-facing distance rate for vehicle class `c`;
- `t_b` = verified billable passenger-trip time;
- `r_t` = passenger-facing passenger-trip time rate;
- `I_L` = final long-distance displacement component, if applicable.

The ordinary meter is:

```text
F_meter =
  [max(d_t, D_min) + max(d_p, P_min)] * r_c
  + t_b * r_t
```

The final passenger fare before separately identified third-party charges is:

```text
F_final = F_meter + I_L
```

Current reference settings are:

```text
D_min = 2 km
P_min = 2 km
r_t = Rs 12.90/minute
platform commission = 7%
long-distance qualification begins after 40 km passenger distance
```

The 2 km passenger minimum and 2 km pickup minimum are minimum billed service components. Above the pickup minimum, actual authorized pickup distance is billed; search-band size does not determine the billed pickup distance.

### 3.1 Current distance calibration

| Class | Provisional routine ICE cost/km | Working passenger distance rate |
|---|---:|---:|
| Bike | ~Rs 10.00 | **Rs 22.00/km** |
| Tuk | Rs 22.10 | **Rs 37.00/km** |
| Mini | Rs 32.80 | **Rs 52.00/km** |
| Compact | Rs 34.00 | **Rs 57.00/km** |
| Sedan | Rs 36.10 | **Rs 65.00/km** |

Let `C_c` be representative class routine economic cost/km, `H_c >= 0` competitive and working-condition headroom/km, and `gamma` the platform commission rate.

The vehicle-distance economic floor is:

```text
R_floor_c = C_c / (1 - gamma)
```

A working published rate may be represented as:

```text
R_c >= (C_c + H_c) / (1 - gamma)
```

with the final published value chosen as a simple transparent class tariff. Headroom is not part of the economic floor. It is the margin above the representative cost floor used for competition, vehicle-capital differences, working conditions and occupational exposure.

The representative class cost is a calibration input, not an individual reimbursement. A driver who operates a more fuel-efficient, lower-maintenance, hybrid or electric vehicle retains that efficiency gain; the platform does not reduce that driver's tariff individually.

At the 25 km/h illustration, the Rs 12.90/minute time component equals Rs 30.96 per passenger-trip kilometre. At 40 km/h it equals Rs 19.35 per passenger-trip kilometre.

For a 13 km passenger trip plus 2 km pickup, ordinary metered fares are:

| Class | At 25 km/h | At 40 km/h |
|---|---:|---:|
| Bike | Rs 732.48 | Rs 581.55 |
| Tuk | Rs 957.48 | Rs 806.55 |
| Mini | Rs 1,182.48 | Rs 1,031.55 |
| Compact | Rs 1,257.48 | Rs 1,106.55 |
| Sedan | Rs 1,377.48 | Rs 1,226.55 |

These speeds are illustrations, not production pricing speeds.

## 4. Passenger disclosure and the digital meter

CGMP v1.4 does **not** provide a platform-generated upfront final-fare estimate in the reference design.

Before booking, the passenger is shown at minimum:

- the vehicle-class Rs/km rate;
- the common Rs/min passenger-trip time rate;
- the minimum and actual pickup-distance charging rule;
- confirmation that ordinary pricing has no demand/supply surge multiplier;
- the long-distance displacement schedule when the planned trip may exceed 40 km; and
- any provisional route/arrival condition relevant to long-distance reconciliation.

The passenger agrees to the published tariff rather than to an estimated final amount. The interface should make the time rule understandable, for example by stating that every additional 10 billable passenger minutes adds Rs 129.

During the passenger trip, the application should show a live accumulated meter with separable distance, time, pickup and provisional long-distance components. The authoritative calculation is server-side.

## 5. Economic calibration without hidden complexity

The current class cost figures are provisional aggregate modelling assumptions. A production deployment should publish dated inputs used to derive representative routine cost/km, including fuel or energy, tyres, scheduled service, brakes/suspension/repairs and other defined routine wear.

The tariff is class-based. Individual efficiency gains belong to the operator. A representative ICE cost may therefore set a conservative class floor while an efficient motorcycle, hybrid or EV retains a higher operator margin.

Competitive headroom is a calibration variable above the floor and may also recognize class-specific working conditions. In particular, motorcycle work exposes riders more directly to weather and crash injury risk than enclosed vehicles; CGMP does not reduce Bike pricing merely because the vehicle itself is inexpensive to operate.

The current approximately Rs 12/minute net labour target is a passenger-trip labour benchmark, not a guarantee of Rs 720 per online hour. Actual online-hour earnings depend on passenger-carrying utilization, pickup time, idle time, cancellations, return-trip matching and market equilibrium.

## 6. Pickup and progressive deterministic search

Stage 1 searches within **0-2 km**. If unmatched, search expands in fixed **2 km increments**:

```text
0-2 km -> 2-4 km -> 4-6 km -> 6-8 km -> ...
```

The passenger may authorize each expansion directly or use saved limits.

Search bands determine candidate eligibility, not billed distance. The minimum pickup component is 2 km; above it, the actual authorized pickup distance is billed. A candidate 3.2 km away therefore produces a 3.2 km pickup-distance charge, not 4 km.

The driver interface should make clear that billed pickup distance is compensated at the normal class distance rate. CGMP does not add a discretionary "driver is far away" premium solely because search expands.

### 6.1 Pickup time policy

Pickup time is intentionally not monetized. The passenger already bears a real pre-trip cost through waiting. CGMP compensates vehicle deployment through pickup distance but does not additionally charge pickup minutes.

This does not assume pickup time is valueless to the driver. Acceptance should be measured against both pickup kilometres and pickup minutes, because congested long pickups may remain unattractive even when their distance is paid.

### 6.2 Passenger cancellation and no-show settlement

If a passenger cancels after the driver has accepted and materially begun travelling toward the pickup, the passenger is charged the **validated pickup component earned up to cancellation**, according to the published cancellation policy, and the driver is compensated from that amount. No passenger-trip distance or passenger-trip time charge is added because the passenger trip did not begin.

If the driver has reached the authorized pickup point and the passenger cancels or becomes a no-show after the published grace period, the full authorized pickup component may become payable. If the driver cancels, fails to make reasonable progress, or the cancellation is attributable to driver/platform fault, the passenger is not charged.

A short cancellation grace mechanism may protect passengers from nuisance charges immediately after matching. Exact grace timing is a pilot-calibration parameter. Repeated same-driver/same-passenger cancellation patterns should be monitored for abuse.

### 6.3 If expanded search still fails

CGMP v1.4 does not use a discretionary driver-bidding premium or platform-selected scarcity multiplier as the reference fallback. If the authorized search limit is exhausted without an accepting driver, the request may remain unmatched or enter a clearly identified retry/rematch flow at the same published tariff.

## 7. Passenger-trip time, pauses and meter integrity

Billable passenger-trip time begins at the server-recorded passenger-trip start and ends at the server-recorded trip end, excluding explicit non-billable pause states.

Traffic lights, ordinary congestion, road closures and passenger-requested waiting remain billable because they consume legitimate passenger-trip time. Driver-initiated personal stops do not.

### 7.1 Driver personal-stop pause

For a driver personal stop, refuelling stop or other driver-originated interruption, the driver must select **Pause billing - personal stop**. Both apps immediately display a clear notification such as:

```text
Time billing paused by driver
Personal stop - passenger time is not being charged
```

When service resumes, both apps display **Time billing resumed**. A visible paused-time counter should be retained in the trip record.

If the personal stop includes an off-route detour, the corresponding driver-personal distance should also be excluded from the passenger's bill. The server should not automatically pause merely because the vehicle is stationary, because genuine traffic remains billable. Telemetry may instead prompt the driver when a likely personal stop is detected.

### 7.2 Meter integrity and meter-farming controls

The platform should validate time and distance using server timestamps, trip state, GPS/route evidence and available traffic context. Controls should detect implausible route prolongation, unnecessary loops, unexplained off-route stationary periods and repeated excess-duration patterns without assuming that every slow trip is abuse.

A single abnormal trip should normally trigger evidence collection or review rather than automatic guilt. Repeated statistically unusual patterns are stronger evidence. Passenger-requested detours and stops should be recorded as explicit trip events.

## 8. Long-distance displacement component

### 8.1 Purpose and 40 km threshold

The ordinary meter applies through the first **40 km of passenger distance**. Long-distance displacement compensation begins only for passenger kilometres beyond 40 km.

Its purpose is to reduce the structural disadvantage of ending far outside the driver's normal operating area while avoiding a rule that makes the outbound passenger finance a guaranteed empty return journey.

The component is not labelled or administered as fuel reimbursement, food reimbursement, accommodation reimbursement, lost wages or guaranteed round-trip compensation.

### 8.2 Progressive per-kilometre accrual

Long-distance compensation must accrue progressively rather than appearing as a retrospective lump sum when a threshold is crossed.

Let published long-distance bands begin above 40 km. For each band `b`, let `lambda_b` be the published displacement add-on per passenger kilometre (or an equivalent published percentage of the class distance rate converted to a per-kilometre add-on). Let `k_b` be the passenger kilometres actually accumulated inside that band.

```text
I_L_provisional = sum_b(lambda_b * k_b)
```

Only kilometres actually inside a band receive that band's rate. Adding distance must never reduce the fare and crossing a band boundary must not reprice earlier kilometres.

The exact post-40 km band rates remain a pilot-calibration item and should not be inferred from the obsolete v1.3 whole-trip percentage table.

### 8.3 Provisional display and end-of-trip reconciliation

The long-distance component accrues visibly during the trip and is labelled **provisional** until trip completion.

At completion, the server determines the authoritative final passenger distance, destination and eligible pre-published route/arrival conditions. If the provisional long-distance amount exceeds final entitlement, only the excess long-distance component is deducted. If it is short, only the required long-distance shortfall is added. Legitimate ordinary distance and passenger-time charges are not clawed back.

Arrival-related modifiers should be based principally on server-estimated conditions disclosed at commitment, not on driver-controlled lateness, so a driver cannot gain both additional time revenue and a higher displacement rate by travelling slowly.

Material destination changes require explicit recalculation. Consecutive same-passenger/same-driver trips that function as one continuous journey may be treated as a single journey for long-distance eligibility so the 40 km threshold cannot be trivially avoided by trip splitting.

### 8.4 One-day displacement principle

The displacement component compensates temporary destination displacement for up to one day. After a qualifying trip the driver may return immediately, work locally, stay overnight, combine the journey with personal activity, or accept another trip.

The component is not clawed back merely because a profitable return trip is quickly found. Conversely, the original passenger does not become liable for a second automatic charge merely because no return trip appears.

For up to **24 hours after long-distance drop-off**, the platform should, where operationally feasible, improve the displaced driver's visibility of suitable trips moving toward the driver's normal operating area or original corridor.

Key pilot measures are return-direction matches within **6, 12 and 24 hours**, paid versus unpaid post-drop-off kilometres, and productive versus idle post-drop-off time.

### 8.5 Motorcycle long-distance acceptance

Long motorcycle journeys create sustained weather, fatigue and road-risk exposure beyond vehicle operating cost alone. Qualifying Bike long-distance work should therefore remain explicitly driver-opt-in and may use published safety or duty-duration limits without changing the ordinary Bike tariff dynamically.

## 9. Commission, cash settlement and third-party charges

The platform commission is **7% of all passenger-paid CGMP fare components**, including pickup distance, passenger-trip distance, passenger-trip time and long-distance displacement compensation.

### 9.1 Cash commission ledger and settlement threshold

For a cash trip, the passenger may pay the driver the full passenger fare. The driver's platform ledger then records the 7% commission as a negative platform balance. Electronic-trip proceeds may automatically offset that balance, and the driver may settle it directly.

The deployment must publish a **negative-balance settlement threshold** and a warning threshold. When the maximum negative balance is reached, the driver should stop receiving new cash trips but may continue receiving eligible electronic-payment trips so the debt can be worked down. Cash-trip eligibility is restored when the balance returns below the permitted threshold.

The exact threshold is a pilot-calibration variable and should reflect fraud exposure, typical trip value, driver earnings and settlement behaviour rather than being hidden or discretionary.

### 9.2 Third-party charges

If an exact third-party amount must reach the driver or third party intact, such as a defined toll reimbursement, the passenger-facing charge may need to be grossed up so the intended external amount remains after the 7% deduction. The implementation must disclose this treatment rather than silently leaving the driver short.

## 10. Optional driver-planning and scheduled-trip module

CGMP retains an optional driver-planning module outside the core fare and live-dispatch mechanism.

Premium driver membership has two reference benefits:

1. **advance demand-pattern forecasts**; and
2. **priority access to scheduled-trip opportunities**.

Premium membership does not change ordinary live-trip fares, commission or the long-distance incentive calculation.

### 10.1 Advance demand-pattern forecasts

Premium drivers may receive future demand forecasts where sufficient information exists.

Possible inputs include historical trip patterns, weather forecasts, school opening/closing times, scheduled public-transport arrivals, major events, expected driver availability and already committed scheduled-trip capacity.

Forecasts are probabilistic planning information, not guaranteed demand and not a passenger-fare multiplier.

Where practical, the forecast should be supply-aware:

```text
expected opportunity
    = expected demand
    - expected available service capacity
```

### 10.2 Scheduled-trip priority access

Scheduled trips may first be exposed to eligible premium drivers during a published premium-priority access window. If a trip remains unclaimed, it is forwarded to eligible regular drivers.

Premium access is therefore priority access rather than exclusivity.

### 10.3 Fair rotation of qualifying long-distance scheduled trips

Qualifying high-value long-distance scheduled opportunities may use a configurable fairness lookback `L_fair`. The reference default remains **7 days**, but the deployed value and qualifying threshold must be objective, published and recalibrated from observed trip frequency, allocation concentration, driver availability and passenger fulfilment.

A recently served driver may be deprioritized while another otherwise eligible driver without a recent qualifying trip is available. If no other driver is available or accepts, the restriction is relaxed so passenger fulfilment is not sacrificed.

## 11. Monitoring and pilot calibration

CGMP v1.4 treats the following as measurement questions:

- deterministic acceptance and rejection;
- acceptance by pickup distance **and pickup time**;
- total request-to-match time;
- passenger abandonment by search stage;
- unmatched-request rate after authorized expansion;
- driver paid-trip earnings versus online-hour earnings;
- passenger-carrying utilization;
- platform sustainability at 7%;
- payment-processing cost as a share of gross fare;
- cash-ledger debt distribution and settlement time;
- cancellation/no-show frequency and cancellation-compensation amounts;
- speeding/aggressive-driving indicators;
- unexplained excess passenger-trip time;
- personal-stop pause frequency and disputed pauses;
- post-acceptance driver cancellation;
- passenger rematch or abandonment after cancellation;
- long-distance acceptance by vehicle class, distance, destination and planned arrival condition;
- provisional-to-final long-distance reconciliation amounts;
- suspected trip splitting around the 40 km threshold;
- post-long-distance local utilization;
- return-direction match within 6, 12 and 24 hours;
- paid versus unpaid kilometres after long-distance drop-off;
- long-distance displacement component as a share of fare; and
- passenger acceptance/complaint rates for long-distance trips.

Long-distance rates should be recalibrated from observed **post-drop-off utilization**, not from an assumption that every driver returns empty.

A pilot should separately report passenger-trip economics and whole-duty-period economics. Competitor benchmarking should use standardized routes and observed traffic/time-of-day conditions rather than a single reference speed.

## 12. Limitations

The reference class cost values remain provisional until backed by a published dated component dataset.

The approximately Rs 12/minute net passenger-trip labour target remains a working benchmark rather than a demonstrated equilibrium wage.

The sustainability of a 7% commission remains unproven and must be tested against payment, mapping, communications, support, fraud, engineering, compliance and dispute-resolution costs. Fixed-subscription competitors may be cheaper for very high-volume drivers even when CGMP produces stronger per-trip economics.

The exact progressive long-distance rates above 40 km are not yet empirically final. The crucial unknown is destination-specific post-drop-off utilization and return-direction matching probability by time of day, day of week and vehicle class.

Pickup time may reduce driver willingness to accept expanded pickups even though it is intentionally not charged. Passenger cancellation rules require a calibrated grace period and abuse controls. Cash settlement requires a calibrated negative-balance threshold.

Explicit trip-time pricing may reduce some time pressure while creating an incentive to prolong journeys. Server-side meter validation, pause-state logging and anomaly detection are therefore production-critical.

The absence of a discretionary price fallback means some requests can remain unmatched during severe shortages. CGMP v1.4 treats that outcome as visible evidence about supply/search/tariff adequacy rather than automatically resolving it with a hidden scarcity multiplier.

Legal and regulatory compatibility must be validated before deployment in each operating jurisdiction.

## 13. Conclusion

CGMP v1.4 has a deliberately transparent pricing and dispatch core:

1. Bike Rs22/km, Tuk Rs37/km, Mini Rs52/km, Compact Rs57/km and Sedan Rs65/km;
2. explicit Rs12.90/min billable passenger-trip time compensation;
3. a 2 km minimum passenger-trip and 2 km pickup minimum;
4. actual authorized pickup-distance billing above the minimum;
5. no pickup-time charge;
6. deterministic cancellation/no-show pickup compensation;
7. explicit personal-stop billing pauses visible to both parties;
8. a server-authoritative live digital meter with anti-meter-farming controls;
9. no platform-generated upfront final-fare estimate;
10. no automatic supply-demand surge multiplier;
11. deterministic passenger-authorized progressive search;
12. no discretionary driver-bidding premium in the reference framework;
13. progressive long-distance displacement compensation beginning after 40 km;
14. provisional long-distance accrual with end-of-trip reconciliation limited to that component;
15. a one-day destination-displacement principle rather than guaranteed empty-return economics;
16. class tariffs that allow individual vehicle-efficiency gains to remain with the operator;
17. a consistent 7% commission across passenger-paid CGMP components; and
18. a cash commission ledger with a published settlement threshold.

The ordinary tariff has reached a stable pre-pilot calibration. The largest remaining pricing task is empirical calibration of the progressive post-40 km long-distance schedule. The largest operational tasks are cancellation implementation, pause-state integrity, anti-meter-farming controls, cash-ledger settlement and return-direction matching.

## Appendix A. Frequently Raised Design Questions

### A.1 Why does CGMP not show an upfront final-fare estimate?

The passenger agrees to a published tariff rather than to a guessed final amount. Actual metered distance and verified billable passenger time determine the ordinary fare. The interface can still explain deterministic sensitivity, such as "every additional 10 billable minutes adds Rs129."

### A.2 Why is pickup time not charged?

Pickup distance compensates vehicle deployment, while pickup time is intentionally not billed because the passenger is already waiting before service begins. Acceptance by both pickup kilometres and pickup minutes must nevertheless be measured.

### A.3 Why retain a 2 km pickup minimum?

It functions as a minimum deployment component rather than a claim that every driver physically travels 2 km. Above the minimum, actual authorized pickup distance is billed. Pilot data should verify whether this minimum remains competitive and sufficient for driver acceptance.

### A.4 What happens if the passenger cancels after the driver starts approaching?

The passenger is charged the validated pickup component earned under the published cancellation policy, and the driver is compensated from it. Driver/platform-fault cancellations are not charged to the passenger. A short cancellation grace period remains a calibration item.

### A.5 Why can congestion increase the fare if there is no surge pricing?

CGMP does not apply an automatic supply-demand scarcity multiplier. Congestion can still increase fare because legitimate passenger-trip time is explicitly paid.

### A.6 What happens when the driver needs fuel or another personal stop?

The driver pauses billing with a visible personal-stop state. Both parties are notified, time billing stops, and any driver-personal off-route distance is excluded. Passenger-requested waiting and ordinary traffic remain billable.

### A.7 How does CGMP deter meter farming?

The server validates timestamps, route/GPS evidence, trip states, pause events and available traffic context. Repeated unexplained loops, detours or excess-duration patterns can be flagged without treating every slow trip as abuse.

### A.8 When does long-distance compensation begin?

After **40 km of passenger distance**. The first 40 km use the ordinary CGMP meter only.

### A.9 Why does long-distance compensation accrue per kilometre?

Progressive per-kilometre bands avoid fare cliffs. Crossing 40 km or another band boundary affects only the kilometres that actually fall inside the new band and never reprices earlier kilometres.

### A.10 Why is the long-distance component provisional during the trip?

The planned destination and route determine the disclosed working schedule, but the final trip may end early or change. At trip end the server reconciles only the long-distance component against authoritative final conditions. Ordinary legitimate distance and time are not clawed back.

### A.11 Does the long-distance component pay for a guaranteed empty return?

No. It compensates temporary displacement while preserving the possibility of local work or a paid return-direction trip. The original passenger does not automatically finance a second journey back.

### A.12 What if the driver immediately finds a return trip?

The displacement amount is not clawed back merely because a useful return opportunity appears. Likewise, the passenger is not charged extra later if no return trip appears.

### A.13 Can passengers split a long trip into several short trips to avoid the 40 km rule?

Consecutive same-passenger/same-driver journeys that function as one continuous journey may be treated as one journey for long-distance eligibility. The exact continuity window must be published and auditable.

### A.14 Why do efficient vehicles keep the savings?

The tariff is class-based and calibrated against a representative vehicle. Individual fuel, maintenance, hybrid or EV efficiency gains belong to the operator rather than being confiscated through individual repricing.

### A.15 Does Rs12 per paid minute mean Rs720 per online hour?

No. It is a passenger-trip labour benchmark. Online-hour earnings also depend on pickup time, idle time, cancellations and return-trip opportunities.

### A.16 Can a platform operate sustainably at 7% commission?

That remains an empirical question. Real payment, mapping, communications, support, fraud, engineering, compliance and dispute-resolution costs must be measured at realistic volume.

### A.17 How are cash-trip commissions collected?

The driver receives the cash fare and the 7% commission becomes a negative platform-ledger balance. Electronic-trip proceeds or direct settlement reduce the debt. At the published settlement threshold, new cash trips are restricted until the balance recovers.

### A.18 What is the most important long-distance pilot metric?

Post-drop-off utilization: whether drivers obtain useful local or return-direction work within 6, 12 and 24 hours, together with paid and unpaid kilometres and idle time.

### A.19 Why forecast demand instead of using passenger-price surge?

Forecasting can help drivers reposition before shortages without changing passenger tariffs. Forecasts are planning information, not guaranteed demand and not a passenger-fare multiplier.

## References

1. Castillo, J. C. (2025). Who Benefits From Surge Pricing? *Econometrica*, 93(5), 1811-1854. https://doi.org/10.3982/ECTA19106
2. Miao, W., Deng, Y., Wang, W., Liu, Y., & Tang, C. S. (2023). The effects of surge pricing on driver behavior in the ride-sharing market: Evidence from a quasi-experiment. *Journal of Operations Management*, 69(5), 794-822. https://doi.org/10.1002/joom.1223
3. Hall, J. V., Horton, J. J., & Knoepfle, D. T. (2023). Ride-Sharing Markets Re-Equilibrate. NBER Working Paper 30883. https://doi.org/10.3386/w30883
4. Buchholz, N., Doval, L., Kastl, J., Matejka, F., & Salz, T. (2025). Personalized Pricing and the Value of Time: Evidence From Auctioned Cab Rides. *Econometrica*, 93(3), 929-958. https://doi.org/10.3982/ECTA18838
5. Pueboobpaphan, S., Indra-Payoong, N., & Opasanon, S. (2019). Experimental analysis of variable surcharge policy of taxi service auction. *Transport Policy*, 76, 134-148. https://doi.org/10.1016/j.tranpol.2017.12.002
6. Egan, M., & Jakob, M. (2016). Market mechanism design for profitable on-demand transport services. *Transportation Research Part B: Methodological*, 89, 178-195. https://doi.org/10.1016/j.trb.2016.04.020
7. Rammohan, S., Marathe, R. R., & Sudarsanam, N. (2022). Profitable market mechanism for platform-based aggregator taxi services. *Transportation Research Interdisciplinary Perspectives*, 16, 100687. https://doi.org/10.1016/j.trip.2022.100687
8. Ashkrof, P., Ghasemi, F., Kucharski, R., Homem de Almeida Correia, G., Cats, O., & van Arem, B. (2025). The implications of drivers' ride acceptance decisions on the operations of ride-sourcing platforms. *Transportation Research Part A: Policy and Practice*, 192, 104362. https://doi.org/10.1016/j.tra.2024.104362
9. Zhang, X., Miao, W., Chu, J., & Png, I. (2026). The Design of Centralized Matching Systems on Two-Sided Platforms: Evidence from the Ride-Hailing Market. *Marketing Science*, published online 3 March 2026. https://doi.org/10.1287/mksc.2023.0561
10. Hussain, Q., & Alhajyaseen, W. K. M. (2025). Driving against the clock: Investigating the impacts of time pressure on taxi and non-professional drivers' safety and compliance. *Accident Analysis & Prevention*, 210, 107864. https://doi.org/10.1016/j.aap.2024.107864
11. Snober, H., Al-Malki, A., Elias, M., Saqallah, M., Badran, M., Kutmawi, Y., Alhajyaseen, W. K. M., & Hussain, Q. (2024). Time Pressure's Impact on Taxi Drivers' Driving Speed: A Driving Simulator Study. *Procedia Computer Science*, 231, 96-102. https://doi.org/10.1016/j.procs.2023.12.180

## Attribution and AI-use disclosure

**Formal creator:** CGMP Project. **Project maintainer and publication custodian:** gihan-kanishka.

OpenAI ChatGPT (GPT-5.6 Sol) was used extensively for formalization of the pricing and dispatch architecture, technical and economic analysis, literature synthesis, reference-code development, documentation and manuscript drafting. Human contribution included conceptual direction, requirements, design decisions, review and authorization of the public release.

The AI system is not an author and cannot assume responsibility for the work; publication responsibility remains with the human project maintainer. For citation purposes, use **CGMP Project** as the creator.