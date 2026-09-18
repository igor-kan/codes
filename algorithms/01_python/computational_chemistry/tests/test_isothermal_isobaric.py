import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from isothermal_isobaric import calculate_isothermal_isobaric, IsothermalIsobaric

class TestIsothermalIsobaric(unittest.TestCase):
    def test_calculate_isothermal_isobaric(self):
        self.assertAlmostEqual(calculate_isothermal_isobaric(10.0), 10.0)

    def test_isothermal_isobaric_class(self):
        obj = IsothermalIsobaric(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
