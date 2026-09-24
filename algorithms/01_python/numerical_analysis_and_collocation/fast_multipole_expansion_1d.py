"""1D Multipole Potential Expansion for N-Body Gravitational and Coulomb Fields."""
import numpy as np


def multipole_moments_1d(charges: np.ndarray, positions: np.ndarray, center: float, p_order: int) -> np.ndarray:
    """Compute multipole expansion moments Q_l = sum q_i * (x_i - x_0)^l."""
    moments = np.zeros(p_order + 1)
    r = positions - center
    for l in range(p_order + 1):
        moments[l] = np.sum(charges * (r**l))
    return moments
