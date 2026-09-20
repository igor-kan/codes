"""
2D Lid-Driven Cavity Flow via Vorticity-Streamfunction Formulation.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6).
"""
import numpy as np

def compute_velocities_from_streamfunction(psi: np.ndarray, dx: float, dy: float):
    """Compute u = d(psi)/dy and v = -d(psi)/dx for grid psi[y_idx, x_idx]."""
    u = np.zeros_like(psi)
    v = np.zeros_like(psi)
    # y corresponds to axis 0 (rows), x corresponds to axis 1 (columns)
    u[1:-1, 1:-1] = (psi[2:, 1:-1] - psi[:-2, 1:-1]) / (2.0 * dy)
    v[1:-1, 1:-1] = -(psi[1:-1, 2:] - psi[1:-1, :-2]) / (2.0 * dx)
    return u, v
