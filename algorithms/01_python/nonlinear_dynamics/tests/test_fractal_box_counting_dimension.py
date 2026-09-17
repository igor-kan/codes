"""Unit tests for box counting dimension."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fractal_box_counting_dimension import BoxCountingDimension


class TestBoxCounting(unittest.TestCase):
    def test_solid_2d_square(self):
        # A solid 2D square has dimension D ~ 2.0
        img = np.ones((128, 128), dtype=bool)
        dim = BoxCountingDimension.compute_dimension_2d(img, box_sizes=[2, 4, 8, 16, 32])
        self.assertAlmostEqual(dim, 2.0, places=1)


if __name__ == "__main__":
    unittest.main()
