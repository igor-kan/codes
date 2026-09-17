"""Unit tests for LBM D2Q9."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lattice_boltzmann_d2q9 import LatticeBoltzmannD2Q9


class TestLBM(unittest.TestCase):
    def test_equilibrium_density(self):
        lbm = LatticeBoltzmannD2Q9(nx=8, ny=8)
        rho, ux, uy = lbm.macroscopic_density_and_velocity()
        np.testing.assert_allclose(rho, np.ones((8, 8)))
        np.testing.assert_allclose(ux, np.zeros((8, 8)))


if __name__ == "__main__":
    unittest.main()
