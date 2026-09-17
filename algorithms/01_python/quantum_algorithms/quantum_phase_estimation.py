"""Quantum Phase Estimation (QPE) Algorithm.

Estimates eigenphase theta in U |psi> = exp(2 pi i theta) |psi> using QFT^dagger.
"""

from typing import Tuple
import numpy as np
try:
    from .quantum_fourier_transform import QuantumFourierTransform
except ImportError:
    from quantum_fourier_transform import QuantumFourierTransform


class QuantumPhaseEstimation:
    """Simulates quantum phase estimation."""

    @staticmethod
    def estimate_phase(eigenphase_theta: float, counting_qubits: int) -> float:
        """Simulate QPE measurement and return estimated phase."""
        num_states = 2**counting_qubits
        exact_index = eigenphase_theta * num_states
        measured_index = round(exact_index) % num_states
        return measured_index / num_states
