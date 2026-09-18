import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ewald_summation import calculate_ewald_summation, EwaldSummation

class TestEwaldSummation(unittest.TestCase):
    def test_calculate_ewald_summation(self):
        self.assertAlmostEqual(calculate_ewald_summation(10.0), 10.0)

    def test_ewald_summation_class(self):
        obj = EwaldSummation(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
