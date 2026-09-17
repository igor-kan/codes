"""Unit tests for Calogero-Moser System."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from integrable_systems_calogero_moser import CalogeroMoserSystem


class TestCalogeroMoser(unittest.TestCase):
    def test_total_momentum_and_hamiltonian(self):
        # 2 particles at q = [1.0, 3.0], p = [2.0, -1.0], g = 1.0
        cm = CalogeroMoserSystem(positions=[1.0, 3.0], momenta=[2.0, -1.0], coupling=1.0)
        invs = cm.conserved_trace_invariants(max_power=2)
        # I_1 = Tr(L) = p_1 + p_2 = 2 - 1 = 1.0 (total momentum)
        self.assertAlmostEqual(invs[0], 1.0)
        # I_2 = 1/2 Tr(L^2) = 1/2 (p_1^2 + p_2^2 + 2 g^2 / (q_1 - q_2)^2)
        # = 1/2 (4 + 1 + 2 * 1 / 4) = 1/2 (5 + 0.5) = 2.75 (Hamiltonian H)
        self.assertAlmostEqual(invs[1], 2.75)


if __name__ == "__main__":
    unittest.main()
