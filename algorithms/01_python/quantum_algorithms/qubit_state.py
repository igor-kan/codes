"""Single Qubit State Representation and Bloch Sphere Coordinates.

Implements pure state |psi> = alpha |0> + beta |1> and Bloch vector (u, v, w).
"""

from typing import Tuple, Sequence
import numpy as np


class QubitState:
    """Pure single-qubit quantum state."""

    def __init__(self, alpha: complex, beta: complex):
        norm = np.sqrt(abs(alpha)**2 + abs(beta)**2)
        if norm < 1e-12:
            raise ValueError("State vector cannot have zero norm")
        self.alpha = complex(alpha / norm)
        self.beta = complex(beta / norm)

    @property
    def vector(self) -> np.ndarray:
        """Statevector in computational basis [alpha, beta]^T."""
        return np.array([self.alpha, self.beta], dtype=np.complex128)

    @property
    def bloch_vector(self) -> Tuple[float, float, float]:
        """Bloch coordinates: (u, v, w) = (2 Re(alpha* beta), 2 Im(alpha* beta), |alpha|^2 - |beta|^2)."""
        u = float(2.0 * np.real(np.conj(self.alpha) * self.beta))
        v = float(2.0 * np.imag(np.conj(self.alpha) * self.beta))
        w = float(abs(self.alpha)**2 - abs(self.beta)**2)
        return u, v, w

    def measurement_probabilities(self) -> Tuple[float, float]:
        """Born rule: P(0) = |alpha|^2, P(1) = |beta|^2."""
        p0 = float(abs(self.alpha)**2)
        p1 = float(abs(self.beta)**2)
        return p0, p1
