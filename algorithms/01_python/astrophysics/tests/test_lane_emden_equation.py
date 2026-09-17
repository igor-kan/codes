"""Unit tests for Lane-Emden equation solver."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lane_emden_equation import LaneEmdenSolver


class TestLaneEmden(unittest.TestCase):
    def test_polytrope_n0(self):
        # For n=0, analytic solution is theta(xi) = 1 - xi^2 / 6, zero at xi_1 = sqrt(6) ~ 2.44949
        solver = LaneEmdenSolver(n=0.0, dxi=1e-3)
        xi_arr, th_arr, xi_surf, dth_surf = solver.solve()
        expected_xi_1 = np.sqrt(6.0)
        self.assertAlmostEqual(xi_surf, expected_xi_1, places=2)

    def test_polytrope_n1(self):
        # For n=1, analytic solution is theta(xi) = sin(xi)/xi, zero at xi_1 = pi ~ 3.14159
        solver = LaneEmdenSolver(n=1.0, dxi=1e-3)
        xi_arr, th_arr, xi_surf, dth_surf = solver.solve()
        self.assertAlmostEqual(xi_surf, np.pi, places=2)


if __name__ == "__main__":
    unittest.main()
