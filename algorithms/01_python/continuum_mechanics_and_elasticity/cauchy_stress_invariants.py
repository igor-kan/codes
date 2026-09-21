"""Cauchy Stress Tensor Invariants and Stress Deviator.

Reference: Landau & Lifshitz Vol 7 (Theory of Elasticity).
Calculates principal stresses (eigenvalues), stress invariants (I1, I2, I3),
deviatoric stress tensor s_ij, and J2, J3 invariants.
"""
import numpy as np
from typing import Dict, Tuple


def stress_invariants(sigma: np.ndarray) -> Dict[str, float]:
    """Calculate principal invariants of 3x3 symmetric stress tensor sigma."""
    if sigma.shape != (3, 3):
        raise ValueError("Stress tensor must be 3x3")
    
    I1 = float(np.trace(sigma))
    I2 = 0.5 * (I1**2 - float(np.trace(sigma @ sigma)))
    I3 = float(np.linalg.det(sigma))
    return {"I1": I1, "I2": I2, "I3": I3}


def principal_stresses(sigma: np.ndarray) -> Tuple[float, float, float]:
    """Calculate ordered principal stresses sigma_1 >= sigma_2 >= sigma_3."""
    eigvals = np.linalg.eigvalsh(sigma)
    return float(eigvals[2]), float(eigvals[1]), float(eigvals[0])


def deviatoric_stress(sigma: np.ndarray) -> Tuple[np.ndarray, float, float]:
    """Calculate deviatoric stress tensor s = sigma - (1/3)*tr(sigma)*I, and J2, J3."""
    I1 = np.trace(sigma)
    s = sigma - (I1 / 3.0) * np.eye(3)
    J2 = 0.5 * float(np.trace(s @ s))
    J3 = float(np.linalg.det(s))
    return s, J2, J3
