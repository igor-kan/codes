"""Unit tests for Foucault Pendulum Geometric Phase."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from foucault_pendulum_geometric_phase import FoucaultPendulumGeometricPhase


class TestFoucaultPendulum(unittest.TestCase):
    def test_north_pole_precession(self):
        # At north pole lambda = pi/2: completes 2pi in 24 hours
        fp = FoucaultPendulumGeometricPhase(latitude_radians=np.pi / 2.0)
        rate = fp.precession_rate()
        self.assertAlmostEqual(rate, -fp.EARTH_OMEGA)
        phase = fp.geometric_phase_per_day()
        self.assertAlmostEqual(phase, 0.0)

    def test_equator_no_precession(self):
        # At equator lambda = 0: no precession
        fp = FoucaultPendulumGeometricPhase(latitude_radians=0.0)
        self.assertAlmostEqual(fp.precession_rate(), 0.0)


if __name__ == "__main__":
    unittest.main()
