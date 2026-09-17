"""Unit tests for Lyapunov exponent estimation."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lyapunov_exponent_spectrum import LyapunovExponent


class TestLyapunov(unittest.TestCase):
    def test_linear_stable_system(self):
        # dx/dt = -2 * x -> lambda = -2.0
        deriv = lambda x: -2.0 * x
        lam = LyapunovExponent.estimate_max_exponent(deriv, np.array([1.0]), dt=0.01, steps=500)
        self.assertAlmostEqual(lam, -2.0, places=1)


if __name__ == "__main__":
    unittest.main()
