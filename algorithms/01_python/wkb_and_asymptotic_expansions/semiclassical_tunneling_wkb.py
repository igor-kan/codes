"""Semiclassical WKB Exponential Barrier Penetration Gamow Factor."""
import numpy as np


def gamow_tunneling_factor(E: float, V0: float, width: float, mass: float = 1.0, hbar: float = 1.0) -> float:
    """T approx exp(-2 * int sqrt(2m(V - E)) / hbar dx)."""
    if E >= V0:
        return 1.0
    gamma = 2.0 * np.sqrt(2.0 * mass * (V0 - E)) * width / hbar
    return float(np.exp(-gamma))
