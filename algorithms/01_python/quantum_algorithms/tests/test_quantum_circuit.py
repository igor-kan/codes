"""Unit tests for Quantum Circuit Simulator."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_circuit import QuantumCircuit
from quantum_gates import QuantumGates


class TestQuantumCircuit(unittest.TestCase):
    def test_bell_state_generation(self):
        # Create |Phi+> = 1/sqrt(2) (|00> + |11>) via H(0) then CNOT(0, 1)
        qc = QuantumCircuit(2)
        qc.apply_single_gate(QuantumGates.H, target_qubit=0)
        qc.apply_cnot(control=0, target=1)

        probs = qc.probabilities()
        self.assertAlmostEqual(probs[0], 0.5)
        self.assertAlmostEqual(probs[1], 0.0)
        self.assertAlmostEqual(probs[2], 0.0)
        self.assertAlmostEqual(probs[3], 0.5)


if __name__ == "__main__":
    unittest.main()
