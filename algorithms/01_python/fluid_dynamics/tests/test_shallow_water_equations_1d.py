"""Unit tests for Shallow Water Equations."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from shallow_water_equations_1d import ShallowWater1D


class TestShallowWater(unittest.TestCase):
    def test_critical_froude(self):
        c = ShallowWater1D.wave_speed(water_depth_h=4.0)
        fr = ShallowWater1D.froude_number(flow_velocity_u=c, water_depth_h=4.0)
        self.assertAlmostEqual(fr, 1.0)


if __name__ == "__main__":
    unittest.main()
