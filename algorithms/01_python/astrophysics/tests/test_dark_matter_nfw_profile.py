"""Unit tests for NFW profile."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dark_matter_nfw_profile import NFWProfile


class TestNFW(unittest.TestCase):
    def test_enclosed_mass_positive(self):
        halo = NFWProfile(rho_0=1e-21, r_s=20e3 * 3.085677581e16)  # 20 kpc in meters
        r = 10e3 * 3.085677581e16
        m = halo.enclosed_mass(r)
        vc = halo.circular_velocity(r)
        self.assertTrue(m > 0)
        self.assertTrue(vc > 0)


if __name__ == "__main__":
    unittest.main()
