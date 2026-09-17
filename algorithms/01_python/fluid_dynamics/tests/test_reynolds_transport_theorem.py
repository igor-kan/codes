"""Unit tests for Reynolds Transport."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from reynolds_transport_theorem import ReynoldsTransport


class TestReynoldsTransport(unittest.TestCase):
    def test_mass_flux(self):
        flux = ReynoldsTransport.mass_flux_rate(density=1000.0, normal_velocity=2.0, surface_area=0.5)
        self.assertAlmostEqual(flux, 1000.0)


if __name__ == "__main__":
    unittest.main()
