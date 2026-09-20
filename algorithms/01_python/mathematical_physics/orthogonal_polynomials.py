"""
Orthogonal Polynomials: Legendre, Associated Legendre, Rodrigues representation.
References: Boas - Mathematical Methods in the Physical Sciences (Ch. 12).
"""
import numpy as np

def legendre_p(n: int, x: np.ndarray) -> np.ndarray:
    """Evaluate Legendre polynomial P_n(x) using Bonnet's recurrence."""
    x = np.asarray(x, dtype=float)
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return x.copy()
    
    p0 = np.ones_like(x)
    p1 = x.copy()
    for k in range(1, n):
        p2 = ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
        p0, p1 = p1, p2
    return p1

def associated_legendre_p(l: int, m: int, x: np.ndarray) -> np.ndarray:
    """Evaluate associated Legendre function P_l^m(x) for |x| <= 1."""
    x = np.asarray(x, dtype=float)
    if abs(m) > l:
        return np.zeros_like(x)
    
    # Negative m relation: P_l^{-m}(x) = (-1)^m (l-m)! / (l+m)! P_l^m(x)
    if m < 0:
        sign = (-1)**(-m)
        from math import factorial
        factor = factorial(l + m) / factorial(l - m)
        return sign * factor * associated_legendre_p(l, -m, x)

    # Compute P_m^m(x)
    pmm = np.ones_like(x)
    somx2 = np.sqrt(np.maximum(0.0, 1.0 - x**2))
    fact = 1.0
    for i in range(1, m + 1):
        pmm *= -fact * somx2
        fact += 2.0
        
    if l == m:
        return pmm
        
    # Compute P_{m+1}^m(x)
    pmmp1 = x * (2 * m + 1) * pmm
    if l == m + 1:
        return pmmp1
        
    # Recurrence to l
    p_ll = np.zeros_like(x)
    for ll in range(m + 2, l + 1):
        p_ll = (x * (2 * ll - 1) * pmmp1 - (ll + m - 1) * pmm) / (ll - m)
        pmm, pmmp1 = pmmp1, p_ll
    return p_ll
