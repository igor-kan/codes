"""Unit tests for Chandler wobble."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from chandler_wobble_euler import EarthPrecession


class TestChandlerWobble(unittest.TestCase):
    def test_euler_period(self):
        # For (C - A)/A = 1/305
        a = 305.0
        c = 306.0
        tau_e = EarthPrecession.euler_period_days(a, c)
        self.assertAlmostEqual(tau_e, 305.0)


if __name__ == "__main__":
    unittest.main()
