"""Unit tests for Brownian First-Passage Time."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from brownian_first_passage_time import BrownianFirstPassage


class TestBrownianFirstPassage(unittest.TestCase):
    def test_density_positive(self):
        val = BrownianFirstPassage.density(t=1.0, barrier_distance=2.0, diffusion_coeff=1.0)
        self.assertGreater(val, 0.0)


if __name__ == "__main__":
    unittest.main()
