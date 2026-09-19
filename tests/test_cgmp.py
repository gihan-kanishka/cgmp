import unittest

from simulator.cgmp import driver_receipt, first_qualifying_bid, ordinary_fare


class TestCGMP(unittest.TestCase):
    def test_tuk_example(self):
        self.assertEqual(ordinary_fare("tuk", 12.6, 35, pickup_km=1.5), 984.0)

    def test_13km_45min(self):
        self.assertEqual(ordinary_fare("bike", 13, 45), 930.0)
        self.assertEqual(ordinary_fare("tuk", 13, 45), 1060.0)
        self.assertEqual(ordinary_fare("mini", 13, 45), 1190.0)
        self.assertEqual(ordinary_fare("compact", 13, 45), 1222.5)
        self.assertEqual(ordinary_fare("sedan", 13, 45), 1255.0)

    def test_commission(self):
        self.assertEqual(driver_receipt(1000), 930.0)

    def test_first_qualifying_bid_wins_even_if_later_bid_is_lower(self):
        self.assertEqual(
            first_qualifying_bid(1000, 1300, [1320, 1250, 1175, 1200]),
            1250.0,
        )

    def test_bid_below_baseline_does_not_clear(self):
        self.assertEqual(
            first_qualifying_bid(1000, 1300, [950, 1100]),
            1100.0,
        )

    def test_no_qualifying_bid(self):
        self.assertIsNone(first_qualifying_bid(1000, 1100, [1150, 1200]))

    def test_ceiling_below_baseline(self):
        self.assertIsNone(first_qualifying_bid(1000, 900, [900]))


if __name__ == "__main__":
    unittest.main()
