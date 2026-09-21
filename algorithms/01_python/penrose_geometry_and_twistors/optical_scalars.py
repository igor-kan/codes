"""
Sachs Optical Scalars for null geodesic congruences: Expansion, Shear, Twist.
Reference: Penrose, The Road to Reality, Ch. 22; Sachs (1961).
"""
import numpy as np
from typing import Dict

def compute_optical_scalars(grad_k: np.ndarray, complex_screen_basis: np.ndarray) -> Dict[str, float]:
    """
    Given space-time gradient nabla_b k_a of a null vector field k^a,
    and a complex 2D spatial screen basis m^a (with m_a bar{m}^a = 1, m_a m^a = 0):
    - Expansion theta = (1/2) Re(grad_k : screen)
    - Shear sigma = grad_k_{ab} m^a m^b
    - Twist (vorticity) omega = (1/2) Im(grad_k : screen)
    """
    m = complex_screen_basis
    m_bar = np.conj(m)
    
    # Project to screen
    rho = -np.einsum('ab,a,b', grad_k, m_bar, m)
    sigma = -np.einsum('ab,a,b', grad_k, m_bar, m_bar)
    
    theta = rho.real
    omega = rho.imag
    shear_mag = abs(sigma)
    
    return {
        "expansion": float(theta),
        "twist": float(omega),
        "shear_magnitude": float(shear_mag)
    }
