"""Unit tests for Microcanonical Entropy."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from microcanonical_entropy import MicrocanonicalEntropy


class TestMicrocanonicalEntropy(unittest.TestCase):
    def test_entropy_monotonicity(self):
        s1 = MicrocanonicalEntropy.entropy(100.0)
        s2 = MicrocanonicalEntropy.entropy(1000.0)
        self.assertGreater(s2, s1)


if __name__ == "__main__":
    unittest.main()
