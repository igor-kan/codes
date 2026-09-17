"""Unit tests for Van der Waerden Symbols."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from spinor_metric_van_der_waerden import VanDerWaerdenSymbols


class TestVanDerWaerdenSymbols(unittest.TestCase):
    def test_determinant_minkowski_norm(self):
        v = [5.0, 1.0, 2.0, 3.0]
        # v_0^2 - v_1^2 - v_2^2 - v_3^2 = 25 - (1 + 4 + 9) = 11
        # det(X) = (5 + 3)(5 - 3) - |1 - 2i|^2 = 16 - 5 = 11
        mat = VanDerWaerdenSymbols.vector_to_spinor(v)
        det_val = VanDerWaerdenSymbols.spinor_determinant(mat)
        self.assertAlmostEqual(det_val, 11.0)


if __name__ == "__main__":
    unittest.main()
