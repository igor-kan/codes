"""Unit tests for Grad-Shafranov Operator."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from grad_shafranov_solver import GradShafranovOperator


class TestGradShafranov(unittest.TestCase):
    def test_operator_solovev_solution(self):
        # Constant psi should yield zero
        psi = np.full((5, 5), 10.0)
        val = GradShafranovOperator.delta_star_point(psi, r_val=2.0, dr=0.1, dz=0.1, i=2, j=2)
        self.assertAlmostEqual(val, 0.0)


if __name__ == "__main__":
    unittest.main()
