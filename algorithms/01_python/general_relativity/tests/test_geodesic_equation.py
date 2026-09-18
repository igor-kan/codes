import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from geodesic_equation import calculate_geodesic_equation, GeodesicEquation

class TestGeodesicEquation(unittest.TestCase):
    def test_calculate_geodesic_equation(self):
        self.assertAlmostEqual(calculate_geodesic_equation(10.0), 10.0)

    def test_geodesic_equation_class(self):
        obj = GeodesicEquation(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
