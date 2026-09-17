"""Unit tests for Quantum Fourier Transform."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_fourier_transform import QuantumFourierTransform


class TestQuantumFourierTransform(unittest.TestCase):
    def test_qft_unitary(self):
        qft = QuantumFourierTransform.matrix(num_qubits=3)
        np.testing.assert_allclose(qft @ qft.conj().T, np.eye(8), atol=1e-12)

    def test_qft_single_qubit_is_hadamard(self):
        # For n=1 qubit, QFT is exactly the Hadamard gate
        qft1 = QuantumFourierTransform.matrix(num_qubits=1)
        h = (1.0 / np.sqrt(2.0)) * np.array([[1.0, 1.0], [1.0, -1.0]])
        np.testing.assert_allclose(qft1, h, atol=1e-12)


if __name__ == "__main__":
    unittest.main()
