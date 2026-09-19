"""Minimal reference calculator for CGMP v1.0-draft."""

from dataclasses import dataclass
from typing import Iterable, Optional


@dataclass(frozen=True)
class VehicleClass:
    name: str
    distance_rate_per_km: float


DEFAULT_CLASSES = {
    "bike": VehicleClass("bike", 30.0),
    "tuk": VehicleClass("tuk", 40.0),
    "mini": VehicleClass("mini", 50.0),
    "compact": VehicleClass("compact", 52.5),
    "sedan": VehicleClass("sedan", 55.0),
}

DEFAULT_TIME_RATE_PER_MIN = 12.0
DEFAULT_COMMISSION_RATE = 0.07


def ordinary_fare(
    vehicle_class: str,
    trip_km: float,
    trip_minutes: float,
    pickup_km: float = 0.0,
    long_distance_provision: float = 0.0,
    time_rate_per_min: float = DEFAULT_TIME_RATE_PER_MIN,
) -> float:
    if vehicle_class not in DEFAULT_CLASSES:
        raise ValueError(f"unknown vehicle class: {vehicle_class}")

    values = {
        "trip_km": trip_km,
        "trip_minutes": trip_minutes,
        "pickup_km": pickup_km,
        "long_distance_provision": long_distance_provision,
        "time_rate_per_min": time_rate_per_min,
    }
    for name, value in values.items():
        if value < 0:
            raise ValueError(f"{name} cannot be negative")

    rate = DEFAULT_CLASSES[vehicle_class].distance_rate_per_km
    fare = (trip_km + pickup_km) * rate
    fare += trip_minutes * time_rate_per_min
    fare += long_distance_provision
    return round(fare, 2)


def driver_receipt(
    passenger_fare: float,
    commission_rate: float = DEFAULT_COMMISSION_RATE,
) -> float:
    if passenger_fare < 0:
        raise ValueError("passenger_fare cannot be negative")
    if not 0 <= commission_rate < 1:
        raise ValueError("commission_rate must be in [0, 1)")
    return round(passenger_fare * (1 - commission_rate), 2)


def lowest_qualifying_bid(
    baseline_fare: float,
    passenger_max: float,
    bids: Iterable[float],
) -> Optional[float]:
    if baseline_fare < 0 or passenger_max < 0:
        raise ValueError("fares cannot be negative")
    if passenger_max < baseline_fare:
        return None

    eligible = [
        float(b) for b in bids
        if b >= baseline_fare and b <= passenger_max
    ]
    if not eligible:
        return None
    return round(min(eligible), 2)


if __name__ == "__main__":
    example = ordinary_fare(
        vehicle_class="tuk",
        trip_km=12.6,
        trip_minutes=35,
        pickup_km=1.5,
    )
    print(f"Example tuk fare: LKR {example:.2f}")
    print(f"Driver receipt at 7% commission: LKR {driver_receipt(example):.2f}")
