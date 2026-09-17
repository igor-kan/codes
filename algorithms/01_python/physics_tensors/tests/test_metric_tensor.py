"""Unit tests for Metric Tensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from metric_tensor import MetricTensor


class TestMetricTensor(unittest.TestCase):
    def test_euclidean_metric(self):
        g = MetricTensor(np.eye(3))
        self.assertEqual(g.dim, 3)
        self.assertEqual(g.signature, (3, 0))
        self.assertAlmostEqual(g.line_element([1.0, 2.0, 3.0]), 14.0)

    def test_minkowski_signature(self):
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        g = MetricTensor(eta)
        self.assertEqual(g.signature, (3, 1))
        self.assertGreater(g.line_element([0.0, 1.0, 0.0, 0.0]), 0)
        self.assertLess(g.line_element([1.0, 0.0, 0.0, 0.0]), 0)

    def test_index_raising_lowering(self):
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        g = MetricTensor(eta)
        v = [2.0, 3.0, 4.0, 5.0]
        v_low = g.lower_index(v)
        np.testing.assert_allclose(v_low, [-2.0, 3.0, 4.0, 5.0])
        v_raised = g.raise_index(v_low)
        np.testing.assert_allclose(v_raised, v)


if __name__ == "__main__":
    unittest.main()
