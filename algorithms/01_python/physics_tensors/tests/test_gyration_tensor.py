"""Unit tests for Gyration Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gyration_tensor import GyrationTensor


class TestGyrationTensor(unittest.TestCase):
    def test_linear_rod(self):
        # 1D line along x-axis
        coords = [[x, 0.0, 0.0] for x in [-2.0, -1.0, 0.0, 1.0, 2.0]]
        gyr = GyrationTensor(coords)
        b, c, kappa2 = gyr.shape_descriptors()
        # For an ideal rod, kappa^2 = 1.0
        self.assertAlmostEqual(kappa2, 1.0)


if __name__ == "__main__":
    unittest.main()
