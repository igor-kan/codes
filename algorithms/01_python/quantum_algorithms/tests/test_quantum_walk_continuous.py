"""Unit tests for Continuous Quantum Walk."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_walk_continuous import ContinuousQuantumWalk


class TestContinuousQuantumWalk(unittest.TestCase):
    def test_unitarity_and_conservation(self):
        # 3-node path graph: 0 - 1 - 2
        adj = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        cqw = ContinuousQuantumWalk(adj)
        probs = cqw.probability_distribution(initial_node=0, t=1.5)
        self.assertAlmostEqual(np.sum(probs), 1.0)


if __name__ == "__main__":
    unittest.main()
