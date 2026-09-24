"""KdV Soliton Split-Step Fourier Integrator: u_t + 6 u u_x + u_xxx = 0."""
import numpy as np


def kdv_soliton_profile(x: np.ndarray, c: float, x0: float = 0.0) -> np.ndarray:
    """Exact analytical single-soliton solution u(x) = 0.5 * c * sech^2(0.5 * sqrt(c) * (x - x0))."""
    return 0.5 * c * (1.0 / np.cosh(0.5 * np.sqrt(c) * (x - x0)))**2
