"""
Jeans Mass and Jeans Length for Gravitational Instability.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 12).
"""
import numpy as np

def jeans_length(T: float, rho: float, mu: float = 2.3, G: float = 6.6743e-11) -> float:
    """Jeans length lambda_J = sqrt(pi k T / (G rho mu m_H))."""
    k = 1.380649e-23
    m_H = 1.6735575e-27
    c_s_sq = k * T / (mu * m_H)
    return float(np.sqrt(np.pi * c_s_sq / (G * rho)))

def jeans_mass(T: float, rho: float, mu: float = 2.3) -> float:
    """Jeans mass M_J = (4 pi / 3) rho (lambda_J / 2)^3."""
    lam_J = jeans_length(T, rho, mu)
    return float((4.0 * np.pi / 3.0) * rho * (0.5 * lam_J)**3)
