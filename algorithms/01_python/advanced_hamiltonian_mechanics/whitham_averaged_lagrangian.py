"""
Whitham Modulation Theory and Wave Action Conservation.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def linear_wave_averaged_lagrangian(omega: float, k: float, a: float, c: float = 1.0) -> float:
    """Averaged Lagrangian L_bar(omega, k, a) = 0.5 a^2 (omega^2 - c^2 k^2)."""
    return 0.5 * (a**2) * (omega**2 - (c * k)**2)

def wave_action_density(omega: float, a: float) -> float:
    """Action density J = dL_bar / domega = omega a^2."""
    return omega * (a**2)
