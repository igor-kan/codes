"""Unit tests for Vlasov 1D."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vlasov_maxwell_1d import Vlasov1D


class TestVlasov(unittest.TestCase):
    def test_advection_conservation(self):
        vlasov = Vlasov1D(nx=20, nv=10, dx=1.0, dv=1.0)
        vlasov.f[5, 5] = 1.0
        v_grid = np.linspace(-5, 5, 10)
        vlasov.advect_x(v_grid, dt=1.0)
        self.assertAlmostEqual(np.sum(vlasov.f), 1.0)


if __name__ == "__main__":
    unittest.main()
