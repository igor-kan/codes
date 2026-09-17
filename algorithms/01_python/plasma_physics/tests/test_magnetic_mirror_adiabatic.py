"""Unit tests for Magnetic Mirror."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from magnetic_mirror_adiabatic import MagneticMirror


class TestMagneticMirror(unittest.TestCase):
    def test_loss_cone_ratio_4(self):
        # Mirror ratio R_m = 4 => sin(alpha) = 1/2 => alpha = 30 deg = pi/6
        angle = MagneticMirror.loss_cone_angle_radians(b_min=1.0, b_max=4.0)
        self.assertAlmostEqual(angle, np.pi / 6.0)


if __name__ == "__main__":
    unittest.main()
