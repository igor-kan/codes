"""Sod Shock Tube Exact 1D Riemann Problem Initial Conditions."""
import numpy as np


def sod_initial_conditions(x: np.ndarray, x0: float = 0.5) -> tuple:
    """Standard Sod shock tube states (rho_L, P_L) = (1.0, 1.0) and (rho_R, P_R) = (0.125, 0.1)."""
    rho = np.where(x < x0, 1.0, 0.125)
    P = np.where(x < x0, 1.0, 0.1)
    u = np.zeros_like(x)
    return rho, u, P
