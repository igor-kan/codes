"""Unit tests for Acoustic Helmholtz."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from acoustic_wave_equation_helmholtz import AcousticHelmholtz


class TestAcousticHelmholtz(unittest.TestCase):
    def test_air_impedance(self):
        # Air at 20 C: rho approx 1.2 kg/m^3, c approx 343 m/s => Z approx 411.6 Rayl
        z = AcousticHelmholtz.characteristic_impedance(fluid_density=1.2, sound_speed=343.0)
        self.assertAlmostEqual(z, 411.6)


if __name__ == "__main__":
    unittest.main()
