"""
Analytical Velocity Profiles for Plane Poiseuille and Couette Flows.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6, Ch. 2).
"""
import numpy as np

def plane_poiseuille_velocity(y: np.ndarray, h: float, dp_dx: float, mu: float) -> np.ndarray:
    """Plane Poiseuille velocity u(y) = (1 / 2 mu) (-dp/dx) y (h - y) for y in [0, h]."""
    return (1.0 / (2.0 * mu)) * (-dp_dx) * y * (h - y)

def planar_couette_velocity(y: np.ndarray, h: float, u_top: float) -> np.ndarray:
    """Couette velocity profile between moving top plate and fixed bottom: u(y) = u_top * y / h."""
    return u_top * y / h
