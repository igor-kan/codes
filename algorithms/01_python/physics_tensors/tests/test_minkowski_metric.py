"""Unit tests for Minkowski Metric and Lorentz Boosts."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from minkowski_metric import MinkowskiSpacetime


class TestMinkowskiMetric(unittest.TestCase):
    def test_boost_invariance(self):
        mink = MinkowskiSpacetime(c=1.0)
        beta = [0.6, 0.0, 0.0]
        Lambda = mink.lorentz_boost(beta)
        eta = mink.eta.g
        transformed_eta = Lambda.T @ eta @ Lambda
        np.testing.assert_allclose(transformed_eta, eta, atol=1e-12)

    def test_four_velocity_norm(self):
        mink = MinkowskiSpacetime(c=1.0)
        u = mink.four_velocity([0.3, 0.4, 0.0])
        norm_sq = mink.invariant_norm_sq(u)
        self.assertAlmostEqual(norm_sq, -1.0, places=7)


if __name__ == "__main__":
    unittest.main()
