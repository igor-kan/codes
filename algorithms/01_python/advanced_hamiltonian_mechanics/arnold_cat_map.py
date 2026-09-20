"""
Arnold's Cat Map and Hyperbolic Toral Automorphism.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def arnold_cat_map(x: float, y: float, n_steps: int = 1) -> tuple:
    """Iterate Arnold's cat map on T^2: (x', y') = (2x + y, x + y) mod 1."""
    M = np.array([[2, 1], [1, 1]])
    pt = np.array([x % 1.0, y % 1.0])
    for _ in range(n_steps):
        pt = (M @ pt) % 1.0
    return float(pt[0]), float(pt[1])

def cat_map_lyapunov_exponent() -> float:
    """Maximal Lyapunov exponent: lambda = ln((3 + sqrt(5)) / 2) approx 0.96242365."""
    eigenvalue = (3.0 + np.sqrt(5.0)) / 2.0
    return float(np.log(eigenvalue))
