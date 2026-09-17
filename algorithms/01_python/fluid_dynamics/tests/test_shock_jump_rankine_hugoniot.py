"""Unit tests for Rankine-Hugoniot Relations."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from shock_jump_rankine_hugoniot import RankineHugoniotShock


class TestRankineHugoniot(unittest.TestCase):
    def test_mach_1_acoustic_limit(self):
        shock = RankineHugoniotShock(gamma=1.4)
        m2 = shock.downstream_mach(m1=1.0)
        p_ratio = shock.pressure_ratio(m1=1.0)
        self.assertAlmostEqual(m2, 1.0)
        self.assertAlmostEqual(p_ratio, 1.0)


if __name__ == "__main__":
    unittest.main()
