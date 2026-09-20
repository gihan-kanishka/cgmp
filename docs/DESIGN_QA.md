# CGMP v1.2 - Frequently Raised Design Questions

This document records recurring design questions about the CGMP v1.2 reference architecture. It is explanatory material, not a separate layer of pricing rules.

## 1. Why is pickup time not compensated separately?

Pickup distance is paid at the vehicle-class distance rate, but pickup time is intentionally not billed. Before the ride starts, the passenger already bears the service cost of waiting for the vehicle. CGMP therefore does not add another monetary charge for those pre-trip minutes.

This does not assume pickup time has no value to the driver. Acceptance by pickup-distance band, total matching time, passenger abandonment and fallback activation are measured so the policy can be revisited if evidence shows a material problem.

## 2. Why use first-qualifying fallback instead of waiting for the cheapest bid?

Stage 3 is not the normal price-discovery mechanism. It is reached only after the initial deterministic search and passenger-authorized deterministic expansion have failed.

At that point the objective is rapid market clearing within a passenger-defined private affordability limit. Waiting for a bidding window could produce a lower price, but would deliberately add delay to an already difficult request. v1.2 therefore keeps first-qualifying clearing and measures its price and latency consequences.

## 3. Could drivers reject ordinary trips in the hope of reaching a premium fallback?

Yes, that behavior is theoretically possible.

v1.2 does not assume it will be material and does not preemptively ban rejecters from later fallback participation. Instead, the platform measures deterministic rejection, later participation on the same request, fallback activation and repeated reject-then-premium patterns.

A same-request exclusion rule can be tested later if evidence shows that gaming is large enough to justify the additional restriction.

## 4. Why does CGMP say it avoids surge pricing when congestion can still increase the fare?

CGMP does not claim that the fare is unaffected by traffic.

The narrower claim is that the ordinary tariff does not automatically apply a supply-demand scarcity multiplier. Congestion can increase the fare because legitimate passenger-trip time is an explicit paid component.

The cause of the increase is therefore measurable trip time rather than a hidden scarcity coefficient.

## 5. If CGMP is cost-grounded, why can vehicle headroom change with competitor fares?

Representative ICE operating economics and the labour target define the economic floor. Class-specific vehicle headroom is the competitive margin above that floor.

Competitive calibration is therefore allowed, but only through scheduled, versioned review using standardized ordinary/non-scarcity competitor fares. It must not become a real-time demand-sensitive price control and must not push the tariff below the economic floor.

## 6. Why are EV operating costs not used to lower the class tariff?

The reference tariff is calibrated from representative ICE class economics.

An EV, hybrid or unusually efficient combustion vehicle can provide the same service at a lower operating cost. CGMP allows the owner to retain that efficiency gain instead of using the lowest-cost drivetrain to reset the passenger rate for the entire class.

## 7. Does Rs 12 per paid minute mean a driver earns Rs 720 per online hour?

No.

Rs 12/minute is the current net labour target during the passenger trip. Actual online-hour earnings also depend on passenger-carrying utilization, pickup time, idle time, acceptance, cancellations and market conditions.

CGMP therefore measures paid-trip earnings and online-hour earnings separately.

## 8. What happens if fallback premiums drift upward over time?

v1.2 measures the fallback premium distribution, the distance between clearing offers and passenger ceilings, fallback activation and repeated driver behavior.

It does not add a premium cap before evidence shows that price drift is material. If persistent drift appears, a cap or alternative clearing rule can be tested as a targeted response.

## 9. Does Stage 3 guarantee that a passenger will get a ride?

No.

Stage 3 provides a final market-clearing opportunity when deterministic dispatch fails. A trip can still remain unmatched if there is no willing driver or if all driver offers exceed the passenger's private limit.

The mechanism improves the set of possible matches; it cannot create vehicle supply that does not exist.

## 10. Can a platform operate sustainably at a 7% commission?

The 7% rate is a current working parameter, not a proven guarantee of platform profitability.

A production deployment must test whether 7% covers its actual payment, mapping, communications, support, fraud, engineering, compliance and dispute-resolution costs at realistic trip volumes.

## 11. Why does CGMP not solve every theoretical problem in advance?

Every additional rule creates its own costs, incentives and failure modes.

v1.2 therefore follows a deliberate anti-over-engineering principle:

> Measure uncertain behavioral problems before adding new pricing or dispatch rules.

Premium caps, rejecter bans, auction waiting windows, pickup-time fractions and latency handicaps remain possible experimental controls, but they are not part of the reference mechanism unless simulation or pilot evidence demonstrates a material need.
