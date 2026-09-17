"""Unit tests for mantle convection."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mantle_convection_rayleigh_benard import MantleConvection


class TestMantleConvection(unittest.TestCase):
    def test_earth_mantle_convecting(self):
        # Earth's mantle has Ra ~ 1e6 to 1e7 >> 1707
        ra = MantleConvection.rayleigh_number(
            density_rho=3300.0,
            gravity_g=9.8,
            thermal_expansion_alpha=3e-5,
            delta_temp_k=2000.0,
            layer_thickness_d=2.9e6,
            thermal_diffusivity_kappa=1e-6,
            dynamic_viscosity_eta=1e21,
        )
        self.assertTrue(ra > 1e6)
        self.assertTrue(MantleConvection.is_convecting(ra, "rigid"))


if __name__ == "__main__":
    unittest.main()
