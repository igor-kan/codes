"""Hartmann Flow of an Electrically Conducting Fluid Between Parallel Plates.

Under transverse magnetic field B_0 in y-direction, channel width 2d:
Hartmann number: Ha = B_0 * d * sqrt(sigma / mu).
Velocity profile: u(y) = u_0 * [cosh(Ha) - cosh(Ha * y / d)] / [cosh(Ha) - 1].
As Ha -> 0, recovers classical Poiseuille parabolic profile.
As Ha >> 1, flattens velocity profile into a central plug with thin Hartmann boundary layers.
"""
import numpy as np


def hartmann_number(B0: float, d: float, electrical_conductivity: float, dynamic_viscosity: float) -> float:
    """Calculate Hartmann dimensionless parameter Ha."""
    return float(B0 * d * np.sqrt(electrical_conductivity / dynamic_viscosity))


def hartmann_velocity_profile(y: np.ndarray, d: float, u0: float, Ha: float) -> np.ndarray:
    """Calculate velocity u(y) for y in [-d, d]."""
    if Ha < 1e-4:
        # Classical Poiseuille flow limit: u(y) = u0 * (1 - (y/d)^2)
        return u0 * (1.0 - (y / d)**2)
    
    cosh_Ha = np.cosh(Ha)
    return u0 * (cosh_Ha - np.cosh(Ha * y / d)) / (cosh_Ha - 1.0)
