"""Unit tests for Bell CHSH Inequality."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bell_chsh_inequality import BellCHSHInequality


class TestBellCHSH(unittest.TestCase):
    def test_violation(self):
        s_quant = BellCHSHInequality.quantum_tsirelson_bound()
        s_class = BellCHSHInequality.classical_local_hidden_variable_bound()
        self.assertGreater(s_quant, s_class)
        self.assertAlmostEqual(s_quant, 2.0 * np.sqrt(2.0))


if __name__ == "__main__":
    unittest.main()
