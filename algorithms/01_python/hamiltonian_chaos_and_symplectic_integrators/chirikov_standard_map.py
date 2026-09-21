"""Chirikov Standard Map (Kicked Rotor Automorphism).

p_(n+1) = p_n + K * sin(theta_n) (mod 2*pi)
theta_(n+1) = theta_n + p_(n+1)   (mod 2*pi)

Greene's residue criterion: Last golden-mean KAM torus is destroyed at K_c approx 0.971635.
"""
import numpy as np
from typing import Tuple


def standard_map_step(theta: float, p: float, K: float) -> Tuple[float, float]:
    """Single iteration of the Chirikov standard map on cylinder/torus."""
    two_pi = 2.0 * np.pi
    p_next = (p + K * np.sin(theta)) % two_pi
    theta_next = (theta + p_next) % two_pi
    return float(theta_next), float(p_next)


def standard_map_orbit(theta0: float, p0: float, K: float, n_iterations: int) -> Tuple[np.ndarray, np.ndarray]:
    """Generate orbit of length n_iterations."""
    thetas = np.zeros(n_iterations)
    ps = np.zeros(n_iterations)
    
    th, p = theta0, p0
    for i in range(n_iterations):
        thetas[i] = th
        ps[i] = p
        th, p = standard_map_step(th, p, K)
        
    return thetas, ps
