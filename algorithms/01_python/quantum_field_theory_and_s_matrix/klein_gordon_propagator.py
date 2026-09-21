"""Klein-Gordon Propagator for Spin-0 Scalar Fields.

Momentum space Feynman propagator: Delta_F(p) = 1 / (p^2 - m^2 + i*epsilon).
"""
import numpy as np
from feynman_slash import minkowski_dot


def scalar_propagator_momentum(p: np.ndarray, m: float, epsilon: float = 1e-6) -> complex:
    """Evaluate momentum space Feynman propagator Delta_F(p)."""
    p_sq = minkowski_dot(p, p)
    denom = p_sq - m**2 + 1j * epsilon
    return 1.0 / denom


def spacelike_propagator_decay(r: float, m: float) -> float:
    """Asymptotic behavior of Feynman scalar propagator at spacelike separations r > 0.

    Decays exponentially as exp(-m * r) / (r^(3/2)).
    """
    if r <= 0:
        raise ValueError("Distance r must be positive")
    return float(np.exp(-m * r) / (r**1.5))
