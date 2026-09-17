"""Unit tests for Fermi-Dirac Gas."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fermi_dirac_gas import FermiDiracGas


class TestFermiDirac(unittest.TestCase):
    def test_fermi_energy_positive(self):
        n_density = 8.5e28  # Copper electron density (m^-3)
        ef = FermiDiracGas.fermi_energy_3d(n_density)
        # E_F approx 7 eV approx 1.1e-18 J
        self.assertGreater(ef, 1e-19)
        self.assertLess(ef, 1e-17)


if __name__ == "__main__":
    unittest.main()
