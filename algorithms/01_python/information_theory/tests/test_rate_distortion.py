import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rate_distortion import calculate_rate_distortion, RateDistortion

class TestRateDistortion(unittest.TestCase):
    def test_calculate_rate_distortion(self):
        self.assertAlmostEqual(calculate_rate_distortion(10.0), 10.0)

    def test_rate_distortion_class(self):
        obj = RateDistortion(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
