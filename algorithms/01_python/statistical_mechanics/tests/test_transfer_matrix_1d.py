"""Unit tests for Transfer Matrix 1D."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transfer_matrix_1d import TransferMatrix1D


class TestTransferMatrix(unittest.TestCase):
    def test_zero_field_eigenvalues(self):
        # For h=0, lambda_+ = 2 cosh(beta J), lambda_- = 2 sinh(beta J)
        tm = TransferMatrix1D(coupling_j=1.0, external_field_h=0.0, temperature=1.0)
        l_plus, l_minus = tm.eigenvalues()
        expected_plus = 2.0 * np.cosh(1.0)
        self.assertAlmostEqual(l_plus, expected_plus)


if __name__ == "__main__":
    unittest.main()
