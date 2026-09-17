"""Unit tests for Schwarzschild Metric."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schwarzschild_metric import SchwarzschildMetric


class TestSchwarzschildMetric(unittest.TestCase):
    def test_schwarzschild_components(self):
        sm = SchwarzschildMetric(m=1.0)
        g = sm.metric_at([0.0, 4.0, np.pi / 2.0, 0.0])
        self.assertAlmostEqual(g.g[0, 0], -0.5)
        self.assertAlmostEqual(g.g[1, 1], 2.0)
        self.assertAlmostEqual(g.g[2, 2], 16.0)

    def test_light_deflection(self):
        sm = SchwarzschildMetric(m=1.0)
        theta_def = sm.light_deflection(impact_parameter=100.0)
        self.assertAlmostEqual(theta_def, 4.0 / 100.0)


if __name__ == "__main__":
    unittest.main()
