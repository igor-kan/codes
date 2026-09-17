"""Unit tests for Density Matrix."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from density_matrix import DensityMatrix


class TestDensityMatrix(unittest.TestCase):
    def test_maximally_mixed_state(self):
        # rho = 1/2 I_2 has purity 0.5 and von Neumann entropy 1 bit
        rho_mat = 0.5 * np.eye(2, dtype=np.complex128)
        dm = DensityMatrix(rho_mat)
        self.assertAlmostEqual(dm.purity, 0.5)
        self.assertAlmostEqual(dm.von_neumann_entropy, 1.0)

    def test_bell_state_entanglement_entropy(self):
        # Bell state |Phi+> = 1/sqrt(2) (|00> + |11>)
        psi = np.zeros(4, dtype=np.complex128)
        psi[0] = 1.0 / np.sqrt(2)
        psi[3] = 1.0 / np.sqrt(2)
        rho_bell = np.outer(psi, psi.conj())
        rho_a = DensityMatrix.partial_trace_bipartite(rho_bell, 2, 2)
        dm_a = DensityMatrix(rho_a)
        # Reduced state of Bell pair is maximally mixed with S = 1.0
        self.assertAlmostEqual(dm_a.von_neumann_entropy, 1.0)


if __name__ == "__main__":
    unittest.main()
