"""Helmholtz Green's Function in 2D Free Space: G(r) = (i/4) * H_0^(1)(k r)."""
import numpy as np
from scipy.special import hankel1


def helmholtz_2d_green_function(r: np.ndarray, k: float) -> np.ndarray:
    """Evaluate outgoing 2D Helmholtz Green function."""
    return 0.25j * hankel1(0, k * r)
