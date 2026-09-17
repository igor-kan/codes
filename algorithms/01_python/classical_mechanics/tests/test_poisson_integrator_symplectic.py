"""Unit tests for Symplectic Integrators."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poisson_integrator_symplectic import SymplecticIntegrator


class TestSymplecticIntegrator(unittest.TestCase):
    def test_harmonic_oscillator_stability(self):
        # V = 1/2 k q^2 with k = 1 => grad V = q
        si = SymplecticIntegrator(grad_v=lambda q: q, mass=1.0)
        q_hist, p_hist = si.integrate(q0=[1.0], p0=[0.0], dt=0.1, steps=500)
        # Verify energy does not drift away: E = 1/2 (p^2 + q^2) approx 0.5
        energies = 0.5 * (p_hist[:, 0]**2 + q_hist[:, 0]**2)
        drift = abs(energies[-1] - energies[0])
        self.assertLess(drift, 0.02)


if __name__ == "__main__":
    unittest.main()
