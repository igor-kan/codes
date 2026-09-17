"""Unit tests for Maxwell Stress Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from maxwell_stress_tensor import MaxwellStressTensor


class TestMaxwellStressTensor(unittest.TestCase):
    def test_poynting_direction(self):
        e = [1.0, 0.0, 0.0]
        b = [0.0, 1.0, 0.0]
        mst = MaxwellStressTensor(e, b)
        s = mst.poynting_vector()
        self.assertGreater(s[2], 0.0)
        self.assertAlmostEqual(s[0], 0.0)
        self.assertAlmostEqual(s[1], 0.0)


if __name__ == "__main__":
    unittest.main()
