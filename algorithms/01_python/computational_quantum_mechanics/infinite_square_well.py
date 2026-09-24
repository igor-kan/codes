"""Infinite Square Potential Well Analytical Solutions.

Energy eigenvalues: E_n = (n^2 * pi^2 * hbar^2) / (2 * m * L^2).
Stationary states: psi_n(x) = sqrt(2 / L) * sin(n * pi * x / L).
"""
import numpy as np


def well_energy_eigenvalue(n: int, L: float, hbar: float = 1.0, mass: float = 1.0) -> float:
    """Calculate exact energy of nth quantum state (n >= 1)."""
    if n < 1:
        raise ValueError("Principal quantum number n must be >= 1")
    return float((n**2 * np.pi**2 * hbar**2) / (2.0 * mass * L**2))


def well_eigenfunction(n: int, L: float, x: np.ndarray) -> np.ndarray:
    """Evaluate nth normalized spatial eigenfunction for x in [0, L]."""
    psi = np.sqrt(2.0 / L) * np.sin(n * np.pi * x / L)
    psi[x < 0] = 0.0
    psi[x > L] = 0.0
    return psi
