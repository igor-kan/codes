"""Unit tests for Hopf bifurcation."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hopf_bifurcation import HopfBifurcation


class TestHopf(unittest.TestCase):
    def test_supercritical_limit_cycle(self):
        hopf = HopfBifurcation(mu=4.0, a=1.0)
        r_star = hopf.limit_cycle_radius()
        self.assertAlmostEqual(r_star, 2.0, places=3)
        dr, _ = hopf.polar_derivatives(r_star, 0.0)
        self.assertAlmostEqual(dr, 0.0, places=5)


if __name__ == "__main__":
    unittest.main()
