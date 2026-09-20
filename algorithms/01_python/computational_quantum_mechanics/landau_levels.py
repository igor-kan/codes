"""
Landau Levels for 2D Electron in Magnetic Field.
References: Landau & Lifshitz - Quantum Mechanics (Vol. 3, Ch. 16).
"""
import numpy as np

def landau_level_energies(n_levels: int, B: float, m: float = 1.0, q: float = 1.0, hbar: float = 1.0) -> np.ndarray:
    """Landau level spectrum: E_n = hbar omega_c (n + 1/2) where omega_c = q B / m."""
    omega_c = q * B / m
    n = np.arange(n_levels)
    return hbar * omega_c * (n + 0.5)

def magnetic_length(B: float, q: float = 1.0, hbar: float = 1.0) -> float:
    """Magnetic length l_B = sqrt(hbar / (q B))."""
    return float(np.sqrt(hbar / (q * B)))
