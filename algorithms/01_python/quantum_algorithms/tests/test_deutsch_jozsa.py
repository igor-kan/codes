"""Unit tests for Deutsch-Jozsa Algorithm."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from deutsch_jozsa import DeutschJozsaAlgorithm


class TestDeutschJozsa(unittest.TestCase):
    def test_constant_function(self):
        f_const = lambda x: 1
        res = DeutschJozsaAlgorithm.classify_function(f_const, num_qubits=3)
        self.assertEqual(res, "constant")

    def test_balanced_function(self):
        f_balanced = lambda x: x % 2
        res = DeutschJozsaAlgorithm.classify_function(f_balanced, num_qubits=3)
        self.assertEqual(res, "balanced")


if __name__ == "__main__":
    unittest.main()
