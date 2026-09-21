"""One-Loop Passarino-Veltman Tensor Integral Reduction.

Calculates scalar 1-point A_0(m^2) and 2-point B_0(p^2, m_1^2, m_2^2) integrals.
"""
import numpy as np
from scipy import integrate


def a0_scalar(m_sq: float, mu_sq: float = 1.0, eps: float = 1e-5) -> complex:
    """Evaluate scalar 1-point loop integral A_0(m^2) in dimensional regularization.

    A_0(m^2) = m^2 * [1/eps - gamma_E + 1 - ln(m^2 / mu^2)].
    """
    if m_sq <= 0:
        return 0.0j
    euler_mascheroni = 0.5772156649
    return m_sq * (1.0 / eps - euler_mascheroni + 1.0 - np.log(m_sq / mu_sq))


def b0_feynman_parametric(p_sq: float, m1_sq: float, m2_sq: float) -> float:
    """Finite part of Passarino-Veltman B_0(p^2, m_1^2, m_2^2) via Feynman parameter integration."""
    def integrand(x):
        # Delta = x * m1_sq + (1 - x) * m2_sq - x * (1 - x) * p_sq
        delta = x * m1_sq + (1.0 - x) * m2_sq - x * (1.0 - x) * p_sq
        if delta <= 0:
            return 0.0
        return -np.log(delta)
    
    val, _ = integrate.quad(integrand, 0.0, 1.0)
    return float(val)
