import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from laser_rate_equations import calculate_laser_rate_equations, LaserRateEquations

class TestLaserRateEquations(unittest.TestCase):
    def test_calculate_laser_rate_equations(self):
        self.assertAlmostEqual(calculate_laser_rate_equations(10.0), 10.0)

    def test_laser_rate_equations_class(self):
        obj = LaserRateEquations(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
