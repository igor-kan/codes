"""5th-Order Weighted Essentially Non-Oscillatory (WENO5) Numerical Flux."""
import numpy as np


def weno5_weights(v1: float, v2: float, v3: float, v4: float, v5: float, eps: float = 1e-6) -> float:
    """Compute reconstructed left interface flux using Jiang-Shu smoothness indicators."""
    # Smoothness indicators beta_0, beta_1, beta_2
    b0 = (13.0 / 12.0) * (v1 - 2.0 * v2 + v3)**2 + 0.25 * (v1 - 4.0 * v2 + 3.0 * v3)**2
    b1 = (13.0 / 12.0) * (v2 - 2.0 * v3 + v4)**2 + 0.25 * (v2 - v4)**2
    b2 = (13.0 / 12.0) * (v3 - 2.0 * v4 + v5)**2 + 0.25 * (3.0 * v3 - 4.0 * v4 + v5)**2
    
    d0, d1, d2 = 0.1, 0.6, 0.3
    alpha0 = d0 / (eps + b0)**2
    alpha1 = d1 / (eps + b1)**2
    alpha2 = d2 / (eps + b2)**2
    alpha_sum = alpha0 + alpha1 + alpha2
    
    w0 = alpha0 / alpha_sum
    w1 = alpha1 / alpha_sum
    w2 = alpha2 / alpha_sum
    
    q0 = (2.0 * v1 - 7.0 * v2 + 11.0 * v3) / 6.0
    q1 = (-v2 + 5.0 * v3 + 2.0 * v4) / 6.0
    q2 = (2.0 * v3 + 5.0 * v4 - v5) / 6.0
    return float(w0 * q0 + w1 * q1 + w2 * q2)
