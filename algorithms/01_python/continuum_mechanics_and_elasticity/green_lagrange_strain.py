"""Nonlinear Green-Lagrange Strain and Infinitesimal Strain.

Deformation gradient: F_ij = delta_ij + du_i / dx_j
Green-Lagrange strain: E = 0.5 * (F^T F - I)
Infinitesimal strain: eps = 0.5 * (grad(u) + grad(u)^T)
"""
import numpy as np
from typing import Tuple


def deformation_gradient(grad_u: np.ndarray) -> np.ndarray:
    """F = I + grad(u)."""
    if grad_u.shape != (3, 3):
        raise ValueError("Displacement gradient must be 3x3")
    return np.eye(3) + grad_u


def green_lagrange_strain(grad_u: np.ndarray) -> np.ndarray:
    """E = 0.5 * (F^T F - I) = 0.5 * (grad_u + grad_u^T + grad_u^T @ grad_u)."""
    F = deformation_gradient(grad_u)
    return 0.5 * (F.T @ F - np.eye(3))


def infinitesimal_strain(grad_u: np.ndarray) -> np.ndarray:
    """Linearized strain tensor eps = 0.5 * (grad_u + grad_u^T)."""
    return 0.5 * (grad_u + grad_u.T)
