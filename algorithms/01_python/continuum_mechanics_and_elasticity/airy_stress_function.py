"""Airy Stress Function Formulation for 2D Elastostatics.

Biharmonic equation: div^4(Phi) = 0.
Stress components: sigma_xx = d^2(Phi)/dy^2, sigma_yy = d^2(Phi)/dx^2, sigma_xy = -d^2(Phi)/dxdy.
Example: Cantilever beam with end load P.
"""
import numpy as np
from typing import Dict


def cantilever_end_load_stresses(P: float, L: float, c: float, b: float, x: float, y: float) -> Dict[str, float]:
    """Stresses in cantilever beam [-c, c] depth, width b, length L loaded by end shear P.

    Moment of inertia I = 2 * b * c^3 / 3.
    """
    I = 2.0 * b * (c**3) / 3.0
    sigma_xx = -P * (L - x) * y / I
    sigma_yy = 0.0
    sigma_xy = -P * (c**2 - y**2) / (2.0 * I)
    return {"sigma_xx": float(sigma_xx), "sigma_yy": float(sigma_yy), "sigma_xy": float(sigma_xy)}
