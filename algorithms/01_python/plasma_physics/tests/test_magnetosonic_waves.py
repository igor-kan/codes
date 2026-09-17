"""Unit tests for Magnetosonic Waves."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from magnetosonic_waves import MagnetosonicWaves


class TestMagnetosonic(unittest.TestCase):
    def test_perpendicular_propagation(self):
        # At theta = pi/2: v_fast = sqrt(v_A^2 + c_s^2), v_slow = 0
        vf, vs = MagnetosonicWaves.phase_speeds(alfven_speed=3.0, sound_speed=4.0, propagation_angle_theta=np.pi / 2.0)
        self.assertAlmostEqual(vf, 5.0)
        self.assertAlmostEqual(vs, 0.0)


if __name__ == "__main__":
    unittest.main()
