import unittest

from simulator.cgmp import (
    DEFAULT_CLASSES,
    DEFAULT_TIME_RATE_PER_MIN,
    LongDistanceBand,
    TARGET_NET_LABOUR_PER_MIN,
    billable_passenger_minutes,
    cancellation_pickup_fare,
    cash_commission_debt,
    cash_trip_allowed,
    commission_amount,
    driver_receipt,
    estimated_fare_at_speed,
    net_vehicle_headroom_per_km,
    ordinary_fare,
    progressive_long_distance_accrual,
    reconcile_long_distance,
    reference_trip_minutes,
    search_radius_for_stage,
)


class TestCGMPv14(unittest.TestCase):
    def test_published_distance_rates(self):
        expected = {
            "bike": 22.0,
            "tuk": 37.0,
            "mini": 52.0,
            "compact": 57.0,
            "sedan": 65.0,
        }
        self.assertEqual({k: v.distance_rate_per_km for k, v in DEFAULT_CLASSES.items()}, expected)

    def test_implied_headrooms(self):
        expected = {
            "bike": 10.46,
            "tuk": 12.31,
            "mini": 15.56,
            "compact": 19.01,
            "sedan": 24.35,
        }
        self.assertEqual({k: net_vehicle_headroom_per_km(k) for k in DEFAULT_CLASSES}, expected)

    def test_time_rate_nets_approximately_12_per_min(self):
        self.assertAlmostEqual(DEFAULT_TIME_RATE_PER_MIN * 0.93, TARGET_NET_LABOUR_PER_MIN, places=2)

    def test_minimum_fare_2km_trip_plus_2km_pickup_at_25(self):
        minutes = reference_trip_minutes(2, 25)
        expected = {
            "bike": 149.92,
            "tuk": 209.92,
            "mini": 269.92,
            "compact": 289.92,
            "sedan": 321.92,
        }
        for name, fare in expected.items():
            self.assertEqual(ordinary_fare(name, 2, minutes, pickup_km=2), fare)

    def test_13km_reference_fares_at_25(self):
        expected = {
            "bike": 732.48,
            "tuk": 957.48,
            "mini": 1182.48,
            "compact": 1257.48,
            "sedan": 1377.48,
        }
        for name, fare in expected.items():
            self.assertEqual(estimated_fare_at_speed(name, 13, 25, 2), fare)

    def test_13km_reference_fares_at_40(self):
        expected = {
            "bike": 581.55,
            "tuk": 806.55,
            "mini": 1031.55,
            "compact": 1106.55,
            "sedan": 1226.55,
        }
        for name, fare in expected.items():
            self.assertEqual(estimated_fare_at_speed(name, 13, 40, 2), fare)

    def test_personal_stop_pauses_time_billing(self):
        self.assertEqual(billable_passenger_minutes(30, 5), 25)
        self.assertEqual(
            ordinary_fare("tuk", 10, 30, pickup_km=2, personal_stop_minutes=5),
            ordinary_fare("tuk", 10, 25, pickup_km=2),
        )

    def test_search_expands_in_2km_steps(self):
        self.assertEqual(search_radius_for_stage(1), 2.0)
        self.assertEqual(search_radius_for_stage(2), 4.0)
        self.assertEqual(search_radius_for_stage(3), 6.0)

    def test_cancellation_pickup_settlement_uses_pickup_rule(self):
        self.assertEqual(cancellation_pickup_fare("bike", 0.5, True), 44.0)
        self.assertEqual(cancellation_pickup_fare("tuk", 3.2, True), 118.4)
        self.assertEqual(cancellation_pickup_fare("tuk", 3.2, False), 0.0)

    def test_long_distance_does_not_reprice_first_40km(self):
        bands = [LongDistanceBand(40, 100, 10.0)]
        self.assertEqual(progressive_long_distance_accrual(39.9, bands), 0.0)
        self.assertEqual(progressive_long_distance_accrual(40.0, bands), 0.0)
        self.assertEqual(progressive_long_distance_accrual(40.1, bands), 1.0)
        self.assertEqual(progressive_long_distance_accrual(41.0, bands), 10.0)

    def test_long_distance_marginal_bands_are_continuous(self):
        bands = [
            LongDistanceBand(40, 100, 10.0),
            LongDistanceBand(100, 150, 15.0),
            LongDistanceBand(150, None, 20.0),
        ]
        self.assertEqual(progressive_long_distance_accrual(100, bands), 600.0)
        self.assertEqual(progressive_long_distance_accrual(101, bands), 615.0)
        self.assertEqual(progressive_long_distance_accrual(151, bands), 1370.0)

    def test_end_of_trip_reconciliation_can_add_or_deduct_only_long_distance(self):
        self.assertEqual(reconcile_long_distance(1000, 925), -75.0)
        self.assertEqual(reconcile_long_distance(1000, 1080), 80.0)

    def test_commission_and_cash_threshold(self):
        self.assertEqual(commission_amount(1000), 70.0)
        self.assertEqual(driver_receipt(1000), 930.0)
        self.assertEqual(cash_commission_debt(1000), 70.0)
        self.assertTrue(cash_trip_allowed(2499, 2500))
        self.assertFalse(cash_trip_allowed(2500, 2500))


if __name__ == "__main__":
    unittest.main()
