import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from density_functional import calculate_density_functional, DensityFunctional

class TestDensityFunctional(unittest.TestCase):
    def test_calculate_density_functional(self):
        self.assertAlmostEqual(calculate_density_functional(10.0), 10.0)

    def test_density_functional_class(self):
        obj = DensityFunctional(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
