"""Melnikov Method for Transverse Homoclinic Intersection and Chaos.

Calculates the distance between stable and unstable manifolds under periodic perturbation:
M(t_0) = int_(-inf)^inf {H_0, H_1}(q_0(t-t_0), p_0(t-t_0)) dt.
If M(t_0) has simple zeros, homoclinic chaos occurs (Smale horseshoe).
"""
import numpy as np
from scipy import integrate


def duffing_melnikov_function(t0: float, gamma: float, delta: float, omega: float) -> float:
    """Melnikov integral for periodically forced, damped Duffing oscillator.

    M(t0) = -4/3 * delta + sqrt(2) * pi * gamma * omega * sech(pi * omega / 2) * sin(omega * t0).
    """
    prefactor = np.sqrt(2.0) * np.pi * gamma * omega / np.cosh(0.5 * np.pi * omega)
    return float(- (4.0 / 3.0) * delta + prefactor * np.sin(omega * t0))


def is_melnikov_chaotic(gamma: float, delta: float, omega: float) -> bool:
    """Check if oscillation amplitude gamma exceeds threshold for transversal manifold crossing."""
    prefactor = np.sqrt(2.0) * np.pi * gamma * omega / np.cosh(0.5 * np.pi * omega)
    return bool(prefactor > (4.0 / 3.0) * delta)
