"""Unit tests for geomagnetic dipole."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from geomagnetic_dipole_field import GeomagneticDipole


class TestGeomagnetic(unittest.TestCase):
    def test_poles_and_equator(self):
        # At magnetic equator (latitude = 0), inclination I = 0
        inc_eq = GeomagneticDipole.magnetic_inclination(0.0)
        self.assertAlmostEqual(inc_eq, 0.0)
        # At magnetic north pole (colatitude = 0), B_theta = 0, B_r = -2 * B_0
        br, bt, btot = GeomagneticDipole.field_components(GeomagneticDipole.R_E, colatitude_rad=0.0)
        self.assertAlmostEqual(bt, 0.0)
        self.assertAlmostEqual(btot, 2.0 * GeomagneticDipole.B_0)


if __name__ == "__main__":
    unittest.main()
