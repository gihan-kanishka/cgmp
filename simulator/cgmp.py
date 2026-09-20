"""Reference calculator for CGMP v1.4-preprint.

The implementation mirrors the current transparent reference design:
- fixed published class rates;
- 2 km passenger and pickup minimum components;
- Rs 12.90/min billable passenger-trip time;
- no pickup-time charge, surge multiplier, or driver bidding;
- progressive long-distance accrual after 40 passenger km;
- end-of-trip reconciliation of the provisional long-distance component;
- passenger-cancellation pickup settlement;
- cash-commission ledger threshold helpers.
"""

from dataclasses import dataclass
from typing import Iterable, Optional

DEFAULT_COMMISSION_RATE = 0.07
DEFAULT_TIME_RATE_PER_MIN = 12.90
TARGET_NET_LABOUR_PER_MIN = 12.0
MINIMUM_TRIP_KM = 2.0
MINIMUM_PICKUP_KM = 2.0
SEARCH_BAND_KM = 2.0
LONG_DISTANCE_THRESHOLD_KM = 40.0
REFERENCE_SPEED_KMPH = 25.0


@dataclass(frozen=True)
class VehicleClass:
    name: str
    routine_ice_cost_per_km: float
    distance_rate_per_km: float


DEFAULT_CLASSES = {
    "bike": VehicleClass("bike", 10.00, 22.00),
    "tuk": VehicleClass("tuk", 22.10, 37.00),
    "mini": VehicleClass("mini", 32.80, 52.00),
    "compact": VehicleClass("compact", 34.00, 57.00),
    "sedan": VehicleClass("sedan", 36.10, 65.00),
}


def chargeable_distances(trip_km: float, pickup_km: float) -> tuple[float, float]:
    if trip_km < 0 or pickup_km < 0:
        raise ValueError("distances cannot be negative")
    return max(trip_km, MINIMUM_TRIP_KM), max(pickup_km, MINIMUM_PICKUP_KM)


def billable_passenger_minutes(total_trip_minutes: float, personal_stop_minutes: float = 0.0) -> float:
    if total_trip_minutes < 0 or personal_stop_minutes < 0:
        raise ValueError("minutes cannot be negative")
    if personal_stop_minutes > total_trip_minutes:
        raise ValueError("personal stop minutes cannot exceed total trip minutes")
    return round(total_trip_minutes - personal_stop_minutes, 6)


def ordinary_fare(
    vehicle_class: str,
    trip_km: float,
    trip_minutes: float,
    pickup_km: float = 0.0,
    personal_stop_minutes: float = 0.0,
    time_rate_per_min: float = DEFAULT_TIME_RATE_PER_MIN,
) -> float:
    if vehicle_class not in DEFAULT_CLASSES:
        raise ValueError(f"unknown vehicle class: {vehicle_class}")
    if time_rate_per_min < 0:
        raise ValueError("time rate cannot be negative")

    trip_charge_km, pickup_charge_km = chargeable_distances(trip_km, pickup_km)
    billable_minutes = billable_passenger_minutes(trip_minutes, personal_stop_minutes)
    rate = DEFAULT_CLASSES[vehicle_class].distance_rate_per_km
    fare = (trip_charge_km + pickup_charge_km) * rate
    fare += billable_minutes * time_rate_per_min
    return round(fare, 2)


def reference_trip_minutes(trip_km: float, reference_speed_kmph: float = REFERENCE_SPEED_KMPH) -> float:
    if trip_km < 0:
        raise ValueError("trip_km cannot be negative")
    if reference_speed_kmph <= 0:
        raise ValueError("reference_speed_kmph must be positive")
    return trip_km / reference_speed_kmph * 60


def estimated_fare_at_speed(
    vehicle_class: str,
    trip_km: float,
    speed_kmph: float,
    pickup_km: float = MINIMUM_PICKUP_KM,
) -> float:
    return ordinary_fare(
        vehicle_class,
        trip_km,
        reference_trip_minutes(trip_km, speed_kmph),
        pickup_km,
    )


