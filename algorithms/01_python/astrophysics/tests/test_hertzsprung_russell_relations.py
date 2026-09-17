"""Unit tests for HR relations."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hertzsprung_russell_relations import StellarHRRelations


class TestHRRelations(unittest.TestCase):
    def test_solar_stefan_boltzmann(self):
        l_calc = StellarHRRelations.stefan_boltzmann_luminosity(StellarHRRelations.R_SUN, StellarHRRelations.T_SUN)
        self.assertAlmostEqual(l_calc / StellarHRRelations.L_SUN, 1.0, places=2)


if __name__ == "__main__":
    unittest.main()
