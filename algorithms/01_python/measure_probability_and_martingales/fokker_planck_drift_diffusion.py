"""
Fokker-Planck Equation 1D Numerical Finite-Difference Solver.
Reference: Evans & Rosenthal; Risken, The Fokker-Planck Equation.
"""
import numpy as np

def step_fokker_planck(p: np.ndarray, dx: float, dt: float, mu: float, D: float) -> np.ndarray:
    """
    d p / dt = - mu d p / dx + D d^2 p / dx^2.
    """
    dp_dx = (np.roll(p, -1) - np.roll(p, 1)) / (2.0 * dx)
    d2p_dx2 = (np.roll(p, -1) - 2.0 * p + np.roll(p, 1)) / (dx**2)
    p_next = p + dt * (-mu * dp_dx + D * d2p_dx2)
    # Enforce positivity and normalize
    p_next = np.maximum(p_next, 0.0)
    p_next /= np.sum(p_next * dx)
    return p_next
