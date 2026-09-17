"""Unit tests for NLSE solitons."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nonlinear_schrodinger_soliton import NLSESoliton


class TestNLSE(unittest.TestCase):
    def test_bright_soliton_peak(self):
        x = np.linspace(-10, 10, 1001)
        psi = NLSESoliton.bright_soliton(x, t=0.0, amplitude=2.0)
        prob_density = np.abs(psi) ** 2
        self.assertAlmostEqual(np.max(prob_density), 4.0, places=3)


if __name__ == "__main__":
    unittest.main()
