import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from london_equations import calculate_london_equations, LondonEquations

class TestLondonEquations(unittest.TestCase):
    def test_calculate_london_equations(self):
        self.assertAlmostEqual(calculate_london_equations(10.0), 10.0)

    def test_london_equations_class(self):
        obj = LondonEquations(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
