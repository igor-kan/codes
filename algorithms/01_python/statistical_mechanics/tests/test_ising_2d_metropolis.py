"""Unit tests for 2D Ising Metropolis."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ising_2d_metropolis import Ising2DMetropolis


class TestIsingMetropolis(unittest.TestCase):
    def test_low_temperature_ferromagnetism(self):
        # At very low temperature T = 0.1 << T_c, spins align
        ising = Ising2DMetropolis(size=6, temperature=0.1)
        # Force all spins to +1
        ising.spins = np.ones((6, 6), dtype=int)
        ising.sweep(sweeps=5)
        # Magnetization remains near 1
        self.assertAlmostEqual(abs(ising.magnetization()), 1.0)


if __name__ == "__main__":
    unittest.main()
