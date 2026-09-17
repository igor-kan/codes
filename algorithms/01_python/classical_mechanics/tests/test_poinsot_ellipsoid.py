"""Unit tests for Poinsot Construction."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poinsot_ellipsoid import PoinsotConstruction


class TestPoinsotEllipsoid(unittest.TestCase):
    def test_symmetric_top_poinsot(self):
        # I_1 = I_2 = 1.0, I_3 = 2.0, E = 1.0, L^2 = 3.0
        # 2E I_1 = 2 <= 3 <= 2E I_3 = 4
        pc = PoinsotConstruction(principal_moments=[1.0, 1.0, 2.0], kinetic_energy=1.0, angular_momentum_sq=3.0)
        h = pc.invariable_plane_distance()
        self.assertAlmostEqual(h, 2.0 / np.sqrt(3.0))


if __name__ == "__main__":
    unittest.main()
