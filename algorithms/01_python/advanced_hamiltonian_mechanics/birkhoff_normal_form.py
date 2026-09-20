"""
Birkhoff Normal Form for 1-DOF Elliptic Fixed Point.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics (Ch. 10).
"""
import numpy as np

def harmonic_action(q: float, p: float, omega: float = 1.0) -> float:
    """Action variable I = (p^2 + omega^2 q^2) / (2 omega)."""
    return 0.5 * (p**2 + (omega**2) * q**2) / omega

def birkhoff_frequency_shift(I: float, omega0: float = 1.0, beta: float = 0.1) -> float:
    """Effective nonlinear frequency omega(I) = dH/dI = omega0 + beta * I."""
    return omega0 + beta * I
