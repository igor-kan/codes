"""Unit tests for Weyl Curvature Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from weyl_tensor import WeylCurvatureTensor


class TestWeylTensor(unittest.TestCase):
    def test_conformally_flat_minkowski(self):
        g = np.diag([-1.0, 1.0, 1.0, 1.0])
        r_cov = np.zeros((4, 4, 4, 4))
        ricci = np.zeros((4, 4))
        weyl = WeylCurvatureTensor.from_riemann_and_ricci(r_cov, ricci, 0.0, g)
        self.assertTrue(weyl.is_conformally_flat())


if __name__ == "__main__":
    unittest.main()
