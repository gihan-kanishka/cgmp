# Driver Planning and Scheduled-Trip Access - v1.4

## Purpose

This optional module helps position future supply without changing ordinary CGMP live-trip pricing or deterministic live dispatch.

It has exactly two premium-driver benefits:

1. **advance demand-pattern forecasts**; and
2. **priority access to scheduled-trip opportunities**.

Premium membership does **not** change:

- ordinary live-trip dispatch priority;
- published live-trip fares;
- platform commission;
- pickup-search treatment;
- long-distance incentive calculations; or
- cancellation, meter-integrity, or cash-settlement rules.

The premium product sells planning information and earlier access to future scheduled work, not preferential treatment in ordinary live dispatch.

## 1. Advance demand-pattern forecasts

Premium drivers may receive future demand forecasts, including day-prior forecasts where sufficient information exists.

Forecast inputs may include:

- historical trip patterns by area, weekday and time;
- weather forecasts;
- school opening and closing times;
- scheduled train or public-transport arrivals;
- major events;
- current and expected driver availability; and
- already committed scheduled-trip capacity.

Forecasts should be presented as probabilistic planning information rather than guaranteed demand.

Where practical, the platform should make forecasts **supply-aware**. A high-demand area should not continue to be promoted as an opportunity when predicted available supply is already sufficient.

A useful planning quantity is:

```text
expected_opportunity(zone, time)
    = expected_demand(zone, time)
    - expected_available_service_capacity(zone, time)
```

This is not a fare multiplier and does not change passenger pricing.

## 2. Scheduled-trip priority access

Passengers may create trips for future pickup.

Scheduled trips may first be exposed to eligible premium drivers during a **published premium-priority access window**.

If the trip remains unclaimed after that window, it is automatically forwarded to eligible regular drivers.

The priority window is an implementation parameter and must not be configured in a way that jeopardizes assignment before the passenger's scheduled pickup time.

Premium access is therefore **priority access, not exclusivity**.

## 3. Fair rotation of qualifying long-distance scheduled trips

Qualifying high-value or long-distance scheduled opportunities may use a configurable fairness lookback `L_fair` so that a small number of drivers do not repeatedly capture unusually attractive scheduled work.

A production deployment must publish the qualifying rule. It may use passenger-trip distance, expected duration, expected fare value, displacement burden, or another auditable criterion. v1.4 does not invent a permanent threshold before pilot evidence exists.

The fairness lookback is a **configurable, published deployment parameter**. A reference value such as 7 days may be tested, but the effective deployed value should be calibrated from allocation concentration, trip frequency, driver availability and passenger fulfilment.

When the rule is enabled:

- a driver who completed a qualifying scheduled trip during the previous `L_fair` days may be temporarily deprioritized while another otherwise eligible driver without a recent qualifying trip is available;
- drivers without a recent qualifying trip are considered first within their access pool;
- among otherwise equivalent drivers, least-recently-served ordering may be used; and
- if no alternative driver is available or accepts, the restriction is relaxed so passenger fulfilment is not sacrificed.

A reference opportunity order is:

```text
premium drivers without a recent qualifying trip
    ->
regular drivers without a recent qualifying trip
    ->
recently served eligible drivers
```

The rule governs access to scheduled opportunities only. It does not change the passenger's ordinary meter or long-distance tariff.

## 4. Scheduled commitments and supply forecasts

A driver committed to a future scheduled trip should not be counted as freely available capacity during the expected occupied interval.

Therefore:

```text
expected_available_supply
    = predicted_online_supply
    - scheduled_commitments
    - expected_busy_capacity
```

This lets scheduled-trip commitments improve the quality of later demand-pattern forecasts.

## 5. Monitoring

A pilot should measure:

- scheduled-trip fill rate;
- premium-window fill rate;
- percentage of scheduled trips forwarded to regular drivers;
- time from scheduled-trip publication to commitment;
- scheduled-trip cancellation and no-show rate;
- distribution of qualifying scheduled trips across eligible drivers;
- repeated allocation concentration;
- fairness-rule override frequency caused by lack of alternative supply;
- forecast error by zone and time window;
- driver repositioning following forecasts;
- whether forecast-driven repositioning improves future match rates; and
- whether forecasts create driver herding or oversupply.

## 6. Governance

The following must be published and versioned before production use:

- premium subscription benefits;
- premium-priority window policy;
- qualifying scheduled-trip fairness rule;
- configured fairness lookback `L_fair` when enabled;
- fairness ordering and availability override; and
- forecast methodology at a level sufficient for audit without exposing security-sensitive implementation details.

Changes must not be made silently or per-driver. No additional premium benefit should be implied unless it is separately specified.
