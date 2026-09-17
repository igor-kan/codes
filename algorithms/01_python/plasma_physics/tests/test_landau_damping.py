"""Unit tests for Landau Damping."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from landau_damping import LandauDamping


class TestLandauDamping(unittest.TestCase):
    def test_damping_is_negative(self):
        gamma = LandauDamping.damping_rate(k_wavenumber=0.3, debye_length=1.0, omega_pe=1e6)
        self.assertLess(gamma, 0.0)


if __name__ == "__main__":
    unittest.main()
