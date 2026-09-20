"""
Point Vortex and Source Superposition in Incompressible Aerodynamics.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6, Ch. 1).
"""
import numpy as np

def point_vortex_velocity(gamma: float, r_vortex: np.ndarray, r_eval: np.ndarray) -> np.ndarray:
    """Induced 2D velocity from point vortex of strength gamma: v = Gamma / (2 pi r) (-sin theta, cos theta)."""
    dx = r_eval[0] - r_vortex[0]
    dy = r_eval[1] - r_vortex[1]
    r_sq = dx**2 + dy**2
    if r_sq < 1e-12:
        return np.zeros(2)
    factor = gamma / (2.0 * np.pi * r_sq)
    return np.array([-factor * dy, factor * dx])
