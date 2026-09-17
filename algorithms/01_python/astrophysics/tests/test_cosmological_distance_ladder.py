"""Unit tests for cosmological distances."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cosmological_distance_ladder import CosmologicalDistances


class TestCosmology(unittest.TestCase):
    def test_low_redshift_hubble_law(self):
        cosmo = CosmologicalDistances(h0_kms_mpc=70.0, omega_m=0.3, omega_lambda=0.7)
        z = 0.001
        dl = cosmo.luminosity_distance(z)
        # At low z << 1, d_L ~ c * z / H_0
        dl_linear = (cosmo.C * z) / cosmo.h0
        self.assertAlmostEqual(dl / dl_linear, 1.0, places=2)


if __name__ == "__main__":
    unittest.main()
