"""
Hénon-Heiles Hamiltonian and Poincaré Surface of Section.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def henon_heiles_hamiltonian(x: float, y: float, px: float, py: float) -> float:
    """H = 0.5 (px^2 + py^2 + x^2 + y^2) + x^2 y - y^3 / 3."""
    return 0.5 * (px**2 + py**2 + x**2 + y**2) + (x**2) * y - (y**3) / 3.0

def henon_heiles_derivs(state: np.ndarray) -> np.ndarray:
    """Equations of motion [x_dot, y_dot, px_dot, py_dot]."""
    x, y, px, py = state
    dx = px
    dy = py
    dpx = -x - 2.0 * x * y
    dpy = -y - x**2 + y**2
    return np.array([dx, dy, dpx, dpy])
