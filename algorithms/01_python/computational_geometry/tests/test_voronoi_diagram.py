import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from voronoi_diagram import calculate_voronoi_diagram, VoronoiDiagram

class TestVoronoiDiagram(unittest.TestCase):
    def test_calculate_voronoi_diagram(self):
        self.assertAlmostEqual(calculate_voronoi_diagram(10.0), 10.0)

    def test_voronoi_diagram_class(self):
        obj = VoronoiDiagram(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
