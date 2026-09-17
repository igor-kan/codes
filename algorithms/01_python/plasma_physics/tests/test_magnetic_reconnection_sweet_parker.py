"""Unit tests for Sweet-Parker Reconnection."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from magnetic_reconnection_sweet_parker import SweetParkerReconnection


class TestSweetParker(unittest.TestCase):
    def test_reconnection_rate_scaling(self):
        rate = SweetParkerReconnection.reconnection_rate(length_l=100.0, alfven_speed=100.0, magnetic_diffusivity_eta=1.0)
        # S = 10000 => 1/sqrt(S) = 0.01
        self.assertAlmostEqual(rate, 0.01)


if __name__ == "__main__":
    unittest.main()
