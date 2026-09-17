"""Unit tests for Maxwell-Boltzmann Gas."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from maxwell_boltzmann_gas import MaxwellBoltzmannGas


class TestMaxwellBoltzmann(unittest.TestCase):
    def test_speed_ordering(self):
        gas = MaxwellBoltzmannGas(molecular_mass=4.65e-26, temperature=300.0)  # N2 molecule
        vp = gas.most_probable_speed()
        v_bar = gas.mean_speed()
        v_rms = gas.rms_speed()
        # Strictly v_p < <v> < v_rms
        self.assertLess(vp, v_bar)
        self.assertLess(v_bar, v_rms)


if __name__ == "__main__":
    unittest.main()
