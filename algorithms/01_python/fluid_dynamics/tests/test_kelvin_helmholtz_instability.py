"""Unit tests for Kelvin-Helmholtz Instability."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kelvin_helmholtz_instability import KelvinHelmholtzInstability


class TestKelvinHelmholtz(unittest.TestCase):
    def test_shear_growth(self):
        growth = KelvinHelmholtzInstability.growth_rate(wavenumber_k=2.0, u1=10.0, u2=0.0, rho1=1.0, rho2=1.0)
        # 2.0 * 10.0 * 1.0 / 2.0 = 10.0
        self.assertAlmostEqual(growth, 10.0)


if __name__ == "__main__":
    unittest.main()
