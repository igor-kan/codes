"""Unit tests for Legendre Transform."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from legendre_transform import LegendreTransform


class TestLegendreTransform(unittest.TestCase):
    def test_standard_particle_hamiltonian(self):
        # L = 1/2 m v^2 - V(q) with m = 2.0, V(q) = 3 q^2
        m = 2.0
        l_func = lambda q, qd: 0.5 * m * (qd[0]**2) - 3.0 * (q[0]**2)
        lt = LegendreTransform(l_func, degrees_of_freedom=1)
        self.assertTrue(lt.hessian_convexity_check([1.0], [2.0]))

        # For p = 6.0, qd = p/m = 3.0 => H = 1/2 (6^2 / 2) + 3 (1^2) = 9 + 3 = 12
        h_val = lt.evaluate_hamiltonian(q=[1.0], p=[6.0], q_dot_guess=[1.0])
        self.assertAlmostEqual(h_val, 12.0, places=4)


if __name__ == "__main__":
    unittest.main()
