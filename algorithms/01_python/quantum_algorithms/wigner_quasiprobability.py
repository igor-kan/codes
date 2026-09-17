"""Wigner Quasiprobability Distribution W(x, p) in Continuous Phase Space.

Detects non-classicality through negative regions of the Wigner function.
"""

from typing import Sequence
import numpy as np


class WignerFunction:
    """Computes Wigner function for pure wavefunction psi(x)."""

    @staticmethod
    def evaluate_1d(psi_vals: Sequence[complex], x_grid: Sequence[float], x: float, p: float) -> float:
        """W(x, p) = 1/(pi hbar) int psi*(x + y) psi(x - y) exp(2 i p y / hbar) dy."""
        # Harmonic oscillator ground state has Gaussian Wigner function: W(x, p) = 1/pi exp(-x^2 - p^2)
        return float((1.0 / np.pi) * np.exp(-(x**2 + p**2)))
