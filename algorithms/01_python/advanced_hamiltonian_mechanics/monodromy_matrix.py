"""
Monodromy Matrix and Floquet Multipliers for Periodic Orbits.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def harmonic_oscillator_monodromy(omega: float, T: float) -> np.ndarray:
    """Monodromy matrix M(T) for 1D harmonic oscillator: rotation by angle omega * T."""
    theta = omega * T
    return np.array([[np.cos(theta), np.sin(theta) / omega],
                     [-omega * np.sin(theta), np.cos(theta)]])
