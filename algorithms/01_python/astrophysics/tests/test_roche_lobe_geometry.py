"""Unit tests for Roche lobe geometry."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from roche_lobe_geometry import RocheLobe


class TestRocheLobe(unittest.TestCase):
    def test_equal_mass_binary(self):
        # For q=1, r_L / a ~ 0.37888
        ratio = RocheLobe.eggleton_radius_ratio(1.0)
        self.assertAlmostEqual(ratio, 0.37888, places=3)


if __name__ == "__main__":
    unittest.main()
