"""Unit tests for Hamilton-Jacobi Solver."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hamilton_jacobi_equation import HamiltonJacobiSolver


class TestHamiltonJacobiSolver(unittest.TestCase):
    def test_harmonic_oscillator_action(self):
        # E = 1/2 k A^2 => Action over full period is J = E / nu = 2 pi E / omega
        k = 4.0
        m = 1.0
        omega = np.sqrt(k / m)  # = 2.0
        e = 8.0
        amplitude = np.sqrt(2.0 * e / k)  # = 2.0
        v_func = lambda q: 0.5 * k * (q**2)

        hj = HamiltonJacobiSolver(energy=e)
        # Half period from -A to +A
        half_action = hj.action_integral_1d(v_func, mass=m, q1=-amplitude * 0.9999, q2=amplitude * 0.9999)
        full_action = 2.0 * half_action
        expected_action = 2.0 * np.pi * e / omega  # = 8 pi approx 25.1327
        self.assertAlmostEqual(full_action, expected_action, delta=0.05)


if __name__ == "__main__":
    unittest.main()
