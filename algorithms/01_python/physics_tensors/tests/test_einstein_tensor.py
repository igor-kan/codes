"""Unit tests for Einstein Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ricci_tensor_and_scalar import RicciCurvature
from einstein_tensor import EinsteinTensor


class TestEinsteinTensor(unittest.TestCase):
    def test_vacuum_solution(self):
        g = np.diag([-1.0, 1.0, 1.0, 1.0])
        inv_g = np.linalg.inv(g)
        ricci = RicciCurvature(np.zeros((4, 4)), inv_g)
        einstein = EinsteinTensor(ricci, g)
        np.testing.assert_allclose(einstein.g_tensor, np.zeros((4, 4)))
        self.assertAlmostEqual(einstein.trace, 0.0)


if __name__ == "__main__":
    unittest.main()
