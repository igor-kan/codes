"""Unit tests for Electromagnetic Field Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from electromagnetic_field_tensor import ElectromagneticFieldTensor


class TestElectromagneticFieldTensor(unittest.TestCase):
    def test_lorentz_invariants(self):
        e = [0.0, 10.0, 0.0]
        b = [0.0, 0.0, 2.0]
        em = ElectromagneticFieldTensor(e, b, c=1.0)
        i1, i2 = em.lorentz_invariants()
        self.assertAlmostEqual(i1, -192.0)
        self.assertAlmostEqual(i2, 0.0)


if __name__ == "__main__":
    unittest.main()
