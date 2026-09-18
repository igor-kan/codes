import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from moving_average import calculate_moving_average, MovingAverage

class TestMovingAverage(unittest.TestCase):
    def test_calculate_moving_average(self):
        self.assertAlmostEqual(calculate_moving_average(10.0), 10.0)

    def test_moving_average_class(self):
        obj = MovingAverage(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
