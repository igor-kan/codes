"""Unit tests for Duffing oscillator."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from duffing_chaotic_oscillator import DuffingOscillator


class TestDuffing(unittest.TestCase):
    def test_integration(self):
        duff = DuffingOscillator()
        t, traj = duff.integrate_rk4(np.array([1.0, 0.0]), dt=0.01, steps=100)
        self.assertEqual(traj.shape, (101, 2))


if __name__ == "__main__":
    unittest.main()
