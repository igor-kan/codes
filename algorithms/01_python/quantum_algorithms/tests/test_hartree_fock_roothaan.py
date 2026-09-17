"""Unit tests for Hartree-Fock Roothaan."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hartree_fock_roothaan import HartreeFockRoothaan


class TestHartreeFock(unittest.TestCase):
    def test_scf_step(self):
        f = np.array([[2.0, -0.5], [-0.5, 3.0]])
        s = np.eye(2)
        eps, p = HartreeFockRoothaan.scf_step(f, s, num_occupied_orbitals=1)
        self.assertEqual(len(eps), 2)
        # Trace of density matrix should be 2 * N_occ = 2
        self.assertAlmostEqual(np.trace(p), 2.0)


if __name__ == "__main__":
    unittest.main()
