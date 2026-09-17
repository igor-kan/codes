"""Unit tests for Inertia Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from inertia_tensor import InertiaTensor


class TestInertiaTensor(unittest.TestCase):
    def test_dumbbell_inertia(self):
        # Two equal masses m=1.0 at (0, 1, 0) and (0, -1, 0)
        masses = [1.0, 1.0]
        positions = [[0.0, 1.0, 0.0], [0.0, -1.0, 0.0]]
        i_tensor = InertiaTensor.from_point_masses(masses, positions)
        evals, _ = i_tensor.principal_moments_and_axes()
        # Rotation around y-axis has zero inertia
        self.assertAlmostEqual(evals[0], 0.0)
        # Rotation around x and z has I = 2 * (1.0 * 1^2) = 2.0
        self.assertAlmostEqual(evals[1], 2.0)
        self.assertAlmostEqual(evals[2], 2.0)

    def test_parallel_axis(self):
        # Point mass at origin shifted by (1, 0, 0)
        i0 = InertiaTensor(np.zeros((3, 3)))
        i_shifted = i0.parallel_axis_theorem(total_mass=2.0, shift_vector=[1.0, 0.0, 0.0])
        # d=(1,0,0), d^2=1 => I_xx = 0, I_yy = 2, I_zz = 2
        np.testing.assert_allclose(i_shifted.i_mat, np.diag([0.0, 2.0, 2.0]))


if __name__ == "__main__":
    unittest.main()
