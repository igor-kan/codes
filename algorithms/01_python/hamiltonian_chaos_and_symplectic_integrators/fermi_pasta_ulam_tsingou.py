"""Fermi-Pasta-Ulam-Tsingou (FPUT) Nonlinear Lattice Recurrence.

FPUT alpha-model: m * d^2(q_i)/dt^2 = (q_(i+1) - 2*q_i + q_(i-1)) + alpha * [(q_(i+1) - q_i)^2 - (q_i - q_(i-1))^2].
Normal mode energy spectrum E_k(t) exhibits quasi-periodic recurrence rather than thermal equipartition.
"""
import numpy as np
from typing import Tuple


def fput_forces(q: np.ndarray, alpha: float) -> np.ndarray:
    """Forces on 1D FPUT lattice with fixed boundary conditions q_0 = q_(N+1) = 0."""
    n = len(q)
    f = np.zeros(n)
    
    # Extended coordinates with boundaries
    q_ext = np.zeros(n + 2)
    q_ext[1:-1] = q

    for i in range(1, n + 1):
        d_right = q_ext[i + 1] - q_ext[i]
        d_left = q_ext[i] - q_ext[i - 1]
        f[i - 1] = (d_right - d_left) + alpha * (d_right**2 - d_left**2)
        
    return f


def normal_mode_energies(q: np.ndarray, p: np.ndarray) -> np.ndarray:
    """Calculate harmonic mode energies E_k via discrete sine transform."""
    n = len(q)
    modes = np.arange(1, n + 1)
    
    # Discrete sine transform basis
    # Q_k = sqrt(2 / (N + 1)) * sum_j q_j * sin(j * k * pi / (N + 1))
    j_idx = np.arange(1, n + 1)
    sin_mat = np.sin(np.outer(j_idx, modes) * np.pi / (n + 1)) * np.sqrt(2.0 / (n + 1))
    
    Q = q @ sin_mat
    P = p @ sin_mat
    omega_k = 2.0 * np.sin(modes * np.pi / (2.0 * (n + 1)))
    
    return 0.5 * (P**2 + (omega_k**2) * (Q**2))
