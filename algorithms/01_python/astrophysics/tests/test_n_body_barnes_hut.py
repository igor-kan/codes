"""Unit tests for Barnes-Hut QuadTree."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from n_body_barnes_hut import QuadTreeNode


class TestBarnesHut(unittest.TestCase):
    def test_two_body_force(self):
        tree = QuadTreeNode(0.0, 10.0, 0.0, 10.0)
        tree.insert(np.array([5.0, 5.0]), mass=100.0)
        f = tree.compute_force(np.array([5.0, 7.0]), theta=0.5, g_const=1.0, eps=0.0)
        # Expected: attractive toward [5.0, 5.0], distance = 2.0 -> force magnitude = 100 / 4 = 25
        self.assertAlmostEqual(f[0], 0.0, places=3)
        self.assertAlmostEqual(f[1], -25.0, places=3)


if __name__ == "__main__":
    unittest.main()
