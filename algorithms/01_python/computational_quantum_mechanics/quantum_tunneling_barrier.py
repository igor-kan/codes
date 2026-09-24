"""Quantum Tunneling Through a Finite Rectangular Potential Barrier.

Transmission coefficient T(E) for rectangular barrier of height V_0 and width a.
"""
import numpy as np


def barrier_transmission_coefficient(E: float, V0: float, a: float,
                                     mass: float = 1.0, hbar: float = 1.0) -> float:
    """Calculate quantum tunneling transmission probability T(E)."""
    if E <= 0 or V0 <= 0:
        raise ValueError("Energy and barrier height must be positive")
    if E < V0:
        k2 = np.sqrt(2.0 * mass * (V0 - E)) / hbar
        sinh_term = np.sinh(k2 * a)
        denom = 1.0 + (V0**2 * sinh_term**2) / (4.0 * E * (V0 - E))
        return float(1.0 / denom)
    elif np.isclose(E, V0):
        gamma = mass * (a**2) * V0 / (2.0 * hbar**2)
        return float(1.0 / (1.0 + gamma))
    else:
        k1 = np.sqrt(2.0 * mass * (E - V0)) / hbar
        sin_term = np.sin(k1 * a)
        denom = 1.0 + (V0**2 * sin_term**2) / (4.0 * E * (E - V0))
        return float(1.0 / denom)
