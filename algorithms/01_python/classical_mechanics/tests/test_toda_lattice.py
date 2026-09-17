"""Unit tests for Toda Lattice."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from toda_lattice import TodaLattice


class TestTodaLattice(unittest.TestCase):
    def test_lax_symmetry(self):
        tl = TodaLattice(positions=[0.0, 1.0, 2.5], momenta=[0.5, -0.2, 0.1])
        l_mat = tl.flaschka_variables()
        np.testing.assert_allclose(l_mat, l_mat.T)
        invs = tl.conserved_quantities()
        self.assertEqual(len(invs), 3)


if __name__ == "__main__":
    unittest.main()
