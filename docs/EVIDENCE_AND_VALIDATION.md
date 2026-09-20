# Evidence and Validation Plan - v1.1

CGMP v1.1-preprint is a design framework, not a claim of proven superiority.

## Architectural claims

The rules directly establish that:

- ordinary fares are deterministic functions of published inputs;
- current tariff calibration is based on representative ICE class economics;
- the current time rate targets approximately Rs 12/min net driver labour after 7% commission;
- the current minimum fare includes 2 km passenger distance and 2 km pickup;
- search begins within 2 km and expands in 2 km increments;
- expanded-search pickup is billed at actual authorized distance, not band ceiling;
- expanded deterministic search does not itself activate bidding;
- sealed bidding becomes eligible only after authorized deterministic expanded search fails;
- passenger fallback ceilings can remain private;
- driver offers can remain private and automated;
- the first qualifying fallback offer can clear immediately.

## Claims requiring empirical validation

A live pilot and strategic simulation are required to determine whether CGMP:

- keeps passenger fares competitive;
- provides sustainable driver net earnings;
- supports a sustainable platform at 7% commission;
- keeps fallback activation rare;
- creates strategic deterministic-offer rejection;
- changes passenger switching/cancellation behavior;
- improves or worsens matching latency;
- produces acceptable fairness under first-qualifying dispatch;
- creates network-latency allocation bias;
- changes speeding/aggressive-driving behavior;
- creates deliberate slow-driving behavior;
- improves long-distance completion.

## Economic calibration data

Before production use, collect:

- current fuel prices;
- representative ICE fuel economy by class;
- routine maintenance and wear per km;
- representative fleet composition;
- insurance/repair/irregular-loss data if a mandatory reserve is to be added;
- driver utilization and idle-time distributions;
- platform payments/maps/support/fraud/communications/engineering/compliance costs;
- competitor passenger fares for standardized benchmark trips.

EV costs may be measured for research, but they do not set the passenger tariff in the current reference design.

## Competitive calibration

Benchmark comparable trips, for example:

- 2 km;
- 5 km;
- 10 km;
- 13 km;
- 20 km.

For each benchmark, record comparable pickup, trip time, vehicle class, fees and any dynamic-price state.

Competitive observations may tune the net vehicle headroom above the economic floor.

Do not tune below the economic floor merely to match a competitor.

## Recommended pilot metrics

- passenger fare/trip and fare/km;
- effective fare at standardized trip conditions;
- driver net earnings per active hour after routine vehicle cost;
- platform contribution after direct operating costs;
- deterministic acceptance rate;
- rejection rate by driver/area/time;
- passenger and driver cancellation;
- initial 0-2 km match rate;
- match rate after each 2 km expansion;
- passenger expansion-approval rate;
- percentage of expansion handled by standing preferences;
- actual pickup-distance distribution;
- fallback activation rate;
- fallback activation-to-assignment latency;
- fallback premium relative to deterministic base;
- fallback failure rate;
- distribution of fallback assignments;
- relationship between network latency and fallback win rate;
- evidence of reject-and-wait behavior;
- speeding events and aggressive-driving complaints;
- unexplained excess journey time;
- slow-driving complaints;
- long-distance acceptance/completion.

## Strategic simulation

Before pilot deployment, simulate drivers with heterogeneous and learning strategies.

At minimum test:

- ordinary acceptance under viable baseline economics;
- reject-and-wait strategies;
- multi-homing to competitor platforms;
- passenger abandonment/switching;
- different fallback ceiling distributions;
- thin versus dense markets;
- first-qualifying latency effects.

## Safety hypothesis

Explicit time compensation may reduce the financial penalty of lawful speeds and congestion.

This is a testable hypothesis, not a proven safety benefit. The opposite incentive to prolong trips must also be measured.

## Publication standard

Adverse results should be published alongside favorable results.

A high fallback activation rate should be treated as evidence that the system requires recalibration or redesign, not as proof that scarcity premiums should simply become the new normal.
