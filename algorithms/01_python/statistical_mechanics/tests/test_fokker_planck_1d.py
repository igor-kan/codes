"""Unit tests for Fokker-Planck Solver."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fokker_planck_1d import FokkerPlanck1D


class TestFokkerPlanck(unittest.TestCase):
    def test_pure_diffusion_conservation(self):
        x = np.linspace(-5.0, 5.0, 50)
        fp = FokkerPlanck1D(x, drift_a=lambda x: 0.0, diffusion_b=1.0)
        p0 = np.exp(-x**2)
        p0 = p0 / np.sum(p0)
        p1 = fp.step(p0, dt=0.001)
        self.assertAlmostEqual(np.sum(p1), 1.0, places=4)


if __name__ == "__main__":
    unittest.main()
