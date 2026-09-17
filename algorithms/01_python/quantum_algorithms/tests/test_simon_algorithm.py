"""Unit tests for Simon's Algorithm."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from simon_algorithm import SimonAlgorithm


class TestSimonAlgorithm(unittest.TestCase):
    def test_solve_period(self):
        s_secret = 6  # 110 in binary
        # Collect linear equations orthogonal to s
        eqs = [y for y in range(8) if (bin(y & s_secret).count("1") % 2 == 0)]
        found_s = SimonAlgorithm.solve_linear_system_mod2(eqs, num_qubits=3)
        self.assertEqual(found_s, s_secret)


if __name__ == "__main__":
    unittest.main()
