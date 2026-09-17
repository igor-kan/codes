"""Unit tests for Collisionless Shock."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from collisionless_shock_rankine import CollisionlessShock


class TestCollisionlessShock(unittest.TestCase):
    def test_compression_limit(self):
        # For gamma = 5/3 (monoatomic plasma): r_max = (8/3)/(2/3) = 4.0
        r_max = CollisionlessShock.max_compression_ratio(polytropic_gamma=5.0 / 3.0)
        self.assertAlmostEqual(r_max, 4.0)


if __name__ == "__main__":
    unittest.main()
