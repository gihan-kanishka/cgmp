"""Reference calculator for CGMP v1.2-preprint.

The reference implementation intentionally keeps the core mechanism small.
Behavioral concerns are measured before adding corrective pricing rules.
"""

from dataclasses import dataclass
from math import ceil
from typing import Iterable, Optional


DEFAULT_COMMISSION_RATE = 0.07
DEFAULT_TIME_RATE_PER_MIN = 12.90
TARGET_NET_LABOUR_PER_MIN = 12.0
MINIMUM_TRIP_KM = 2.0
INCLUDED_PICKUP_KM = 2.0
SEARCH_BAND_KM = 2.0
REFERENCE_SPEED_KMPH = 25.0
RATE_ROUNDING_INCREMENT = 0.5


@dataclass(frozen=True)
class VehicleClass:
    name: str
    routine_ice_cost_per_km: float
    target_net_vehicle_headroom_per_km: float
    distance_rate_per_km: float


def round_up(value: float, increment: float = RATE_ROUNDING_INCREMENT) -> float:
    if increment <= 0:
        raise ValueError("increment must be positive")
    return round(ceil(value / increment) * increment, 2)


def calibrated_distance_rate(
    routine_ice_cost_per_km: float,
    target_net_vehicle_headroom_per_km: float,
    commission_rate: float = DEFAULT_COMMISSION_RATE,
    rounding_increment: float = RATE_ROUNDING_INCREMENT,
) -> float:
    if routine_ice_cost_per_km < 0 or target_net_vehicle_headroom_per_km < 0:
        raise ValueError("cost and headroom cannot be negative")
    if not 0 <= commission_rate < 1:
        raise ValueError("commission_rate must be in [0, 1)")
    raw = (
        routine_ice_cost_per_km + target_net_vehicle_headroom_per_km
    ) / (1 - commission_rate)
    return round_up(raw, rounding_increment)


def _vehicle(name: str, cost: float, headroom: float) -> VehicleClass:
    return VehicleClass(
        name=name,
        routine_ice_cost_per_km=cost,
        target_net_vehicle_headroom_per_km=headroom,
        distance_rate_per_km=calibrated_distance_rate(cost, headroom),
    )


DEFAULT_CLASSES = {
    "bike": _vehicle("bike", 10.50, 3.0),
    "tuk": _vehicle("tuk", 22.10, 12.0),
    "mini": _vehicle("mini", 32.80, 15.0),
    "compact": _vehicle("compact", 34.00, 15.0),
    "sedan": _vehicle("sedan", 36.10, 21.0),
}


def chargeable_distances(trip_km: float, pickup_km: float) -> tuple[float, float]:
    if trip_km < 0 or pickup_km < 0:
        raise ValueError("distances cannot be negative")
    return max(trip_km, MINIMUM_TRIP_KM), max(pickup_km, INCLUDED_PICKUP_KM)


def ordinary_fare(
    vehicle_class: str,
    trip_km: float,
    trip_minutes: float,
    pickup_km: float = 0.0,
    long_distance_provision: float = 0.0,
    time_rate_per_min: float = DEFAULT_TIME_RATE_PER_MIN,
) -> float:
    """Return the gross passenger-facing deterministic fare.

    trip_minutes is passenger-trip time only. Pickup time is intentionally
    excluded from the v1.2 reference tariff.
    """
    if vehicle_class not in DEFAULT_CLASSES:
        raise ValueError(f"unknown vehicle class: {vehicle_class}")
    if trip_minutes < 0 or long_distance_provision < 0 or time_rate_per_min < 0:
        raise ValueError("time and provisions cannot be negative")

    trip_charge_km, pickup_charge_km = chargeable_distances(trip_km, pickup_km)
    rate = DEFAULT_CLASSES[vehicle_class].distance_rate_per_km
    fare = (trip_charge_km + pickup_charge_km) * rate
    fare += trip_minutes * time_rate_per_min
    fare += long_distance_provision
    return round(fare, 2)


def reference_trip_minutes(
    trip_km: float,
    reference_speed_kmph: float = REFERENCE_SPEED_KMPH,
) -> float:
    if trip_km < 0:
        raise ValueError("trip_km cannot be negative")
    if reference_speed_kmph <= 0:
        raise ValueError("reference_speed_kmph must be positive")
    return trip_km / reference_speed_kmph * 60


def estimated_fare_at_reference_speed(
    vehicle_class: str,
    trip_km: float,
    pickup_km: float = INCLUDED_PICKUP_KM,
) -> float:
    return ordinary_fare(
        vehicle_class=vehicle_class,
        trip_km=trip_km,
        trip_minutes=reference_trip_minutes(trip_km),
        pickup_km=pickup_km,
    )


