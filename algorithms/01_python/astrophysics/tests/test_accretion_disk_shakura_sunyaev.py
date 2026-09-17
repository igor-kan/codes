"""Unit tests for Shakura-Sunyaev disk."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from accretion_disk_shakura_sunyaev import ShakuraSunyaevDisk


class TestShakuraSunyaev(unittest.TestCase):
    def test_temperature_profile(self):
        t = ShakuraSunyaevDisk.temperature_profile(radius_m=1e8, mass_kg=2e30, m_dot_kg_s=1e15, r_in_m=1e7)
        self.assertTrue(t > 0)
        t_in = ShakuraSunyaevDisk.temperature_profile(radius_m=1e6, mass_kg=2e30, m_dot_kg_s=1e15, r_in_m=1e7)
        self.assertEqual(t_in, 0.0)


if __name__ == "__main__":
    unittest.main()
