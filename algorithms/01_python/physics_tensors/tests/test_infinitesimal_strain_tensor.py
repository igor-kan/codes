"""Unit tests for Infinitesimal Strain Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from infinitesimal_strain_tensor import InfinitesimalStrainTensor


class TestInfinitesimalStrainTensor(unittest.TestCase):
    def test_rigid_body_rotation(self):
        # Pure antisymmetric gradient has zero strain
        grad_u = [
            [0.0, -0.05, 0.0],
            [0.05, 0.0, 0.0],
            [0.0, 0.0, 0.0]
        ]
        strain, omega = InfinitesimalStrainTensor.from_displacement_gradient(grad_u)
        np.testing.assert_allclose(strain.strain, np.zeros((3, 3)), atol=1e-12)
        np.testing.assert_allclose(omega, grad_u)


if __name__ == "__main__":
    unittest.main()
