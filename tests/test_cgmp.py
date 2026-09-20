import unittest

from simulator.cgmp import (
    DEFAULT_CLASSES,
    DEFAULT_TIME_RATE_PER_MIN,
    TARGET_NET_LABOUR_PER_MIN,
    commission_amount,
    driver_receipt,
    effective_passenger_rate_per_trip_km,
    estimated_fare_at_reference_speed,
    first_qualifying_bid,
    net_vehicle_headroom_per_km,
    ordinary_fare,
    passenger_ceiling,
    reference_trip_minutes,
    search_radius_for_stage,
)


class TestCGMPv12(unittest.TestCase):
    def test_published_distance_rates(self):
        expected = {
            "bike": 19.0,
            "tuk": 37.0,
            "mini": 51.5,
            "compact": 53.0,
            "sedan": 61.5,
        }
        self.assertEqual(
            {k: v.distance_rate_per_km for k, v in DEFAULT_CLASSES.items()},
            expected,
        )

    def test_net_vehicle_headrooms_meet_targets(self):
        for name, vc in DEFAULT_CLASSES.items():
            self.assertGreaterEqual(
                net_vehicle_headroom_per_km(name),
                vc.target_net_vehicle_headroom_per_km,
            )

    def test_time_rate_nets_approximately_12_per_min(self):
        self.assertAlmostEqual(
            DEFAULT_TIME_RATE_PER_MIN * 0.93,
            TARGET_NET_LABOUR_PER_MIN,
            places=2,
        )

    def test_minimum_fare_2km_trip_plus_2km_pickup(self):
        minutes = reference_trip_minutes(2)
        expected = {
            "bike": 137.92,
            "tuk": 209.92,
            "mini": 267.92,
            "compact": 273.92,
            "sedan": 307.92,
        }
        for name, fare in expected.items():
            self.assertEqual(ordinary_fare(name, 2, minutes, pickup_km=2), fare)

    def test_pickup_time_is_not_charged(self):
        self.assertEqual(
            ordinary_fare("tuk", 5, 12, pickup_km=2),
            ordinary_fare("tuk", 5, 12, pickup_km=2),
        )

    def test_13km_reference_fares(self):
        expected = {
            "bike": 687.48,
            "tuk": 957.48,
            "mini": 1174.98,
            "compact": 1197.48,
            "sedan": 1324.98,
        }
        for name, fare in expected.items():
            self.assertEqual(estimated_fare_at_reference_speed(name, 13, 2), fare)

    def test_effective_rates_at_25kmh(self):
        expected = {
            "bike": 49.96,
            "tuk": 67.96,
            "mini": 82.46,
            "compact": 83.96,
            "sedan": 92.46,
        }
        for name, rate in expected.items():
            self.assertEqual(effective_passenger_rate_per_trip_km(name), rate)

    def test_search_expands_in_2km_steps(self):
        self.assertEqual(search_radius_for_stage(1), 2.0)
        self.assertEqual(search_radius_for_stage(2), 4.0)
        self.assertEqual(search_radius_for_stage(3), 6.0)

    def test_fallback_locked_before_expanded_search_failure(self):
        self.assertIsNone(
            first_qualifying_bid(
                1000, 1300, [1100, 1050], deterministic_expanded_search_failed=False
            )
        )

    def test_first_qualifying_gross_bid_after_expansion_failure(self):
        self.assertEqual(
            first_qualifying_bid(
                1000,
                1300,
                [1320, 1250, 1175, 1200],
                deterministic_expanded_search_failed=True,
            ),
            1250.0,
        )

    def test_driver_specific_passenger_ceiling_modes(self):
        self.assertEqual(passenger_ceiling(1000, 10, "percentage_above_base", 0.2), 1200)
        self.assertEqual(
            passenger_ceiling(1000, 10, "fixed_amount_per_trip_km_above_base", 10),
            1100,
        )
        self.assertEqual(
            passenger_ceiling(1000, 10, "fixed_fee_by_trip_distance_band", 250),
            1250,
        )

    def test_commission_on_commissionable_amount(self):
        self.assertEqual(commission_amount(1000), 70.0)
        self.assertEqual(driver_receipt(1000), 930.0)

    def test_pass_through_can_be_commission_exempt(self):
        self.assertEqual(commission_amount(1100, commission_exempt_amount=100), 70.0)
        self.assertEqual(driver_receipt(1100, commission_exempt_amount=100), 1030.0)


if __name__ == "__main__":
    unittest.main()
