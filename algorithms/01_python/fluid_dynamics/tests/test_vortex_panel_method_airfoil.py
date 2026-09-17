"""Unit tests for Thin Airfoil Theory."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vortex_panel_method_airfoil import ThinAirfoilTheory


class TestAirfoil(unittest.TestCase):
    def test_lift_slope(self):
        cl = ThinAirfoilTheory.lift_coefficient(angle_of_attack_rad=np.radians(5.0))
        # 2 pi * (5 * pi / 180) approx 0.548
        self.assertAlmostEqual(cl, 2.0 * np.pi * np.radians(5.0))


if __name__ == "__main__":
    unittest.main()
