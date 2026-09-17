"""Unit tests for Langevin Dynamics."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from langevin_dynamics_sim import LangevinDynamics


class TestLangevinDynamics(unittest.TestCase):
    def test_thermal_velocity_scale(self):
        ld = LangevinDynamics(mass=1.0, friction=0.5, temperature=1.0)
        x, v = 0.0, 0.0
        for _ in range(200):
            x, v = ld.step(x, v, dt=0.01)
        # Velocity should remain on order sqrt(k_B T / m) = 1.0
        self.assertLess(abs(v), 5.0)


if __name__ == "__main__":
    unittest.main()
