"""Unit tests for KdV soliton."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from korteveg_de_vries_soliton import KdVSoliton


class TestKdV(unittest.TestCase):
    def test_single_soliton_shape_and_integral(self):
        x = np.linspace(-20, 20, 4001)
        dx = x[1] - x[0]
        c = 4.0
        u0 = KdVSoliton.single_soliton(x, t=0.0, c=c)
        ut = KdVSoliton.single_soliton(x, t=1.0, c=c)
        # Peak amplitude is c/2 = 2.0
        self.assertAlmostEqual(np.max(u0), 2.0, places=3)
        self.assertAlmostEqual(np.max(ut), 2.0, places=3)
        # Total integral int u dx = 2 * sqrt(c) = 4.0
        i1 = KdVSoliton.energy_invariant(u0, dx)
        self.assertAlmostEqual(i1, 4.0, places=2)


if __name__ == "__main__":
    unittest.main()
