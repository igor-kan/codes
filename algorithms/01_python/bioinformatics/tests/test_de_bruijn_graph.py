import unittest
import sys
import os

# Insert the parent directory into sys.path to import adjacent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from de_bruijn_graph import calculate_de_bruijn_graph, DeBruijnGraph

class TestDeBruijnGraph(unittest.TestCase):
    def test_calculate_de_bruijn_graph(self):
        self.assertAlmostEqual(calculate_de_bruijn_graph(10.0), 10.0)

    def test_de_bruijn_graph_class(self):
        obj = DeBruijnGraph(5.0)
        self.assertAlmostEqual(obj.compute(), 5.0)

if __name__ == "__main__":
    unittest.main()