def effective_passenger_rate_per_trip_km(
    vehicle_class: str,
    reference_speed_kmph: float = REFERENCE_SPEED_KMPH,
) -> float:
    if vehicle_class not in DEFAULT_CLASSES:
        raise ValueError(f"unknown vehicle class: {vehicle_class}")
    if reference_speed_kmph <= 0:
        raise ValueError("reference_speed_kmph must be positive")
    time_equivalent = (60 / reference_speed_kmph) * DEFAULT_TIME_RATE_PER_MIN
    return round(DEFAULT_CLASSES[vehicle_class].distance_rate_per_km + time_equivalent, 2)


def commission_amount(
    gross_passenger_fare: float,
    commission_exempt_amount: float = 0.0,
    commission_rate: float = DEFAULT_COMMISSION_RATE,
) -> float:
    """Commission applies only to commissionable fare.

    Direct pass-through amounts may be excluded if the implementation marks
    them as commission-exempt before the ride is accepted.
    """
    if gross_passenger_fare < 0 or commission_exempt_amount < 0:
        raise ValueError("fare amounts cannot be negative")
    if commission_exempt_amount > gross_passenger_fare:
        raise ValueError("commission_exempt_amount cannot exceed fare")
    if not 0 <= commission_rate < 1:
        raise ValueError("commission_rate must be in [0, 1)")
    commissionable = gross_passenger_fare - commission_exempt_amount
    return round(commissionable * commission_rate, 2)


def driver_receipt(
    gross_passenger_fare: float,
    commission_exempt_amount: float = 0.0,
    commission_rate: float = DEFAULT_COMMISSION_RATE,
) -> float:
    return round(
        gross_passenger_fare
        - commission_amount(
            gross_passenger_fare,
            commission_exempt_amount=commission_exempt_amount,
            commission_rate=commission_rate,
        ),
        2,
    )


def net_vehicle_headroom_per_km(
    vehicle_class: str,
    commission_rate: float = DEFAULT_COMMISSION_RATE,
) -> float:
    vc = DEFAULT_CLASSES[vehicle_class]
    net_distance_receipt = vc.distance_rate_per_km * (1 - commission_rate)
    return round(net_distance_receipt - vc.routine_ice_cost_per_km, 2)


def search_radius_for_stage(stage: int) -> float:
    """Stage 1 is 0-2 km, stage 2 reaches 0-4 km, and so on."""
    if stage < 1:
        raise ValueError("stage must be >= 1")
    return stage * SEARCH_BAND_KM


def passenger_ceiling(
    driver_specific_baseline_fare: float,
    trip_km: float,
    mode: str,
    value: float,
) -> float:
    """Apply the passenger's private rule to driver-specific F0_i."""
    if driver_specific_baseline_fare < 0 or trip_km < 0 or value < 0:
        raise ValueError("inputs cannot be negative")
    if mode == "percentage_above_base":
        return round(driver_specific_baseline_fare * (1 + value), 2)
    if mode == "fixed_amount_per_trip_km_above_base":
        return round(driver_specific_baseline_fare + trip_km * value, 2)
    if mode == "fixed_fee_by_trip_distance_band":
        return round(driver_specific_baseline_fare + value, 2)
    raise ValueError(f"unknown passenger ceiling mode: {mode}")


def first_qualifying_bid(
    driver_specific_baseline_fare: float,
    passenger_max_for_driver: float,
    gross_bids_in_authoritative_order: Iterable[float],
    deterministic_expanded_search_failed: bool,
) -> Optional[float]:
    """Return first qualifying gross passenger-facing fallback offer.

    Fallback is locked until the authorized deterministic expanded-search
    process has failed.
    """
    if not deterministic_expanded_search_failed:
        return None
    if driver_specific_baseline_fare < 0 or passenger_max_for_driver < 0:
        raise ValueError("fares cannot be negative")
    if passenger_max_for_driver < driver_specific_baseline_fare:
        return None

    for bid in gross_bids_in_authoritative_order:
        bid = float(bid)
        if driver_specific_baseline_fare <= bid <= passenger_max_for_driver:
            return round(bid, 2)
    return None


if __name__ == "__main__":
    for name in DEFAULT_CLASSES:
        fare = estimated_fare_at_reference_speed(name, 13.0, 2.0)
        print(f"{name}: 13 km + 2 km pickup @ 25 km/h = LKR {fare:.2f}")
