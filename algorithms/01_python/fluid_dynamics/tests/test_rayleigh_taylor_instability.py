"""Unit tests for Rayleigh-Taylor Instability."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rayleigh_taylor_instability import RayleighTaylorInstability


class TestRayleighTaylor(unittest.TestCase):
    def test_stable_configuration(self):
        # Heavy fluid at bottom => Atwood number negative, zero growth
        gamma = RayleighTaylorInstability.growth_rate(wavenumber_k=10.0, rho_heavy=1.0, rho_light=2.0)
        self.assertEqual(gamma, 0.0)


if __name__ == "__main__":
    unittest.main()
