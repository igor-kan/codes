"""Unit tests for Navier-Stokes Vorticity Streamfunction."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from navier_stokes_2d_vorticity_streamfunction import VorticityStreamfunction2D


class TestVorticityStreamfunction(unittest.TestCase):
    def test_couette_streamfunction(self):
        ns = VorticityStreamfunction2D(nx=10, ny=10, dx=1.0, kinematic_viscosity=0.01)
        # psi(x, y) = 1/2 y^2 => u = d psi / dy = y
        y = np.arange(10)
        for i in range(10):
            ns.psi[i, :] = 0.5 * (y**2)
        u, v = ns.velocities_from_streamfunction()
        # u at y=5 should be 5.0
        self.assertAlmostEqual(u[5, 5], 5.0)
        self.assertAlmostEqual(v[5, 5], 0.0)


if __name__ == "__main__":
    unittest.main()
