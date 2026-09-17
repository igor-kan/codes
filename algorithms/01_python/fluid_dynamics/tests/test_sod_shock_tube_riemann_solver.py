"""Unit tests for Sod Shock Tube Benchmark."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sod_shock_tube_riemann_solver import SodShockTubeBenchmark


class TestSodShockTube(unittest.TestCase):
    def test_sound_speeds(self):
        cl, cr = SodShockTubeBenchmark.acoustic_speeds()
        self.assertAlmostEqual(cl, np.sqrt(1.4))
        self.assertAlmostEqual(cr, np.sqrt(1.4 * 0.1 / 0.125))


if __name__ == "__main__":
    unittest.main()
