"""Hénon-Heiles Non-Integrable Hamiltonian and Poincaré Surface of Section.

H(x, y, px, py) = 0.5 * (px^2 + py^2) + 0.5 * (x^2 + y^2) + x^2 * y - (1/3) * y^3.
Transition from regular KAM tori (E < 1/12) to widespread chaos (E -> 1/6).
Equilibrium escape energy: E_esc = 1/6 approx 0.16667.
"""
import numpy as np
from typing import Tuple


def henon_heiles_hamiltonian(x: float, y: float, px: float, py: float) -> float:
    """Evaluate Hénon-Heiles energy."""
    return 0.5 * (px**2 + py**2) + 0.5 * (x**2 + y**2) + (x**2) * y - (1.0 / 3.0) * (y**3)


def henon_heiles_force(q: np.ndarray) -> np.ndarray:
    """Force F = -grad(V) where q = [x, y]."""
    x, y = q[0], q[1]
    fx = -x - 2.0 * x * y
    fy = -y - x**2 + y**2
    return np.array([fx, fy])


def px_from_energy(E: float, x: float, y: float, py: float) -> float:
    """Solve for px > 0 on Poincaré section x = 0 at specified energy E."""
    V = 0.5 * (x**2 + y**2) + (x**2) * y - (1.0 / 3.0) * (y**3)
    px_sq = 2.0 * (E - V) - py**2
    if px_sq < 0:
        raise ValueError("Kinetic energy px^2 is negative for these coordinates")
    return float(np.sqrt(px_sq))
