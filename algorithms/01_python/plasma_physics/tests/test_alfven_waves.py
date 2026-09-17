"""Unit tests for Alfven Waves."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from alfven_waves import AlfvenWave


class TestAlfvenWaves(unittest.TestCase):
    def test_solar_wind_alfven_speed(self):
        # Solar wind at 1 AU: B = 5e-9 T, rho = 5 protons/cm^3 = 8.35e-21 kg/m^3
        va = AlfvenWave.alfven_speed(magnetic_field_tesla=5e-9, mass_density=8.35e-21)
        # v_A approx 50 km/s
        self.assertGreater(va, 30e3)
        self.assertLess(va, 70e3)


if __name__ == "__main__":
    unittest.main()