def net_vehicle_headroom_per_km(
    vehicle_class: str,
    commission_rate: float = DEFAULT_COMMISSION_RATE,
) -> float:
    if vehicle_class not in DEFAULT_CLASSES:
        raise ValueError(f"unknown vehicle class: {vehicle_class}")
    vc = DEFAULT_CLASSES[vehicle_class]
    return round(vc.distance_rate_per_km * (1 - commission_rate) - vc.routine_ice_cost_per_km, 2)


def commission_amount(gross_passenger_fare: float, commission_rate: float = DEFAULT_COMMISSION_RATE) -> float:
    if gross_passenger_fare < 0:
        raise ValueError("fare cannot be negative")
    if not 0 <= commission_rate < 1:
        raise ValueError("commission_rate must be in [0, 1)")
    return round(gross_passenger_fare * commission_rate, 2)


def driver_receipt(gross_passenger_fare: float, commission_rate: float = DEFAULT_COMMISSION_RATE) -> float:
    return round(gross_passenger_fare - commission_amount(gross_passenger_fare, commission_rate), 2)


def search_radius_for_stage(stage: int) -> float:
    if stage < 1:
        raise ValueError("stage must be >= 1")
    return stage * SEARCH_BAND_KM


def cancellation_pickup_fare(
    vehicle_class: str,
    validated_pickup_km: float,
    eligible_for_passenger_charge: bool,
) -> float:
    """Passenger-facing pickup settlement when passenger cancels.

    Eligibility incorporates the deployment's published grace/no-show rules.
    No passenger-trip distance or passenger-trip time is included.
    """
    if vehicle_class not in DEFAULT_CLASSES:
        raise ValueError(f"unknown vehicle class: {vehicle_class}")
    if validated_pickup_km < 0:
        raise ValueError("validated_pickup_km cannot be negative")
    if not eligible_for_passenger_charge:
        return 0.0
    pickup_charge_km = max(validated_pickup_km, MINIMUM_PICKUP_KM)
    return round(pickup_charge_km * DEFAULT_CLASSES[vehicle_class].distance_rate_per_km, 2)


@dataclass(frozen=True)
class LongDistanceBand:
    lower_km: float
    upper_km: Optional[float]
    marginal_amount_per_km: float


def progressive_long_distance_accrual(
    passenger_trip_km: float,
    bands: Iterable[LongDistanceBand],
) -> float:
    """Accrue only kilometres inside each published marginal band.

    Bands should begin at or above LONG_DISTANCE_THRESHOLD_KM. No default band
    amounts are provided because v1.4 still requires empirical calibration.
    """
    if passenger_trip_km < 0:
        raise ValueError("passenger_trip_km cannot be negative")

    total = 0.0
    for band in bands:
        if band.lower_km < LONG_DISTANCE_THRESHOLD_KM:
            raise ValueError("long-distance bands cannot start below 40 km")
        if band.marginal_amount_per_km < 0:
            raise ValueError("marginal amount cannot be negative")
        upper = passenger_trip_km if band.upper_km is None else min(passenger_trip_km, band.upper_km)
        eligible = max(0.0, upper - band.lower_km)
        total += eligible * band.marginal_amount_per_km
    return round(total, 2)


def reconcile_long_distance(provisional_amount: float, final_amount: float) -> float:
    """Return signed end-of-trip adjustment for long-distance only."""
    if provisional_amount < 0 or final_amount < 0:
        raise ValueError("long-distance amounts cannot be negative")
    return round(final_amount - provisional_amount, 2)


def cash_commission_debt(fare: float, commission_rate: float = DEFAULT_COMMISSION_RATE) -> float:
    return commission_amount(fare, commission_rate)


def cash_trip_allowed(outstanding_debt: float, settlement_threshold: float) -> bool:
    if outstanding_debt < 0 or settlement_threshold <= 0:
        raise ValueError("debt must be non-negative and threshold positive")
    return outstanding_debt < settlement_threshold


if __name__ == "__main__":
    for speed in (25.0, 40.0):
        print(f"13 km + 2 km pickup @ {speed:g} km/h")
        for name in DEFAULT_CLASSES:
            fare = estimated_fare_at_speed(name, 13.0, speed, 2.0)
            print(f"  {name}: LKR {fare:.2f}")
