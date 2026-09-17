"""Unit tests for TOV solver."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tolman_oppenheimer_volkoff import TOVSolver


class TestTOV(unittest.TestCase):
    def test_constant_density_sphere(self):
        # Incompressible fluid EOS: rho = constant = 1e18 kg/m^3 (approx nuclear saturation)
        rho_const = 5e17
        solver = TOVSolver(eos_rho=lambda p: rho_const, p_central=1e33, dr=50.0, r_max=20000.0)
        r_arr, p_arr, m_arr, r_star, m_star = solver.solve()
        self.assertTrue(r_star > 1000.0)
        self.assertTrue(m_star > 1e29)


if __name__ == "__main__":
    unittest.main()
