"""
Rayleigh-Plesset Equation for Cavitation Bubble Dynamics.
Reference: Zeldovich; Batchelor.
"""
import numpy as np

def bubble_radial_acceleration(R: float, R_dot: float, P_bubble: float, P_inf: float, rho: float) -> float:
    """
    R d^2 R / dt^2 + 3/2 (dR/dt)^2 = (P_bubble - P_inf) / rho.
    """
    term1 = (P_bubble - P_inf) / rho
    term2 = 1.5 * (R_dot**2)
    return float((term1 - term2) / R)
