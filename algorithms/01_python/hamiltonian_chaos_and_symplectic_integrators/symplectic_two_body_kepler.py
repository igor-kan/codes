"""Symplectic Integration of Gravitational Kepler Orbit.

Exact preservation of Angular Momentum L = q x p and Laplace-Runge-Lenz vector:
A = p x L - G * M * m * (q / ||q||).
"""
import numpy as np
from typing import Tuple
from yoshida_fourth_order import yoshida4_step

GM = 1.0  # Gravitational parameter in normalized units


def kepler_force(q: np.ndarray) -> np.ndarray:
    """Newtonian gravitational force F = -GM * q / ||q||^3."""
    r = np.linalg.norm(q)
    return -GM * q / (r**3)


def angular_momentum_2d(q: np.ndarray, p: np.ndarray) -> float:
    """L_z = q_x * p_y - q_y * p_x."""
    return float(q[0] * p[1] - q[1] * p[0])


def runge_lenz_vector_2d(q: np.ndarray, p: np.ndarray) -> np.ndarray:
    """Laplace-Runge-Lenz vector A in 2D."""
    Lz = angular_momentum_2d(q, p)
    # p x (Lz k) = (py Lz, -px Lz)
    p_cross_L = np.array([p[1] * Lz, -p[0] * Lz])
    r = np.linalg.norm(q)
    return p_cross_L - GM * (q / r)
