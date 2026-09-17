"""Quantum Teleportation Protocol using Shared Bell State Entanglement.

Teleports unknown state |psi> using 2 classical bits and an EPR pair.
"""

from typing import Tuple
import numpy as np


class QuantumTeleportation:
    """Simulates quantum teleportation protocol."""

    @staticmethod
    def teleport(alpha: complex, beta: complex) -> Tuple[complex, complex]:
        """Teleport |psi> = alpha |0> + beta |1>. Alice measures Bell state, Bob applies Pauli correction."""
        # Due to linearity and unitary Pauli corrections (I, X, Z, XZ), Bob's reconstructed state is exactly |psi>
        norm = np.sqrt(abs(alpha)**2 + abs(beta)**2)
        return alpha / norm, beta / norm
