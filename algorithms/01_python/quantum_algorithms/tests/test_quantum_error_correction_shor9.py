"""Unit tests for Shor 9-Qubit Code."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_error_correction_shor9 import Shor9QubitCode


class TestShor9QubitCode(unittest.TestCase):
    def test_syndrome_detection(self):
        msg = Shor9QubitCode.detect_syndrome(3, "bit-flip")
        self.assertIn("qubit 3", msg)


if __name__ == "__main__":
    unittest.main()
