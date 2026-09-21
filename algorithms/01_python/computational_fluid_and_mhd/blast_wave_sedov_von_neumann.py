"""Sedov-von Neumann Self-Similar Strong Explosion Blast Wave.

Shock radius evolution: R(t) = xi_0 * (E * t^2 / rho_0)^(1/5).
Shock velocity: v_s = (2/5) * R / t.
Rankine-Hugoniot jump conditions for strong shock (Mach >> 1):
rho_shock = ((gamma + 1) / (gamma - 1)) * rho_0
P_shock = (2 / (gamma + 1)) * rho_0 * v_s^2.
"""
import numpy as np
from typing import Dict


def sedov_shock_radius(E_explosion: float, rho_ambient: float, t: float, gamma: float = 1.4) -> float:
    """Calculate blast wave shock radius R(t) at time t."""
    if t <= 0:
        raise ValueError("Time t must be positive")
    
    # xi_0 approx 1.033 for gamma = 1.4
    xi_0 = 1.033
    return float(xi_0 * ((E_explosion * (t**2)) / rho_ambient)**0.2)


def sedov_shock_front_properties(E_explosion: float, rho_ambient: float, t: float, gamma: float = 1.4) -> Dict[str, float]:
    """Calculate shock front position, speed, post-shock pressure, and density."""
    R = sedov_shock_radius(E_explosion, rho_ambient, t, gamma)
    v_s = 0.4 * R / t
    rho_shock = ((gamma + 1.0) / (gamma - 1.0)) * rho_ambient
    P_shock = (2.0 / (gamma + 1.0)) * rho_ambient * (v_s**2)

    return {"radius": R, "velocity": v_s, "density": rho_shock, "pressure": P_shock}
