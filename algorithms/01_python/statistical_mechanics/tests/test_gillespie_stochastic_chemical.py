"""Unit tests for Gillespie Algorithm."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gillespie_stochastic_chemical import GillespieAlgorithm


class TestGillespie(unittest.TestCase):
    def test_birth_death_step(self):
        # A -> 2A (rate 1), A -> 0 (rate 0.5)
        state = np.array([10])
        props = [10.0 * 1.0, 10.0 * 0.5]
        s_mat = np.array([[1], [-1]])
        tau, next_state = GillespieAlgorithm.step(state, props, s_mat)
        self.assertGreater(tau, 0.0)
        self.assertIn(next_state[0], [9, 11])


if __name__ == "__main__":
    unittest.main()
