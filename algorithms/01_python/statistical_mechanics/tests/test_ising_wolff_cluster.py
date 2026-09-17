"""Unit tests for Wolff Ising Algorithm."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ising_wolff_cluster import WolffIsing2D


class TestWolffIsing(unittest.TestCase):
    def test_cluster_growth(self):
        wolff = WolffIsing2D(size=8, temperature=2.269)
        c_size = wolff.cluster_step()
        self.assertGreaterEqual(c_size, 1)
        self.assertLessEqual(c_size, 64)


if __name__ == "__main__":
    unittest.main()
