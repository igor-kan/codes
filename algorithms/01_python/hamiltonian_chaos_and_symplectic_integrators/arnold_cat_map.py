"""Arnold Cat Map Symplectic Automorphism on the 2-Torus.

M = [[1, 1], [1, 2]].
det(M) = 1 (symplectic / area-preserving).
Eigenvalues: lambda_1 = (3 + sqrt(5)) / 2 > 1 (hyperbolic expansion), lambda_2 = 1 / lambda_1.
Lyapunov exponent: lambda = ln(lambda_1) approx 0.9624.
"""
import numpy as np
from typing import Tuple


def arnold_cat_step(x: float, y: float) -> Tuple[float, float]:
    """Single Arnold cat map iteration on [0, 1) x [0, 1)."""
    x_next = (x + y) % 1.0
    y_next = (x + 2.0 * y) % 1.0
    return float(x_next), float(y_next)


def arnold_cat_lyapunov() -> float:
    """Exact maximal Lyapunov exponent of the Arnold Cat map."""
    eig_max = 0.5 * (3.0 + np.sqrt(5.0))
    return float(np.log(eig_max))
