"""
Gauss Hypergeometric 2F1 and Confluent Hypergeometric 1F1 Series.
References: Arfken, Weber, Harris - Mathematical Methods for Physicists (Ch. 18).
"""
import numpy as np

def hyp2f1(a: float, b: float, c: float, z: complex, max_iter: int = 500, tol: float = 1e-14) -> complex:
    """Evaluate Gauss hypergeometric function 2F1(a, b; c; z) for |z| < 1."""
    if abs(z) >= 1.0:
        raise ValueError("|z| must be < 1 for direct power series convergence")
    term = 1.0 + 0.0j
    result = term
    for k in range(max_iter):
        factor = (a + k) * (b + k) / ((c + k) * (k + 1)) * z
        term *= factor
        result += term
        if abs(term) < tol * abs(result):
            break
    return result

def hyp1f1(a: float, b: float, z: complex, max_iter: int = 500, tol: float = 1e-14) -> complex:
    """Evaluate Confluent hypergeometric function 1F1(a; b; z) = M(a, b, z)."""
    term = 1.0 + 0.0j
    result = term
    for k in range(max_iter):
        factor = (a + k) / ((b + k) * (k + 1)) * z
        term *= factor
        result += term
        if abs(term) < tol * abs(result):
            break
    return result
