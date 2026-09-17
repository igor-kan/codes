"""Unit tests for Lorenz attractor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lorenz_attractor_rk4 import LorenzAttractor


class TestLorenz(unittest.TestCase):
    def test_trajectory_shape(self):
        lorenz = LorenzAttractor()
        traj = lorenz.integrate(np.array([1.0, 1.0, 1.0]), dt=0.01, steps=100)
        self.assertEqual(traj.shape, (101, 3))
        # Fixed point at origin is unstable for rho > 1
        deriv_origin = lorenz.derivatives(np.zeros(3))
        np.testing.assert_array_equal(deriv_origin, np.zeros(3))


if __name__ == "__main__":
    unittest.main()
