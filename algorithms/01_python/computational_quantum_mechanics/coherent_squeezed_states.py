"""
Coherent and Squeezed States in Fock Space.
References: Izaac & Wang - Computational Quantum Mechanics (Ch. 5).
"""
import numpy as np
from scipy.special import gammaln

def coherent_state_fock(alpha: complex, n_max: int = 30) -> np.ndarray:
    """Fock state expansion coefficients for coherent state |alpha>."""
    c = np.zeros(n_max, dtype=complex)
    alpha_mag = abs(alpha)
    alpha_phase = np.angle(alpha) if alpha != 0 else 0.0
    for n in range(n_max):
        # ln(c_n) = -0.5*|alpha|^2 + n*ln(|alpha|) - 0.5*ln(n!)
        if alpha_mag == 0:
            c[n] = 1.0 if n == 0 else 0.0
        else:
            ln_mag = -0.5 * (alpha_mag**2) + n * np.log(alpha_mag) - 0.5 * gammaln(n + 1)
            c[n] = np.exp(ln_mag) * np.exp(1j * n * alpha_phase)
    norm = np.linalg.norm(c)
    return c / norm if norm > 0 else c

def quadrature_variances(alpha: complex):
    """Quadrature variances for coherent state (Delta X1 = Delta X2 = 1/2)."""
    return 0.5, 0.5
