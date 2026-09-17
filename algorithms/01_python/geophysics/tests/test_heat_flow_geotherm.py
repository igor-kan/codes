"""Unit tests for continental geotherm."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from heat_flow_geotherm import ContinentalGeotherm


class TestGeotherm(unittest.TestCase):
    def test_temperature_gradient(self):
        t10km = ContinentalGeotherm.temperature(10000.0, surface_temp_t0=15.0)
        self.assertTrue(t10km > 15.0)


if __name__ == "__main__":
    unittest.main()
