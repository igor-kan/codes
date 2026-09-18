import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fresnel_equations import calculate_fresnel_equations, FresnelEquations

class TestFresnelEquations(unittest.TestCase):
    def test_calculate_fresnel_equations(self):
        self.assertAlmostEqual(calculate_fresnel_equations(10.0), 10.0)

    def test_fresnel_equations_class(self):
        obj = FresnelEquations(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
