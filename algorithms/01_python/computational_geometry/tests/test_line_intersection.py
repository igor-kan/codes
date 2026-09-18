import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from line_intersection import calculate_line_intersection, LineIntersection

class TestLineIntersection(unittest.TestCase):
    def test_calculate_line_intersection(self):
        self.assertAlmostEqual(calculate_line_intersection(10.0), 10.0)

    def test_line_intersection_class(self):
        obj = LineIntersection(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
