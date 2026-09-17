"""Unit tests for Diffusion Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from diffusion_tensor import DiffusionTensor


class TestDiffusionTensor(unittest.TestCase):
    def test_isotropic_diffusion(self):
        # Isotropic diffusion has FA = 0
        iso = DiffusionTensor(np.eye(3) * 1e-9)
        self.assertAlmostEqual(iso.fractional_anisotropy, 0.0)

    def test_linear_anisotropy(self):
        # Highly anisotropic diffusion (fiber tract)
        fiber = DiffusionTensor(np.diag([10e-9, 0.0, 0.0]))
        self.assertAlmostEqual(fiber.fractional_anisotropy, 1.0)


if __name__ == "__main__":
    unittest.main()
