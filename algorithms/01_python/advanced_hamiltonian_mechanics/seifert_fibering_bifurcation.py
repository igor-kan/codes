"""
Torus Mapping and Poincaré-Birkhoff Theorem.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def standard_twist_map(theta: float, r: float, k: float = 0.5) -> tuple:
    """Chirikov standard map: r_{n+1} = r_n + k sin(theta_n), theta_{n+1} = theta_n + r_{n+1} mod 2 pi."""
    r_new = r + k * np.sin(theta)
    theta_new = (theta + r_new) % (2.0 * np.pi)
    return float(theta_new), float(r_new)
