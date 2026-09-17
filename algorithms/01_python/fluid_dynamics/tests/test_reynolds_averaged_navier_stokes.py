"""Unit tests for RANS Boussinesq."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from reynolds_averaged_navier_stokes import RANSBoussinesq


class TestRANS(unittest.TestCase):
    def test_isotropic_normal_stresses(self):
        # For zero mean strain, tau_{ii}^R = -2/3 rho k
        rans = RANSBoussinesq(eddy_viscosity_mut=0.01, turbulent_ke_k=3.0, fluid_density=1.0)
        stress = rans.reynolds_stress_tensor(np.zeros((3, 3)))
        np.testing.assert_allclose(stress, -2.0 * np.eye(3))


if __name__ == "__main__":
    unittest.main()
