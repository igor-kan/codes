"""Unit tests for Quantum Gates."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_gates import QuantumGates


class TestQuantumGates(unittest.TestCase):
    def test_unitarity(self):
        for gate in [QuantumGates.X, QuantumGates.Y, QuantumGates.Z, QuantumGates.H, QuantumGates.CNOT, QuantumGates.SWAP]:
            self.assertTrue(QuantumGates.is_unitary(gate))

    def test_hadamard_pauli_conjugation(self):
        # H X H = Z, H Z H = X
        h, x, z = QuantumGates.H, QuantumGates.X, QuantumGates.Z
        np.testing.assert_allclose(h @ x @ h, z, atol=1e-12)
        np.testing.assert_allclose(h @ z @ h, x, atol=1e-12)


if __name__ == "__main__":
    unittest.main()
