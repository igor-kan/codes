"""Unit tests for Torsion Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from torsion_tensor import TorsionTensor


class TestTorsionTensor(unittest.TestCase):
    def test_symmetric_connection(self):
        gamma = np.zeros((3, 3, 3))
        gamma[0, 1, 2] = 2.0
        gamma[0, 2, 1] = 2.0
        tt = TorsionTensor(gamma)
        self.assertTrue(tt.is_torsion_free())


if __name__ == "__main__":
    unittest.main()
