"""Unit tests for Blasius Boundary Layer."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from blasius_boundary_layer import BlasiusBoundaryLayer


class TestBlasius(unittest.TestCase):
    def test_skin_friction_constant(self):
        fpp0 = BlasiusBoundaryLayer.wall_shear_parameter()
        self.assertAlmostEqual(fpp0, 0.332, places=3)


if __name__ == "__main__":
    unittest.main()
