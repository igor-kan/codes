"""Unit tests for surface waves."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rayleigh_love_surface_waves import SurfaceWaves


class TestSurfaceWaves(unittest.TestCase):
    def test_rayleigh_velocity_ratio(self):
        vp, vs = 5000.0, 3000.0
        vr = SurfaceWaves.rayleigh_wave_velocity(vp, vs)
        # Rayleigh wave velocity is approx 0.90 to 0.93 of S-wave velocity
        ratio = vr / vs
        self.assertTrue(0.88 <= ratio <= 0.95)


if __name__ == "__main__":
    unittest.main()
