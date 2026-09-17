"""Unit tests for Viscous Stress Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from viscous_stress_tensor import ViscousStressTensor


class TestViscousStressTensor(unittest.TestCase):
    def test_shear_dissipation_positive(self):
        vst = ViscousStressTensor(shear_viscosity=1.0)
        # Simple Couette shear flow: v_x = gamma * y
        grad_v = [[0.0, 5.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        phi = vst.dissipation_function(grad_v)
        # Phi = mu * gamma^2 = 1.0 * 25.0 = 25.0
        self.assertAlmostEqual(phi, 25.0)


if __name__ == "__main__":
    unittest.main()
