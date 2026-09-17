"""Unit tests for Boltzmann BGK."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from boltzmann_transport_bgk import BoltzmannBGK1D


class TestBoltzmannBGK(unittest.TestCase):
    def test_exponential_decay(self):
        bgk = BoltzmannBGK1D(relaxation_time=1.0)
        f0 = np.array([2.0, 4.0])
        feq = np.array([1.0, 1.0])
        f_next = bgk.relax_step(f0, feq, dt=0.5)
        # 2 + 0.5*(1 - 2) = 1.5
        self.assertAlmostEqual(f_next[0], 1.5)


if __name__ == "__main__":
    unittest.main()
