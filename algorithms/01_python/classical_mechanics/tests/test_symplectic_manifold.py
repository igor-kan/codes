"""Unit tests for Symplectic Manifold."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from symplectic_manifold import SymplecticManifold


class TestSymplecticManifold(unittest.TestCase):
    def test_j_properties(self):
        sm = SymplecticManifold(degrees_of_freedom=2)
        j = sm.j_matrix
        # J^2 = -I
        np.testing.assert_allclose(j @ j, -np.eye(4))
        # J^T = -J
        np.testing.assert_allclose(j.T, -j)
        # J is itself a symplectic matrix: J^T J J = (-J)(-I) = J
        self.assertTrue(sm.is_symplectic_matrix(j))

    def test_harmonic_rotation_is_symplectic(self):
        sm = SymplecticManifold(degrees_of_freedom=1)
        theta = np.pi / 4.0
        # Phase flow of harmonic oscillator is a rotation in (q, p)
        rot = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        self.assertTrue(sm.is_symplectic_matrix(rot))


if __name__ == "__main__":
    unittest.main()
