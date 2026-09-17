"""Unit tests for Christoffel Symbols."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from christoffel_symbols import ChristoffelSymbols


class TestChristoffelSymbols(unittest.TestCase):
    def test_flat_euclidean_christoffel(self):
        def flat_metric(x):
            return np.eye(3)

        cs = ChristoffelSymbols.from_metric_field(flat_metric, [1.0, 2.0, 3.0])
        np.testing.assert_allclose(cs.gamma, np.zeros((3, 3, 3)), atol=1e-8)
        acc = cs.geodesic_acceleration([1.0, 0.0, 0.0])
        np.testing.assert_allclose(acc, np.zeros(3), atol=1e-8)

    def test_polar_coordinates_christoffel(self):
        def polar_metric(x):
            r, _ = x
            return np.diag([1.0, r**2])

        r_val = 2.5
        cs = ChristoffelSymbols.from_metric_field(polar_metric, [r_val, 0.5])
        self.assertAlmostEqual(cs.gamma[0, 1, 1], -r_val, places=4)
        self.assertAlmostEqual(cs.gamma[1, 0, 1], 1.0 / r_val, places=4)


if __name__ == "__main__":
    unittest.main()
