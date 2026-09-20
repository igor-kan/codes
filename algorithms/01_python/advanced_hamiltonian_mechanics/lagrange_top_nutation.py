"""
Lagrange Symmetric Top Precession and Nutation.
References: Landau & Lifshitz - Mechanics (Vol. 1, Ch. 6).
"""
import numpy as np

def lagrange_top_effective_potential(theta: np.ndarray, P_phi: float, P_psi: float, I1: float = 1.0, I3: float = 1.0, Mgl: float = 1.0) -> np.ndarray:
    """Effective potential V_eff(theta) for symmetric top."""
    theta = np.asarray(theta, dtype=float)
    sin_sq = np.sin(theta)**2
    term1 = (P_phi - P_psi * np.cos(theta))**2 / (2.0 * I1 * np.maximum(sin_sq, 1e-8))
    term2 = (P_psi**2) / (2.0 * I3)
    term3 = Mgl * np.cos(theta)
    return term1 + term2 + term3
