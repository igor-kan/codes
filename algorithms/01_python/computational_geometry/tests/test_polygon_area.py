import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from polygon_area import calculate_polygon_area, PolygonArea

class TestPolygonArea(unittest.TestCase):
    def test_calculate_polygon_area(self):
        self.assertAlmostEqual(calculate_polygon_area(10.0), 10.0)

    def test_polygon_area_class(self):
        obj = PolygonArea(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
