"""Unit tests for Magnetic Susceptibility Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from magnetic_susceptibility_tensor import MagneticSusceptibilityTensor


class TestMagneticSusceptibilityTensor(unittest.TestCase):
    def test_magnetization(self):
        chi = MagneticSusceptibilityTensor(np.diag([1e-4, 2e-4, 1e-4]))
        m = chi.magnetization([100.0, 0.0, 0.0])
        self.assertAlmostEqual(m[0], 0.01)
        self.assertAlmostEqual(chi.magnetic_anisotropy, 1e-4)


if __name__ == "__main__":
    unittest.main()
