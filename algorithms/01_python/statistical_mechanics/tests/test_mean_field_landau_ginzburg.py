"""Unit tests for Landau-Ginzburg Mean Field."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mean_field_landau_ginzburg import LandauGinzburgMeanField


class TestLandauGinzburg(unittest.TestCase):
    def test_spontaneous_symmetry_breaking(self):
        lg = LandauGinzburgMeanField(t_critical=10.0, a_coeff=2.0, b_coeff=1.0)
        m_above = lg.spontaneous_magnetization(temperature=12.0)
        m_below = lg.spontaneous_magnetization(temperature=9.0)
        self.assertEqual(m_above, 0.0)
        # Sqrt(2 * 1 / 2) = 1.0
        self.assertAlmostEqual(m_below, 1.0)


if __name__ == "__main__":
    unittest.main()
