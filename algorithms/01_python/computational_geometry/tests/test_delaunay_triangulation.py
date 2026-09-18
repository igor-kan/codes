import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from delaunay_triangulation import calculate_delaunay_triangulation, DelaunayTriangulation

class TestDelaunayTriangulation(unittest.TestCase):
    def test_calculate_delaunay_triangulation(self):
        self.assertAlmostEqual(calculate_delaunay_triangulation(10.0), 10.0)

    def test_delaunay_triangulation_class(self):
        obj = DelaunayTriangulation(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
