"""Unit tests for Debye Solid."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from debye_solid_heat_capacity import DebyeSolid


class TestDebyeSolid(unittest.TestCase):
    def test_dulong_petit(self):
        limit = DebyeSolid.dulong_petit_limit(num_atoms=100)
        self.assertEqual(limit, 300.0)


if __name__ == "__main__":
    unittest.main()
