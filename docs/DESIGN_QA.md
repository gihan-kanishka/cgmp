# CGMP v1.4 - Frequently Raised Design Questions

## Why is pickup time not billed?
Pickup distance compensates vehicle deployment while the passenger already bears waiting time. Acceptance is still measured against pickup minutes because slow distant pickups may be unattractive.

## Why retain a 2 km pickup minimum?
It provides a minimum deployment payment and forms the minimum-service structure together with the 2 km passenger component. It remains a pilot-calibration parameter.

## Why no driver bidding or surge?
CGMP keeps ordinary pricing deterministic. If authorized search fails, the request may remain unmatched rather than automatically converting scarcity into a higher passenger price.

## Why can traffic still raise the fare?
Legitimate passenger-trip time is paid at Rs 12.90/minute. No surge means no automatic demand/supply scarcity multiplier, not free driver time.

## Why do efficiency gains remain with the driver?
The class tariff is based on representative class economics. A more efficient vehicle retains its lower-cost advantage.

## What happens if the passenger cancels during pickup?
After the published grace rule, validated pickup compensation already earned can be debited from the passenger and credited to the driver. No passenger-trip distance or time is charged if the passenger trip never begins.

## What happens during a driver personal stop?
The driver must pause time billing. Both apps display the pause and resume state. Legitimate traffic remains billable; personal time does not.

## Why does long-distance treatment begin after 40 km?
The first 40 passenger kilometres remain ordinary service. Beyond 40 km, displacement compensation begins progressively so there is no retrospective threshold jump.

## Why reconcile the long-distance amount at trip end?
The live amount is provisional. Final distance and eligibility become authoritative at completion. Only the long-distance component is adjusted; the legitimate ordinary meter is not clawed back.

## Does the passenger pay for an empty return?
No. Long-distance compensation follows a one-day displacement principle and depends on empirical return/local-work outcomes rather than assuming every driver returns empty.

## Can 7% support the platform?
That remains empirical. Payment, maps, communications, support, fraud, engineering, compliance and dispute-resolution costs must be measured at realistic volume.
