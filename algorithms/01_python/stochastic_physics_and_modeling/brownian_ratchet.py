"""
Flashing Brownian Ratchet and Directed Thermal Transport.
References: Gershenfeld - The Nature of Mathematical Modeling.
"""
import numpy as np

def sawtooth_force(x: float, L: float = 1.0, alpha: float = 0.2, F0: float = 1.0) -> float:
    """Asymmetric sawtooth ratchet potential force."""
    mod_x = x % L
    if mod_x < alpha * L:
        return -F0 / alpha
    else:
        return F0 / (1.0 - alpha)
