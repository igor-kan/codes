import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from black_hole_horizon import calculate_black_hole_horizon, BlackHoleHorizon

class TestBlackHoleHorizon(unittest.TestCase):
    def test_calculate_black_hole_horizon(self):
        self.assertAlmostEqual(calculate_black_hole_horizon(10.0), 10.0)

    def test_black_hole_horizon_class(self):
        obj = BlackHoleHorizon(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
