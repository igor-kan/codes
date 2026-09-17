"""Unit tests for Small Oscillations."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from small_oscillations import SmallOscillations


class TestSmallOscillations(unittest.TestCase):
    def test_two_coupled_masses(self):
        # Two equal masses m=1 connected by springs of stiffness k=10
        m_mat = np.eye(2)
        k_mat = np.array([[20.0, -10.0], [-10.0, 20.0]])
        so = SmallOscillations(m_mat, k_mat)
        freqs, modes = so.normal_modes()
        # Symmetric mode: omega_1 = sqrt(10) approx 3.162
        # Antisymmetric mode: omega_2 = sqrt(30) approx 5.477
        self.assertAlmostEqual(freqs[0], np.sqrt(10.0))
        self.assertAlmostEqual(freqs[1], np.sqrt(30.0))
        # Orthogonality check: A^T M A = I
        np.testing.assert_allclose(modes.T @ m_mat @ modes, np.eye(2), atol=1e-10)


if __name__ == "__main__":
    unittest.main()
