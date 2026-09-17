"""Unit tests for VQE Solver."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vqe_ground_state import VQESolver


class TestVQESolver(unittest.TestCase):
    def test_ground_state_energy(self):
        # H = [[2, 1], [1, 2]] with eigenvalues 1 and 3 => ground energy = 1.0
        h = np.array([[2.0, 1.0], [1.0, 2.0]])
        vqe = VQESolver(h)
        e_vqe, e_exact = vqe.solve_2level_ansatz()
        self.assertAlmostEqual(e_vqe, 1.0, places=4)
        self.assertAlmostEqual(e_exact, 1.0, places=4)


if __name__ == "__main__":
    unittest.main()
