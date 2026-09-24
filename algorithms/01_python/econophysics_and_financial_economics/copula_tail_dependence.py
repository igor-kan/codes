"""Clayton and Gumbel Archimedean Copulas for Non-linear Tail Dependence.

Clayton: Lower tail dependence lambda_L = 2^(-1 / theta).
Gumbel: Upper tail dependence lambda_U = 2 - 2^(1 / theta).
"""
import numpy as np


def clayton_copula_cdf(u: np.ndarray, v: np.ndarray, theta: float) -> np.ndarray:
    """Clayton copula joint CDF: C(u, v) = (u^(-theta) + v^(-theta) - 1)^(-1 / theta)."""
    if theta <= 0:
        raise ValueError("Theta must be > 0 for positive lower tail dependence")
    return (u**(-theta) + v**(-theta) - 1.0)**(-1.0 / theta)


def clayton_lower_tail_dependence(theta: float) -> float:
    """lambda_L = 2^(-1 / theta)."""
    return float(2.0**(-1.0 / theta))
