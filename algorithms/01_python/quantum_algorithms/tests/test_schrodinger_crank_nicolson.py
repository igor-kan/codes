"""Unit tests for Crank-Nicolson Schrodinger Solver."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schrodinger_crank_nicolson import CrankNicolsonSchrodinger


class TestCrankNicolson(unittest.TestCase):
    def test_norm_preservation(self):
        x = np.linspace(-5.0, 5.0, 100)
        v = np.zeros_like(x)
        solver = CrankNicolsonSchrodinger(x, v)
        # Initial Gaussian wavepacket
        psi0 = np.exp(-x**2).astype(np.complex128)
        psi0 = psi0 / np.linalg.norm(psi0)

        psi1 = solver.step(psi0, dt=0.05)
        self.assertAlmostEqual(np.linalg.norm(psi1), 1.0)


if __name__ == "__main__":
    unittest.main()
