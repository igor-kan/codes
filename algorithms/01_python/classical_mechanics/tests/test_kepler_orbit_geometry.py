"""Unit tests for Kepler Orbit Geometry."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kepler_orbit_geometry import KeplerOrbitGeometry


class TestKeplerOrbitGeometry(unittest.TestCase):
    def test_periapsis_and_apoapsis(self):
        a = 10.0
        e = 0.2
        orbit = KeplerOrbitGeometry(semi_major_axis=a, eccentricity=e)
        r_peri = orbit.orbital_radius(true_anomaly=0.0)
        r_apo = orbit.orbital_radius(true_anomaly=np.pi)
        self.assertAlmostEqual(r_peri, a * (1.0 - e))  # = 8.0
        self.assertAlmostEqual(r_apo, a * (1.0 + e))   # = 12.0

    def test_kepler_solver_circular(self):
        orbit = KeplerOrbitGeometry(semi_major_axis=1.0, eccentricity=0.0)
        m = np.pi / 3.0
        e_sol = orbit.solve_kepler_equation(m)
        self.assertAlmostEqual(e_sol, m)


if __name__ == "__main__":
    unittest.main()
