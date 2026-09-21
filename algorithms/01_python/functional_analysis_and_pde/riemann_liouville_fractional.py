"""
Riemann-Liouville Fractional Integral and Derivative.
Reference: Hassani, Mathematical Methods for Physics; Podlubny, Fractional Differential Equations.
"""
import numpy as np
from scipy.special import gamma

def fractional_integral_rl(f_vals: np.ndarray, t: np.ndarray, alpha: float) -> np.ndarray:
    """
    Computes Riemann-Liouville fractional integral of order alpha > 0:
    I^alpha f(t) = (1 / Gamma(alpha)) int_0^t (t - tau)^{alpha - 1} f(tau) d tau.
    """
    n = len(t)
    out = np.zeros(n)
    dt = t[1] - t[0]
    g_alpha = gamma(alpha)
    
    for i in range(1, n):
        taus = t[:i+1]
        kernel = (t[i] - taus)**(alpha - 1.0)
        kernel[-1] = 0.0  # regularize endpoint
        integrand = kernel * f_vals[:i+1]
        out[i] = np.trapz(integrand, taus) / g_alpha
    return out
