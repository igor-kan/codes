"""Unit tests for Hoshen-Kopelman Algorithm."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from percolation_hoshen_kopelman import HoshenKopelman2D


class TestHoshenKopelman(unittest.TestCase):
    def test_two_disconnected_islands(self):
        grid = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 1]
        ]
        labels = HoshenKopelman2D.label_clusters(grid)
        # Top-left cluster label should differ from bottom-right
        self.assertGreater(labels[0, 0], 0)
        self.assertGreater(labels[3, 3], 0)
        self.assertNotEqual(labels[0, 0], labels[3, 3])


if __name__ == "__main__":
    unittest.main()
