"""Mueller-Stokes Formalism for Partially Polarized Light.

Stokes vector: S = [I, Q, U, V]^T.
Degree of polarization: DOP = sqrt(Q^2 + U^2 + V^2) / I <= 1.
Mueller matrices for ideal linear polarizers, depolarizers, and retarders.
"""
import numpy as np
from typing import Tuple


def degree_of_polarization(stokes: np.ndarray) -> Tuple[float, float, float]:
    """Calculate Total DOP, Linear DOP (DOLP), and Circular DOP (DOCP)."""
    I, Q, U, V = stokes
    dop = np.sqrt(Q**2 + U**2 + V**2) / I
    dolp = np.sqrt(Q**2 + U**2) / I
    docp = abs(V) / I
    return float(dop), float(dolp), float(docp)


def ideal_depolarizer(fraction: float = 1.0) -> np.ndarray:
    """Mueller matrix for partial/total depolarizer."""
    ret = np.eye(4)
    ret[1, 1] = 1.0 - fraction
    ret[2, 2] = 1.0 - fraction
    ret[3, 3] = 1.0 - fraction
    return ret
