"""Unit tests for Omori law."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from omori_aftershock_law import OmoriLaw


class TestOmori(unittest.TestCase):
    def test_decay_rate(self):
        r1 = OmoriLaw.rate(t_days=1.0, k=100.0, c_days=0.1, p=1.0)
        r10 = OmoriLaw.rate(t_days=10.0, k=100.0, c_days=0.1, p=1.0)
        self.assertTrue(r1 > r10)


if __name__ == "__main__":
    unittest.main()
