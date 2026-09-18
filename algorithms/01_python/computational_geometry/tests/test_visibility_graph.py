import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from visibility_graph import calculate_visibility_graph, VisibilityGraph

class TestVisibilityGraph(unittest.TestCase):
    def test_calculate_visibility_graph(self):
        self.assertAlmostEqual(calculate_visibility_graph(10.0), 10.0)

    def test_visibility_graph_class(self):
        obj = VisibilityGraph(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
