"""Unit tests for Noether's Theorem."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from noether_theorem import NoetherTheorem


class TestNoetherTheorem(unittest.TestCase):
    def test_angular_momentum_conservation(self):
        r = [1.0, 0.0, 0.0]
        p = [0.0, 2.0, 0.0]
        l = NoetherTheorem.angular_momentum_3d(r, p)
        np.testing.assert_allclose(l, [0.0, 0.0, 2.0])

    def test_runge_lenz_circular_orbit(self):
        # In circular orbit, eccentricity e = 0 => Runge-Lenz vector magnitude ||A|| = 0
        m = 1.0
        k = 1.0
        r_val = 2.0
        v_val = np.sqrt(k / (m * r_val))  # Circular orbit velocity
        r = [r_val, 0.0, 0.0]
        v = [0.0, v_val, 0.0]
        a_vec = NoetherTheorem.runge_lenz_vector(r, v, mass=m, k_potential=k)
        np.testing.assert_allclose(a_vec, [0.0, 0.0, 0.0], atol=1e-10)


if __name__ == "__main__":
    unittest.main()
