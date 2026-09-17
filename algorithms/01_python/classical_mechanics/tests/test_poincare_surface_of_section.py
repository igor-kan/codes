"""Unit tests for Poincare Surface of Section."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poincare_surface_of_section import PoincareSection


class TestPoincareSection(unittest.TestCase):
    def test_harmonic_section_crossing(self):
        # 1D harmonic oscillator: x(t) = sin(t)
        t = np.linspace(0, 4 * np.pi, 200)
        z = np.column_stack([np.sin(t), np.cos(t)])  # (x, p)
        crossings = PoincareSection.extract_crossings(t, z, cross_dim=0, cross_val=0.0)
        # Sin(t) crosses 0 with positive derivative at t = 2 pi
        self.assertEqual(len(crossings), 2)
        # At crossing x approx 0, p approx 1
        self.assertAlmostEqual(crossings[0][0], 0.0, places=2)
        self.assertAlmostEqual(crossings[0][1], 1.0, places=2)


if __name__ == "__main__":
    unittest.main()
