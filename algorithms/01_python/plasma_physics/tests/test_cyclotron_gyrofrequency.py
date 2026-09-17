"""Unit tests for Cyclotron Kinematics."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cyclotron_gyrofrequency import CyclotronKinematics


class TestCyclotron(unittest.TestCase):
    def test_proton_larmor_radius(self):
        # Proton q = 1.6e-19, m = 1.67e-27, B = 1.0 T, v_perp = 1e5 m/s
        rl = CyclotronKinematics.larmor_radius(perpendicular_velocity=1e5, charge=1.6e-19, magnetic_field=1.0, mass=1.67e-27)
        # r_L = 1.67e-27 * 1e5 / 1.6e-19 approx 1 mm
        self.assertAlmostEqual(rl, 1.04e-3, places=4)


if __name__ == "__main__":
    unittest.main()
