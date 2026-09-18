import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from friedmann_equations import calculate_friedmann_equations, FriedmannEquations

class TestFriedmannEquations(unittest.TestCase):
    def test_calculate_friedmann_equations(self):
        self.assertAlmostEqual(calculate_friedmann_equations(10.0), 10.0)

    def test_friedmann_equations_class(self):
        obj = FriedmannEquations(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
