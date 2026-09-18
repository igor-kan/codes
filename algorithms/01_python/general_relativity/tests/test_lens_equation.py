import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lens_equation import calculate_lens_equation, LensEquation

class TestLensEquation(unittest.TestCase):
    def test_calculate_lens_equation(self):
        self.assertAlmostEqual(calculate_lens_equation(10.0), 10.0)

    def test_lens_equation_class(self):
        obj = LensEquation(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
