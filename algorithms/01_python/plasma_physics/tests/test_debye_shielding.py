"""Unit tests for Debye Shielding."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from debye_shielding import DebyeShielding


class TestDebyeShielding(unittest.TestCase):
    def test_tokamak_debye_length(self):
        # Tokamak core: n_e = 1e20 m^-3, T_e = 1e8 K (10 keV)
        ld = DebyeShielding.debye_length(electron_density=1e20, electron_temp_kelvin=1e8)
        # lambda_D is on order of tens of microns
        self.assertGreater(ld, 1e-6)
        self.assertLess(ld, 1e-3)
        # Quasi-neutrality requires Lambda >> 1
        lam = DebyeShielding.plasma_parameter(1e20, 1e8)
        self.assertGreater(lam, 1e3)


if __name__ == "__main__":
    unittest.main()
