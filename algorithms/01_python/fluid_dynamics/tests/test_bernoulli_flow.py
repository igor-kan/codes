"""Unit tests for Bernoulli Flow."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bernoulli_flow import BernoulliEquation


class TestBernoulli(unittest.TestCase):
    def test_torricelli_speed(self):
        v = BernoulliEquation.torricelli_efflux_speed(height=5.0)
        # Sqrt(2 * 9.80665 * 5) approx 9.9028
        self.assertAlmostEqual(v, np.sqrt(2.0 * 9.80665 * 5.0))


if __name__ == "__main__":
    unittest.main()
