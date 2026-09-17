"""Unit tests for Rossler attractor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rossler_attractor import RosslerAttractor


class TestRossler(unittest.TestCase):
    def test_trajectory(self):
        rossler = RosslerAttractor()
        traj = rossler.integrate(np.array([0.1, 0.1, 0.1]), dt=0.01, steps=100)
        self.assertEqual(traj.shape, (101, 3))


if __name__ == "__main__":
    unittest.main()
