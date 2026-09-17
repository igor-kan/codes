"""Unit tests for Discrete Quantum Walk."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_walk_discrete import DiscreteQuantumWalk1D


class TestQuantumWalk(unittest.TestCase):
    def test_walk_probability_conservation(self):
        qw = DiscreteQuantumWalk1D(steps=15)
        probs = qw.run()
        self.assertAlmostEqual(np.sum(probs), 1.0)


if __name__ == "__main__":
    unittest.main()
