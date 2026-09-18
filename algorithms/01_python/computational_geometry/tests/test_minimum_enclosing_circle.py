import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from minimum_enclosing_circle import calculate_minimum_enclosing_circle, MinimumEnclosingCircle

class TestMinimumEnclosingCircle(unittest.TestCase):
    def test_calculate_minimum_enclosing_circle(self):
        self.assertAlmostEqual(calculate_minimum_enclosing_circle(10.0), 10.0)

    def test_minimum_enclosing_circle_class(self):
        obj = MinimumEnclosingCircle(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
