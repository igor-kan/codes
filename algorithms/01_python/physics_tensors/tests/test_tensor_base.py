"""Unit tests for Tensor Base."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tensor_base import Tensor


class TestTensorBase(unittest.TestCase):
    def test_scalar_tensor(self):
        t = Tensor(42.0, valence=(0, 0), dim=4)
        self.assertEqual(t.rank, 0)
        self.assertEqual(t.data.item(), 42.0)

    def test_vector_tensor(self):
        v = Tensor([1.0, 2.0, 3.0, 4.0], valence=(1, 0), dim=4)
        self.assertEqual(v.rank, 1)
        self.assertEqual(v.p, 1)
        self.assertEqual(v.q, 0)

    def test_contraction(self):
        delta = Tensor(np.eye(3), valence=(1, 1), dim=3)
        tr = delta.contract(0, 0)
        self.assertEqual(tr.rank, 0)
        self.assertAlmostEqual(tr.data.item(), 3.0)

    def test_tensor_product(self):
        u = Tensor([1.0, 2.0], valence=(1, 0), dim=2)
        v = Tensor([3.0, 4.0], valence=(0, 1), dim=2)
        prod = u.tensor_product(v)
        self.assertEqual(prod.valence, (1, 1))
        expected = np.array([[3.0, 4.0], [6.0, 8.0]])
        np.testing.assert_allclose(prod.data, expected)


if __name__ == "__main__":
    unittest.main()
