"""Unit tests for Bernstein-Vazirani Algorithm."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bernstein_vazirani import BernsteinVaziraniAlgorithm


class TestBernsteinVazirani(unittest.TestCase):
    def test_secret_recovery(self):
        s = 5  # 101 in binary, n=3
        f_oracle = lambda x: bin(x & s).count("1") % 2
        recovered = BernsteinVaziraniAlgorithm.recover_secret(f_oracle, num_qubits=3)
        self.assertEqual(recovered, "101")


if __name__ == "__main__":
    unittest.main()
