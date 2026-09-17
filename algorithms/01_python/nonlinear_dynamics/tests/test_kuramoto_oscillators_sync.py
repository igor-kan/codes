"""Unit tests for Kuramoto model."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kuramoto_oscillators_sync import KuramotoModel


class TestKuramoto(unittest.TestCase):
    def test_complete_synchronization(self):
        # All identical frequencies, strong coupling
        omega = np.ones(50) * 2.0
        model = KuramotoModel(natural_frequencies=omega, coupling_k=5.0)
        # Random initial phases
        theta = np.random.uniform(-np.pi, np.pi, 50)
        for _ in range(500):
            theta = model.step_rk4(theta, dt=0.02)
        r, _ = model.order_parameter(theta)
        self.assertTrue(r > 0.95)


if __name__ == "__main__":
    unittest.main()
