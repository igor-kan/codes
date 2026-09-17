"""Unit tests for Jeans instability."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from jeans_instability_collapse import JeansInstability


class TestJeans(unittest.TestCase):
    def test_sound_speed_and_freefall(self):
        cs = JeansInstability.sound_speed(10.0, mu=2.0)
        self.assertTrue(cs > 0)
        t_ff = JeansInstability.free_fall_time(1e-18)
        self.assertTrue(t_ff > 0)


if __name__ == "__main__":
    unittest.main()
