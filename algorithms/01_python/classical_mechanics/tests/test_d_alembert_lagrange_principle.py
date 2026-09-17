"""Unit tests for D'Alembert's Principle."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from d_alembert_lagrange_principle import DAlembertPrinciple


class TestDAlembertPrinciple(unittest.TestCase):
    def test_virtual_work_equilibrium(self):
        # Two equal and opposite forces in balance
        forces = [10.0, -10.0]
        # Equal rigid displacement delta r_1 = delta r_2
        disp = np.array([[1.0, 1.0], [-2.0, -2.0]])
        self.assertTrue(DAlembertPrinciple.verify_equilibrium(forces, disp))


if __name__ == "__main__":
    unittest.main()
