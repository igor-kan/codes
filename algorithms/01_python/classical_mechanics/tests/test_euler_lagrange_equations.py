"""Unit tests for Euler-Lagrange Equations."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from euler_lagrange_equations import EulerLagrangeSystem


class TestEulerLagrangeEquations(unittest.TestCase):
    def test_cyclic_coordinate_central_potential(self):
        # 2D polar central potential: L = 1/2 m (rdot^2 + r^2 phidot^2) - V(r)
        # phi is a cyclic coordinate => conjugate angular momentum p_phi is conserved!
        m = 1.0
        l_func = lambda q, qd, t: 0.5 * m * (qd[0]**2 + (q[0]**2) * (qd[1]**2)) - (1.0 / q[0])
        el = EulerLagrangeSystem(l_func, degrees_of_freedom=2)
        cyclic = el.cyclic_coordinates(q_sample=[2.0, 1.5], q_dot_sample=[0.5, 1.0])
        # Index 1 (phi) must be cyclic
        self.assertIn(1, cyclic)


if __name__ == "__main__":
    unittest.main()
