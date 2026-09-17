"""Unit tests for Quadrupole Moment Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quadrupole_moment_tensor import QuadrupoleMomentTensor


class TestQuadrupoleMomentTensor(unittest.TestCase):
    def test_traceless_property(self):
        charges = [1.0, -1.0, 1.0, -1.0]
        pos = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [-1.0, 0.0, 0.0], [0.0, -1.0, 0.0]]
        quad = QuadrupoleMomentTensor.from_charges(charges, pos)
        self.assertAlmostEqual(np.trace(quad.q), 0.0)


if __name__ == "__main__":
    unittest.main()
