"""Unit tests for QAOA MaxCut."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from qaoa_maxcut import QAOAMaxCut


class TestQAOAMaxCut(unittest.TestCase):
    def test_triangle_graph_maxcut(self):
        edges = [(0, 1), (1, 2), (2, 0)]
        qaoa = QAOAMaxCut(edges, num_nodes=3)
        cut = qaoa.cut_value([0, 1, 0])
        self.assertEqual(cut, 2)


if __name__ == "__main__":
    unittest.main()
