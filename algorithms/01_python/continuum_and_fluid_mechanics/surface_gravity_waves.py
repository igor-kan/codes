"""
Airy Linear Surface Gravity Wave Dispersion.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6, Ch. 8).
"""
import numpy as np

def surface_wave_dispersion(k: float, h: float, g: float = 9.81) -> float:
    """Wave angular frequency omega^2 = g k tanh(k h)."""
    return float(np.sqrt(g * k * np.tanh(k * h)))

def phase_and_group_velocity(k: float, h: float, g: float = 9.81):
    """Phase speed c_p = omega / k, group speed c_g = d(omega)/dk = 0.5 c_p (1 + 2 k h / sinh(2 k h))."""
    omega = surface_wave_dispersion(k, h, g)
    c_p = omega / k
    kh2 = 2.0 * k * h
    c_g = 0.5 * c_p * (1.0 + kh2 / np.sinh(kh2))
    return float(c_p), float(c_g)
