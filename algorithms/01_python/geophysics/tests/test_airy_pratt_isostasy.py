"""Unit tests for isostasy models."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from airy_pratt_isostasy import IsostasyModels


class TestIsostasy(unittest.TestCase):
    def test_airy_mountain_root(self):
        # 3 km mountain, rho_c=2700, rho_m=3300 -> delta_rho = 600
        # r = 3000 * 2700 / 600 = 13500 m = 13.5 km root
        r = IsostasyModels.airy_root_thickness(3000.0, 2700.0, 3300.0)
        self.assertAlmostEqual(r, 13500.0, places=1)


if __name__ == "__main__":
    unittest.main()
