"""Unit tests for Bennett Pinch."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mhd_equilibrium_pinch import BennettPinch


class TestBennettPinch(unittest.TestCase):
    def test_current_positive(self):
        current = BennettPinch.bennett_current(linear_density_n=1e18, total_temp_kelvin=1e7)
        self.assertGreater(current, 1e4)


if __name__ == "__main__":
    unittest.main()
