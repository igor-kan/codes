"""
Hagen-Poiseuille Viscous Laminar Flow in a Cylindrical Pipe.
Reference: Zeldovich, Higher Mathematics for Beginners.
"""
import numpy as np

def velocity_profile(r: np.ndarray, R_pipe: float, delta_P: float, L: float, eta: float) -> np.ndarray:
    """
    v(r) = (delta_P / (4 eta L)) * (R_pipe^2 - r^2).
    """
    return (delta_P / (4.0 * eta * L)) * (R_pipe**2 - r**2)

def volumetric_flow_rate(R_pipe: float, delta_P: float, L: float, eta: float) -> float:
    """
    Q = (pi delta_P R_pipe^4) / (8 eta L).
    """
    return float((np.pi * delta_P * (R_pipe**4)) / (8.0 * eta * L))
