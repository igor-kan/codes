"""
Spherical Harmonics Y_l^m(theta, phi).
References: Arfken, Weber, Harris - Mathematical Methods for Physicists.
"""
import numpy as np
import math
from orthogonal_polynomials import associated_legendre_p

def spherical_harmonic(l: int, m: int, theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """Compute spherical harmonic Y_l^m(theta, phi)."""
    theta = np.asarray(theta, dtype=float)
    phi = np.asarray(phi, dtype=float)
    cos_t = np.cos(theta)
    
    # Normalization constant N_lm = sqrt((2l+1)/(4pi) * (l-m)!/(l+m)!)
    fact_ratio = math.factorial(l - abs(m)) / math.factorial(l + abs(m))
    norm = np.sqrt((2 * l + 1) / (4 * np.pi) * fact_ratio)
    
    p_lm = associated_legendre_p(l, abs(m), cos_t)
    
    if m >= 0:
        cood = norm * p_lm * np.exp(1j * m * phi)
    else:
        # Y_l^{-m} = (-1)^m Y_l^m*
        cood = (-1)**m * norm * p_lm * np.exp(1j * m * phi)
        
    return cood
