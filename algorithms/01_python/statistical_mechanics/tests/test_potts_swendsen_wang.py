"""Unit tests for Potts Swendsen-Wang."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from potts_swendsen_wang import PottsSwendsenWang


class TestPotts(unittest.TestCase):
    def test_states_within_bounds(self):
        potts = PottsSwendsenWang(size=6, q_states=4, temperature=1.5)
        potts.step()
        self.assertTrue(bool(np.all(potts.spins >= 0)))
        self.assertTrue(bool(np.all(potts.spins < 4)))


if __name__ == "__main__":
    unittest.main()
