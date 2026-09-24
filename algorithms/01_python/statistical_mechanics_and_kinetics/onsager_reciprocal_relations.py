"""Onsager Reciprocal Relations and Thermoelectric Transport Matrix."""
import numpy as np


def verify_onsager_symmetry(L_transport: np.ndarray) -> bool:
    """Verify Onsager reciprocal symmetry L_ij = L_ji."""
    return bool(np.allclose(L_transport, L_transport.T))


def seebeck_coefficient(L11: float, L12: float, T: float) -> float:
    """Seebeck thermoelectric voltage coefficient S = - L12 / (T * L11)."""
    return float(-L12 / (T * L11))
