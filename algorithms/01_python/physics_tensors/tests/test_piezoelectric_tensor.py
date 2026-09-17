"""Unit tests for Piezoelectric Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from piezoelectric_tensor import PiezoelectricTensor


class TestPiezoelectricTensor(unittest.TestCase):
    def test_quartz_transverse_effect(self):
        # Simplified quartz d_11 piezoelectric coefficient
        d_mat = np.zeros((3, 6))
        d11 = 2.3e-12  # C/N
        d_mat[0, 0] = d11
        d_mat[0, 1] = -d11
        piezo = PiezoelectricTensor(d_mat)

        # Apply tensile stress sigma_xx = 1e6 Pa
        stress = np.diag([1e6, 0.0, 0.0])
        p = piezo.polarization(stress)
        self.assertAlmostEqual(p[0], d11 * 1e6)
        self.assertAlmostEqual(p[1], 0.0)


if __name__ == "__main__":
    unittest.main()
