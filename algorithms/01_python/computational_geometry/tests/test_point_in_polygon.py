import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from point_in_polygon import calculate_point_in_polygon, PointInPolygon

class TestPointInPolygon(unittest.TestCase):
    def test_calculate_point_in_polygon(self):
        self.assertAlmostEqual(calculate_point_in_polygon(10.0), 10.0)

    def test_point_in_polygon_class(self):
        obj = PointInPolygon(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
