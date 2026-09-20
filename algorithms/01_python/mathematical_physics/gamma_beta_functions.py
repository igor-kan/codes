"""
Gamma & Beta Functions with Lanczos 7-term Approximation.
References: Press et al. - Numerical Recipes (Ch. 6).
"""
import numpy as np
import math

LANCZOS_G = 5.0
LANCZOS_COEFFS = [
    1.000000000190015,
    76.18009172947146,
    -86.50532032941677,
    24.01409824083091,
    -1.231739572450155,
    0.1208650973866179e-2,
    -0.5395239384953e-5
]

def log_gamma(z: float) -> float:
    """Compute ln(Gamma(z)) for z > 0 using Lanczos approximation."""
    if z <= 0:
        raise ValueError("z must be positive")
    x = z
    y = x
    tmp = x + 5.5
    tmp -= (x + 0.5) * np.log(tmp)
    ser = LANCZOS_COEFFS[0]
    for j in range(1, 7):
        y += 1.0
        ser += LANCZOS_COEFFS[j] / y
    return -tmp + np.log(2.5066282746310005 * ser / x)

def gamma_func(z: float) -> float:
    """Compute Gamma(z) for positive real numbers."""
    return np.exp(log_gamma(z))

def beta_func(x: float, y: float) -> float:
    """Compute Beta(x, y) = Gamma(x)Gamma(y)/Gamma(x+y)."""
    return np.exp(log_gamma(x) + log_gamma(y) - log_gamma(x + y))
