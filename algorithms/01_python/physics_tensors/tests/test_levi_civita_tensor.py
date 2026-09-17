"""Unit tests for Levi-Civita Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from levi_civita_tensor import LeviCivitaTensor


class TestLeviCivitaTensor(unittest.TestCase):
    def test_cross_product_identity(self):
        eps = LeviCivitaTensor.symbol_3d()
        u = np.array([1.0, 2.0, 3.0])
        v = np.array([4.0, 5.0, 6.0])
        cross_eps = np.einsum('ijk,j,k->i', eps, u, v)
        cross_np = np.cross(u, v)
        np.testing.assert_allclose(cross_eps, cross_np)

    def test_hodge_dual_invariance(self):
        # In Minkowski spacetime, *(*F) = -F for 2-forms
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        f = np.zeros((4, 4))
        f[0, 1] = 2.0
        f[1, 0] = -2.0
        star_f = LeviCivitaTensor.hodge_star_2form_4d(f, eta)
        star_star_f = LeviCivitaTensor.hodge_star_2form_4d(star_f, eta)
        np.testing.assert_allclose(star_star_f, -f, atol=1e-10)


if __name__ == "__main__":
    unittest.main()
