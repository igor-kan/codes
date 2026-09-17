"""Unit tests for Kretschmann Scalar."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kretschmann_scalar import KretschmannScalar


class TestKretschmannScalar(unittest.TestCase):
    def test_schwarzschild_horizon_finite(self):
        m = 1.0
        r_s = 2.0 * m
        k_horizon = KretschmannScalar.schwarzschild_exact(m, r_s)
        self.assertAlmostEqual(k_horizon, 0.75)


if __name__ == "__main__":
    unittest.main()
