"""
Generalized Laguerre Polynomials L_n^(alpha)(x) and Hydrogenic Orbitals.
References: Arfken, Weber, Harris - Mathematical Methods for Physicists.
"""
import numpy as np
import math

def laguerre_l(n: int, alpha: float, x: np.ndarray) -> np.ndarray:
    """Evaluate generalized Laguerre polynomial L_n^(alpha)(x)."""
    x = np.asarray(x, dtype=float)
    if n == 0:
        return np.ones_like(x)
    if n == 1:
        return 1.0 + alpha - x
    
    l0 = np.ones_like(x)
    l1 = 1.0 + alpha - x
    for k in range(1, n):
        l2 = ((2 * k + 1 + alpha - x) * l1 - (k + alpha) * l0) / (k + 1)
        l0, l1 = l1, l2
    return l1

def hydrogenic_radial_wf(n: int, l: int, r: np.ndarray, a0: float = 1.0) -> np.ndarray:
    """Normalized radial wavefunction R_{nl}(r) for hydrogen atom in atomic units."""
    rho = 2.0 * r / (n * a0)
    norm = np.sqrt((2.0 / (n * a0))**3 * math.factorial(n - l - 1) / (2.0 * n * math.factorial(n + l)))
    lag = laguerre_l(n - l - 1, 2 * l + 1, rho)
    return norm * np.exp(-rho / 2.0) * (rho**l) * lag
