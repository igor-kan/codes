"""Unit tests for KAM Theorem Standard Map."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kam_theorem_mapping import ChirikovStandardMap


class TestKAMStandardMap(unittest.TestCase):
    def test_area_preservation(self):
        csm = ChirikovStandardMap(perturbation_k=0.5)
        det_val = csm.jacobian_determinant(theta=1.234)
        self.assertAlmostEqual(det_val, 1.0)

    def test_trajectory_length(self):
        csm = ChirikovStandardMap(perturbation_k=0.2)
        th, p = csm.iterate_trajectory(0.1, 0.2, steps=50)
        self.assertEqual(len(th), 50)
        self.assertEqual(len(p), 50)


if __name__ == "__main__":
    unittest.main()
