"""Unit tests for oceanic crust cooling."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from oceanic_crust_cooling_halfspace import OceanicLithosphereCooling


class TestOceanicCooling(unittest.TestCase):
    def test_bathymetry(self):
        d0 = OceanicLithosphereCooling.seafloor_subsidence(0.0)
        self.assertEqual(d0, 2500.0)
        d64 = OceanicLithosphereCooling.seafloor_subsidence(64.0)
        # 2500 + 350 * 8 = 5300 m
        self.assertEqual(d64, 5300.0)


if __name__ == "__main__":
    unittest.main()
