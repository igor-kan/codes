"""1D Nonlinear Shallow Water (Saint-Venant) Riemann Solver.

Conserved variables: U = [h, h*u]^T.
Flux: F = [h*u, h*u^2 + 0.5 * g * h^2]^T.
Characteristic wave speeds: lambda_1 = u - sqrt(g * h), lambda_2 = u + sqrt(g * h).
Roe approximate Riemann solver flux calculation.
"""
import numpy as np
from typing import Tuple

G = 9.81


def shallow_water_flux(h: float, hu: float) -> Tuple[float, float]:
    """Physical flux vector for shallow water equations."""
    u = hu / h if h > 1e-6 else 0.0
    f1 = hu
    f2 = hu * u + 0.5 * G * (h**2)
    return float(f1), float(f2)


def roe_wave_speeds(h_L: float, u_L: float, h_R: float, u_R: float) -> Tuple[float, float]:
    """Roe averaged wave speeds for shallow water interface."""
    sqrt_hL = np.sqrt(max(1e-6, h_L))
    sqrt_hR = np.sqrt(max(1e-6, h_R))
    
    u_roe = (sqrt_hL * u_L + sqrt_hR * u_R) / (sqrt_hL + sqrt_hR)
    c_roe = np.sqrt(0.5 * G * (h_L + h_R))

    return float(u_roe - c_roe), float(u_roe + c_roe)
