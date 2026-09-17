"""Unit tests for Eddington Luminosity."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from eddington_luminosity import EddingtonLimit


class TestEddington(unittest.TestCase):
    def test_solar_mass_luminosity(self):
        l_edd = EddingtonLimit.luminosity(EddingtonLimit.M_SUN)
        # Solar mass Eddington luminosity is approx 1.26e31 W (~3.3e4 L_sun)
        l_solar_ratio = l_edd / EddingtonLimit.L_SUN
        self.assertTrue(3.0e4 <= l_solar_ratio <= 3.6e4)


if __name__ == "__main__":
    unittest.main()
