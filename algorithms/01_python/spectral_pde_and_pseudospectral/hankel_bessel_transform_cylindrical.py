"""Quasi-Discrete Hankel Transform (QDHT) with Zero-Order Bessel Functions."""
import numpy as np
from scipy.special import jn_zeros, j0


def bessel_j0_roots(N: int) -> np.ndarray:
    """Compute first N zeros of J_0(r)."""
    return jn_zeros(0, N)
