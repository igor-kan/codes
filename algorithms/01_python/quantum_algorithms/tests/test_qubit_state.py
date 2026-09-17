"""Unit tests for Qubit State."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from qubit_state import QubitState


class TestQubitState(unittest.TestCase):
    def test_hadamard_state_bloch(self):
        # |+> = 1/sqrt(2) (|0> + |1>) has Bloch vector (1, 0, 0)
        q = QubitState(1.0, 1.0)
        u, v, w = q.bloch_vector
        self.assertAlmostEqual(u, 1.0)
        self.assertAlmostEqual(v, 0.0)
        self.assertAlmostEqual(w, 0.0)
        p0, p1 = q.measurement_probabilities()
        self.assertAlmostEqual(p0, 0.5)
        self.assertAlmostEqual(p1, 0.5)


if __name__ == "__main__":
    unittest.main()
