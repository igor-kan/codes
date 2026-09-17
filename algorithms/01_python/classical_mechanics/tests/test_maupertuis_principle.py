"""Unit tests for Maupertuis Principle."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from maupertuis_principle import MaupertuisJacobiMetric


class TestMaupertuisPrinciple(unittest.TestCase):
    def test_free_particle_jacobi_metric(self):
        # V(q) = 0, E = 8 => conformal factor 2E = 16
        mj = MaupertuisJacobiMetric(energy=8.0, potential_func=lambda q: 0.0)
        g_j = mj.metric_at([1.0, 2.0])
        np.testing.assert_allclose(g_j, 16.0 * np.eye(2))

        # Straight line from (0,0) to (3,4) length = 5
        # W = sqrt(16) * 5 = 20
        path = np.linspace([0.0, 0.0], [3.0, 4.0], 100)
        w = mj.jacobi_arc_length(path)
        self.assertAlmostEqual(w, 20.0, places=2)


if __name__ == "__main__":
    unittest.main()
