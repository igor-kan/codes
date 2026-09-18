import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from boltzmann_distribution import calculate_boltzmann_distribution, BoltzmannDistribution

class TestBoltzmannDistribution(unittest.TestCase):
    def test_calculate_boltzmann_distribution(self):
        self.assertAlmostEqual(calculate_boltzmann_distribution(10.0), 10.0)

    def test_boltzmann_distribution_class(self):
        obj = BoltzmannDistribution(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
