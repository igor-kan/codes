"""Unit tests for Killing Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from killing_tensor import KillingTensor


class TestKillingTensor(unittest.TestCase):
    def test_metric_is_trivial_killing_tensor(self):
        # The metric tensor itself is always a Killing tensor: nabla_lambda g_{mu nu} = 0
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        kt = KillingTensor(eta)
        u = [1.0, 0.0, 0.0, 0.0]
        c = kt.conserved_quantity(u)
        self.assertAlmostEqual(c, -1.0)


if __name__ == "__main__":
    unittest.main()
