"""Unit tests for Elasticity Stiffness Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from elasticity_stiffness_tensor import ElasticityStiffnessTensor


class TestElasticityStiffnessTensor(unittest.TestCase):
    def test_uniaxial_stress(self):
        e = 200e9  # 200 GPa
        nu = 0.3
        stiff = ElasticityStiffnessTensor.isotropic(youngs_modulus=e, poissons_ratio=nu)
        # Uniaxial strain: eps_xx = 0.001
        strain = np.diag([0.001, -nu * 0.001, -nu * 0.001])
        stress = stiff.stress_from_strain(strain)
        # Uniaxial stress: sigma_xx = E * eps_xx, sigma_yy = sigma_zz = 0
        self.assertAlmostEqual(stress[0, 0], e * 0.001, delta=1e2)
        self.assertAlmostEqual(stress[1, 1], 0.0, delta=1e2)
        self.assertAlmostEqual(stress[2, 2], 0.0, delta=1e2)


if __name__ == "__main__":
    unittest.main()
