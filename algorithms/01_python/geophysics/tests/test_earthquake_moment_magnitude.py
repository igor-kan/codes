"""Unit tests for moment magnitude."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from earthquake_moment_magnitude import MomentMagnitude


class TestMomentMagnitude(unittest.TestCase):
    def test_magnitude_calculation(self):
        # M0 = 1e19 N*m -> Mw ~ 6.6
        mw = MomentMagnitude.moment_magnitude(1e19)
        self.assertAlmostEqual(mw, 6.60, places=1)


if __name__ == "__main__":
    unittest.main()
