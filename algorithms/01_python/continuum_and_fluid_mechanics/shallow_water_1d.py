"""
1D Nonlinear Shallow Water Equations (Saint-Venant Equations).
References: Landau & Lifshitz - Fluid Mechanics.
"""
import numpy as np

def shallow_water_step(h: np.ndarray, hu: np.ndarray, dx: float, dt: float, g: float = 9.81):
    """Lax-Friedrichs finite volume step for 1D shallow water system [h, h*u]."""
    u = hu / np.maximum(h, 1e-6)
    # Fluxes: F_h = h*u, F_hu = h*u^2 + 0.5*g*h^2
    f_h = hu
    f_hu = hu * u + 0.5 * g * h**2

    h_new = h.copy()
    hu_new = hu.copy()
    h_new[1:-1] = 0.5 * (h[2:] + h[:-2]) - 0.5 * (dt / dx) * (f_h[2:] - f_h[:-2])
    hu_new[1:-1] = 0.5 * (hu[2:] + hu[:-2]) - 0.5 * (dt / dx) * (f_hu[2:] - f_hu[:-2])
    return h_new, hu_new
