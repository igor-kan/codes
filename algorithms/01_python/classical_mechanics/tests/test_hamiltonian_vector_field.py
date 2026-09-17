"""Unit tests for Hamiltonian Vector Field."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hamiltonian_vector_field import HamiltonianVectorField


class TestHamiltonianVectorField(unittest.TestCase):
    def test_harmonic_oscillator_flow(self):
        # H = 1/2 p^2 + 1/2 omega^2 q^2
        omega = 2.0
        h_func = lambda z: 0.5 * (z[1]**2) + 0.5 * (omega**2) * (z[0]**2)
        hvf = HamiltonianVectorField(h_func, degrees_of_freedom=1)
        z0 = [1.0, 3.0]
        # dot{q} = p = 3, dot{p} = -omega^2 q = -4
        flow = hvf.vector_field(z0)
        np.testing.assert_allclose(flow, [3.0, -4.0], atol=1e-4)

    def test_liouville_divergence_zero(self):
        # Non-linear pendulum: H = 1/2 p^2 - cos(q)
        h_func = lambda z: 0.5 * (z[1]**2) - np.cos(z[0])
        hvf = HamiltonianVectorField(h_func, degrees_of_freedom=1)
        div_val = hvf.divergence([1.2, 0.8])
        self.assertAlmostEqual(div_val, 0.0, places=4)


if __name__ == "__main__":
    unittest.main()
