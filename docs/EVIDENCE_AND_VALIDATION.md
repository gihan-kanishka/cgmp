# Evidence and Validation Plan - v1.2

CGMP v1.2 is a design framework, not a claim of proven superiority.

The core mechanism is intentionally kept small. Uncertain behavioral problems are measured before corrective rules are added.

## Before production calibration

Collect and publish dated evidence for:

- fuel prices by relevant fuel type;
- representative ICE fuel economy by class;
- tyre cost/life;
- scheduled servicing;
- brakes, suspension and routine repairs;
- other routine wear included in the class cost;
- fleet composition used to define a representative class;
- the economic basis for the Rs 12/min net passenger-trip labour target;
- direct platform operating costs relevant to the 7% commission.

Current aggregate ICE cost/km figures remain provisional until this breakdown exists.

## Competitor calibration

Use standardized comparable **ordinary/non-scarcity** fares.

Do not use live competitor surge observations to make real-time CGMP changes.

Benchmark at multiple trip distances and observed traffic conditions rather than relying only on the 25 km/h illustration.

Suggested distances:

- 2 km;
- 5 km;
- 10 km;
- 13 km;
- 20 km.

## Core pilot metrics

### Matching and pickup

- initial 0-2 km match rate;
- acceptance by pickup-distance band;
- match rate after each expansion stage;
- total request-to-match time;
- time spent in each stage;
- passenger abandonment/cancellation by stage;
- actual pickup-distance distribution;
- post-acceptance driver cancellation rate;
- time from driver acceptance to driver cancellation;
- passenger rematch/abandonment after driver cancellation.

### Fallback

- fallback activation rate;
- fallback premium distribution;
- clearing premium as a percentage of driver-specific `F0_i`;
- clearing-offer proximity to `M_i`;
- fallback failure rate;
- request-to-fallback time;
- fallback activation-to-assignment time;
- reject-then-fallback participation;
- network/device latency versus fallback win rate.

### Economics

- passenger fare per trip and per km;
- driver net earnings per paid passenger-trip hour;
- driver net earnings per online hour;
- passenger-carrying utilization;
- pickup time;
- idle time;
- platform contribution under 7% commission.

The distinction between paid passenger-trip earnings and online-hour earnings must remain explicit.

### Forecasting and scheduled trips

- scheduled-trip fill rate;
- premium-window fill rate;
- share of scheduled trips forwarded to regular drivers;
- time from scheduled-trip publication to commitment;
- scheduled-trip cancellation/no-show rate;
- distribution of qualifying high-value long-distance trips across eligible drivers;
- fairness-rule override rate when no alternative driver is available;
- concentration of qualifying trips by driver;
- sensitivity of fairness and fulfilment outcomes to the configured fairness lookback `L_fair`;
- forecast error by zone/time window;
- forecast-driven repositioning;
- effect of forecast-driven repositioning on later match rates;
- driver herding or oversupply caused by forecasts.

### Time and safety

- actual versus expected passenger-trip time;
- unexplained excess journey time;
- disputed time intervals;
- speeding/aggressive-driving indicators;
- slow-driving complaints.

## Simulation priorities

A toy/agent-based simulation should test only the material uncertain mechanisms first:

1. baseline acceptance versus reject-and-wait;
2. fallback with and without same-request rejecter exclusion;
3. first-qualifying clearing versus a short lowest-offer window comparator;
4. unpaid pickup-time effects on Stage 2 acceptance;
5. passenger abandonment as total matching time increases.

The simulation should not be used to justify adding controls automatically. It should identify whether a problem is large enough to deserve additional complexity.

## Decision rule

If a problem is not materially present in simulation or pilot evidence, do not add a rule for it.

That is the v1.2 anti-over-engineering principle.
