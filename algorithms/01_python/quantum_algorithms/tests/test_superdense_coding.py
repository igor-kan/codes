"""Unit tests for Superdense Coding."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from superdense_coding import SuperdenseCoding


class TestSuperdenseCoding(unittest.TestCase):
    def test_all_bit_pairs(self):
        for b1 in (0, 1):
            for b2 in (0, 1):
                rec1, rec2 = SuperdenseCoding.encode_and_decode(b1, b2)
                self.assertEqual((rec1, rec2), (b1, b2))


if __name__ == "__main__":
    unittest.main()
