"""Multi-Qubit Quantum Circuit Simulator and Measurement Engine.

Simulates statevector evolution on 2^n dimensional Hilbert space.
"""

from typing import List, Tuple
import numpy as np
try:
    from .quantum_gates import QuantumGates
except ImportError:
    from quantum_gates import QuantumGates


class QuantumCircuit:
    """Quantum circuit simulator on n qubits."""

    def __init__(self, num_qubits: int):
        self.n = num_qubits
        self.dim = 2**num_qubits
        # Initialize in |00...0>
        self.state = np.zeros(self.dim, dtype=np.complex128)
        self.state[0] = 1.0

    def apply_single_gate(self, gate_2x2: np.ndarray, target_qubit: int):
        """Apply single-qubit gate to target_qubit using Kronecker products."""
        # Qubit 0 is most significant
        ops = []
        for i in range(self.n):
            ops.append(gate_2x2 if i == target_qubit else QuantumGates.I)
        full_gate = ops[0]
        for op in ops[1:]:
            full_gate = np.kron(full_gate, op)
        self.state = full_gate @ self.state

    def apply_cnot(self, control: int, target: int):
        """Apply CNOT between control and target qubits."""
        p0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=np.complex128)
        p1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=np.complex128)

        ops0 = [p0 if i == control else QuantumGates.I for i in range(self.n)]
        ops1 = [p1 if i == control else (QuantumGates.X if i == target else QuantumGates.I) for i in range(self.n)]

        term0 = ops0[0]
        term1 = ops1[0]
        for i in range(1, self.n):
            term0 = np.kron(term0, ops0[i])
            term1 = np.kron(term1, ops1[i])

        cnot_full = term0 + term1
        self.state = cnot_full @ self.state

    def probabilities(self) -> np.ndarray:
        """P(i) = |psi_i|^2."""
        return np.abs(self.state)**2
