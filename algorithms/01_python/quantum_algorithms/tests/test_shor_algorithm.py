"""Unit tests for Shor's Algorithm."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from shor_algorithm import ShorAlgorithm


class TestShorAlgorithm(unittest.TestCase):
    def test_factor_15(self):
        p, q = ShorAlgorithm.factorize(15, seed_a=7)
        self.assertEqual(p * q, 15)
        self.assertIn(p, [3, 5])
        self.assertIn(q, [3, 5])


if __name__ == "__main__":
    unittest.main()
