# Driver Planning and Scheduled-Trip Access - v1.2

## Purpose

This optional module helps position future supply without changing ordinary CGMP live-trip pricing or dispatch.

It has exactly two premium-driver benefits:

1. **advance demand-pattern forecasts**; and
2. **priority access to scheduled-trip opportunities**.

Premium membership does **not** change:

- ordinary live-trip dispatch priority;
- published live-trip fares;
- platform commission;
- Stage 1 or Stage 2 treatment;
- Stage 3 eligibility or clearing;
- fallback pricing rules.

The premium product sells planning information and earlier access to future scheduled work, not preferential treatment in ordinary live dispatch.

## 1. Advance demand-pattern forecasts

Premium drivers may receive future demand forecasts, including day-prior forecasts where sufficient information exists.

Forecast inputs may include:

- historical trip patterns by area, weekday and time;
- weather forecasts;
- school opening and closing times;
- scheduled train or public-transport arrivals;
- major events;
- current and expected driver availability;
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

Scheduled trips are first exposed to eligible premium drivers during a **published premium-priority access window**.

If the trip remains unclaimed after that window, it is automatically forwarded to eligible regular drivers.

The priority window is an implementation parameter and must not be configured in a way that jeopardizes assignment before the passenger's scheduled pickup time.

Premium access is therefore **priority access, not exclusivity**.

## 3. Fair rotation of high-value long-distance scheduled trips

High-profit long-distance scheduled trips should be distributed as fairly as practicable among otherwise eligible drivers without sacrificing passenger fulfilment.

A production deployment must publish an objective rule defining a **qualifying high-value long-distance scheduled trip**. The definition may use trip distance, expected duration, fare value or another auditable threshold. v1.2 does not invent that threshold before deployment evidence exists.

The fairness lookback is a **configurable, published deployment parameter**. The v1.2 reference default is **7 days**, but a deployment may shorten or lengthen it using observed allocation concentration, trip frequency and availability evidence.

Let `L_fair` be the configured fairness lookback in days. Then:

- a driver who completed a qualifying high-value long-distance trip during the previous `L_fair` days is temporarily deprioritized for another qualifying trip;
- drivers who have not completed such a trip during the previous `L_fair` days are considered first;
- among otherwise equivalent drivers in the same access pool, the driver least recently served by a qualifying trip receives earlier opportunity;
- if no non-recent driver is available or accepts, the restriction is relaxed and recently served drivers may receive the trip.

For qualifying high-value long-distance scheduled trips, fairness takes precedence over premium status once the relevant candidate pool is considered. The intended sequence is:

```text
premium drivers with no qualifying trip in previous L_fair days
    ->
regular drivers with no qualifying trip in previous L_fair days
    ->
recently served eligible drivers
```

This prevents the same small group of drivers from repeatedly capturing the most profitable scheduled trips while retaining an availability override when necessary.

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
- qualifying long-distance trip distribution across eligible drivers;
- repeated allocation concentration;
- fairness-rule override frequency caused by lack of alternative supply;
- forecast error by zone and time window;
- driver repositioning following forecasts;
- whether forecast-driven repositioning improves future match rates;
- whether forecasts create driver herding or oversupply.

## 6. Governance

The following must be published and versioned before production use:

- premium subscription benefits;
- premium-priority window policy;
- qualifying long-distance/high-value threshold;
- configurable fairness lookback `L_fair` and its current effective value;
- fairness ordering and availability override;
- forecast methodology at a level sufficient for audit without exposing security-sensitive implementation details.

Changes to `L_fair` should be versioned and should not be made silently or per-driver.

No additional premium benefit should be implied unless it is separately specified.
