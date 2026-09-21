"""
Free-space Green's function for the 3D Helmholtz Equation (nabla^2 + k^2) G(r, r') = -delta(r - r').
Reference: Hassani, Mathematical Methods for Physics, Ch. 20; Blennow, Ch. 9.
"""
import numpy as np

def helmholtz_greens_function(r_vec: np.ndarray, r_prime_vec: np.ndarray, k: float) -> complex:
    """
    G(r, r') = exp(i k |r - r'|) / (4 pi |r - r'|).
    Outgoing radiating wave condition.
    """
    diff = np.linalg.norm(r_vec - r_prime_vec)
    if np.isclose(diff, 0.0):
        return complex(np.inf, np.inf)
    return np.exp(1j * k * diff) / (4.0 * np.pi * diff)
