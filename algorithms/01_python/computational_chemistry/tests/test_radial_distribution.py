import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from radial_distribution import calculate_radial_distribution, RadialDistribution

class TestRadialDistribution(unittest.TestCase):
    def test_calculate_radial_distribution(self):
        self.assertAlmostEqual(calculate_radial_distribution(10.0), 10.0)

    def test_radial_distribution_class(self):
        obj = RadialDistribution(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
