"""Unit tests for Couette-Poiseuille Flows."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from couette_poiseuille_flow import ExactLaminarFlows


class TestExactLaminar(unittest.TestCase):
    def test_pipe_flow_centerline_max(self):
        # Centerline r = 0 has maximum velocity
        u_max = ExactLaminarFlows.hagen_poiseuille_velocity(r=0.0, pipe_radius_r=0.1, pressure_gradient=-100.0, dynamic_viscosity=1.0)
        u_wall = ExactLaminarFlows.hagen_poiseuille_velocity(r=0.1, pipe_radius_r=0.1, pressure_gradient=-100.0, dynamic_viscosity=1.0)
        self.assertGreater(u_max, 0.0)
        self.assertAlmostEqual(u_wall, 0.0)


if __name__ == "__main__":
    unittest.main()
