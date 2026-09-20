"""
Poynting Vector and Maxwell Stress Tensor.
References: Landau & Lifshitz - The Classical Theory of Fields.
"""
import numpy as np

def poynting_vector(E: np.ndarray, B: np.ndarray, mu0: float = 1.0) -> np.ndarray:
    """Poynting flux S = (E x B) / mu0."""
    return np.cross(E, B) / mu0

def maxwell_stress_tensor(E: np.ndarray, B: np.ndarray, eps0: float = 1.0, mu0: float = 1.0) -> np.ndarray:
    """Maxwell stress tensor T_ij = eps0 (E_i E_j - 0.5 delta_ij E^2) + (1/mu0) (B_i B_j - 0.5 delta_ij B^2)."""
    E2 = np.dot(E, E)
    B2 = np.dot(B, B)
    T = eps0 * (np.outer(E, E) - 0.5 * E2 * np.eye(3)) + (1.0 / mu0) * (np.outer(B, B) - 0.5 * B2 * np.eye(3))
    return T
