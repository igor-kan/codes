"""Unit tests for Bose-Einstein Condensate."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bose_einstein_condensate import BoseEinsteinCondensation


class TestBEC(unittest.TestCase):
    def test_condensed_fraction_at_half_tc(self):
        tc = 100e-9  # 100 nK
        frac = BoseEinsteinCondensation.condensed_fraction(t=50e-9, t_c=tc)
        # 1 - (0.5)^3 = 1 - 0.125 = 0.875
        self.assertAlmostEqual(frac, 0.875)


if __name__ == "__main__":
    unittest.main()
