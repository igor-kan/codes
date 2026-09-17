"""Unit tests for Arnold's cat map."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from arnold_cat_map import ArnoldCatMap


class TestArnoldCatMap(unittest.TestCase):
    def test_fixed_point_origin(self):
        nx, ny = ArnoldCatMap.step(0.0, 0.0)
        self.assertEqual(nx, 0.0)
        self.assertEqual(ny, 0.0)

    def test_lyapunov_exponent(self):
        lam = ArnoldCatMap.lyapunov_exponent()
        # lambda ~ ln(2.6180339887) ~ 0.96242
        self.assertAlmostEqual(lam, 0.96242, places=4)


if __name__ == "__main__":
    unittest.main()
