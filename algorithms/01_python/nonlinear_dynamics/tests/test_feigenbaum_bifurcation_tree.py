"""Unit tests for Feigenbaum cascade."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from feigenbaum_bifurcation_tree import FeigenbaumCascade


class TestFeigenbaum(unittest.TestCase):
    def test_stable_fixed_point(self):
        # For r=2.5, fixed point is x* = 1 - 1/r = 0.6
        samples = FeigenbaumCascade.iterate(2.5, n_transient=200, n_samples=20)
        self.assertTrue(np.allclose(samples, 0.6, atol=1e-3))

    def test_chaotic_regime_lyapunov(self):
        # For r=4.0, logistic map is fully chaotic, lambda = ln(2) ~ 0.69315
        lam = FeigenbaumCascade.lyapunov_exponent(4.0, n_iterations=5000)
        self.assertAlmostEqual(lam, np.log(2.0), places=2)


if __name__ == "__main__":
    unittest.main()
