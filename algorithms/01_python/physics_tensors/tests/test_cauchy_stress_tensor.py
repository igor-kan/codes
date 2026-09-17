"""Unit tests for Cauchy Stress Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cauchy_stress_tensor import CauchyStressTensor


class TestCauchyStressTensor(unittest.TestCase):
    def test_pure_shear_von_mises(self):
        # Pure shear stress tau
        tau = 50.0
        mat = [
            [0.0, tau, 0.0],
            [tau, 0.0, 0.0],
            [0.0, 0.0, 0.0]
        ]
        stress = CauchyStressTensor(mat)
        # For pure shear, sigma_vM = sqrt(3) * tau
        self.assertAlmostEqual(stress.von_mises_equivalent_stress(), np.sqrt(3.0) * tau)
        self.assertAlmostEqual(stress.hydrostatic_stress, 0.0)


if __name__ == "__main__":
    unittest.main()
