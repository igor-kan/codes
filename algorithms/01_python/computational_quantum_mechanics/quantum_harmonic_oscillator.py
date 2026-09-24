"""Quantum Harmonic Oscillator Hermite Eigenfunctions.

E_n = (n + 1/2) * hbar * omega.
psi_n(x) = (m*omega / (pi*hbar))^(1/4) * (1 / sqrt(2^n * n!)) * H_n(xi) * exp(-xi^2 / 2).
"""
import numpy as np
import math
from scipy.special import hermite


def qho_energy(n: int, omega: float, hbar: float = 1.0) -> float:
    """E_n = (n + 0.5) * hbar * omega."""
    return float((n + 0.5) * hbar * omega)


def qho_eigenfunction(n: int, x: np.ndarray, omega: float = 1.0, hbar: float = 1.0, mass: float = 1.0) -> np.ndarray:
    """Evaluate nth QHO eigenfunction."""
    alpha = np.sqrt(mass * omega / hbar)
    xi = alpha * x
    norm = (alpha / np.sqrt(np.pi))**0.5 / np.sqrt(2.0**n * math.factorial(n))
    H_n = hermite(n)
    return norm * H_n(xi) * np.exp(-0.5 * xi**2)
