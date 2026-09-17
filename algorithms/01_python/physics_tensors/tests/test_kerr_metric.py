"""Unit tests for Kerr Metric."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kerr_metric import KerrMetric


class TestKerrMetric(unittest.TestCase):
    def test_horizons_schwarzschild_limit(self):
        kerr = KerrMetric(m=2.0, a=0.0)
        r_plus, r_minus = kerr.horizons
        self.assertAlmostEqual(r_plus, 4.0)
        self.assertAlmostEqual(r_minus, 0.0)

    def test_ergosphere(self):
        kerr = KerrMetric(m=2.0, a=1.0)
        r_e_equator = kerr.ergosphere_outer_radius(theta=np.pi / 2.0)
        self.assertAlmostEqual(r_e_equator, 4.0)


if __name__ == "__main__":
    unittest.main()
