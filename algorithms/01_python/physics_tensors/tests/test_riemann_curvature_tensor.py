"""Unit tests for Riemann Curvature Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from christoffel_symbols import ChristoffelSymbols
from riemann_curvature_tensor import RiemannCurvatureTensor


class TestRiemannCurvatureTensor(unittest.TestCase):
    def test_2d_sphere_curvature(self):
        def sphere_metric(x):
            th, _ = x
            return np.diag([1.0, np.sin(th)**2])

        def cs_field(x):
            return ChristoffelSymbols.from_metric_field(sphere_metric, x)

        theta = np.pi / 3.0
        r_tensor = RiemannCurvatureTensor.from_christoffel_field(cs_field, [theta, 0.0])
        g = sphere_metric([theta, 0.0])

        self.assertTrue(r_tensor.check_algebraic_symmetries(g))
        r_cov = r_tensor.lower_first_index(g)
        self.assertAlmostEqual(r_cov[0, 1, 0, 1], np.sin(theta)**2, places=3)


if __name__ == "__main__":
    unittest.main()
