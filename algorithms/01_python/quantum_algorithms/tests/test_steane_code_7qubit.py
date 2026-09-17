"""Unit tests for Steane 7-Qubit Code."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from steane_code_7qubit import SteaneCode7Qubit


class TestSteaneCode(unittest.TestCase):
    def test_error_localization(self):
        # Error on qubit 5 (101 in binary) => syndrome = [1, 0, 1]
        loc = SteaneCode7Qubit.syndrome_to_error_location([1, 0, 1])
        self.assertEqual(loc, 5)


if __name__ == "__main__":
    unittest.main()
