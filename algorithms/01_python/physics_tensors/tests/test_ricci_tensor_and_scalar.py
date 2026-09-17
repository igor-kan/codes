"""Unit tests for Ricci Tensor and Scalar."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ricci_tensor_and_scalar import RicciCurvature


class TestRicciCurvature(unittest.TestCase):
    def test_2d_sphere_ricci_scalar(self):
        a = 2.0
        g = np.diag([a**2, a**2])
        inv_g = np.linalg.inv(g)
        r_mu_nu = np.eye(2)
        ricci = RicciCurvature(r_mu_nu, inv_g)
        self.assertAlmostEqual(ricci.scalar, 2.0 / (a**2))


if __name__ == "__main__":
    unittest.main()
