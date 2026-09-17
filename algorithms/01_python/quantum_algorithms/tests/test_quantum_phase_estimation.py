"""Unit tests for Quantum Phase Estimation."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_phase_estimation import QuantumPhaseEstimation


class TestQuantumPhaseEstimation(unittest.TestCase):
    def test_phase_estimation_accuracy(self):
        theta = 0.375  # Exactly 3/8
        est = QuantumPhaseEstimation.estimate_phase(theta, counting_qubits=4)
        self.assertAlmostEqual(est, 0.375)


if __name__ == "__main__":
    unittest.main()
