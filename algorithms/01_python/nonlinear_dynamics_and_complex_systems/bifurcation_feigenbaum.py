"""
Bifurcation Orbit Diagram Generation for Logistic Map x_{n+1} = r x_n (1 - x_n).
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13.
"""
import numpy as np

def generate_orbit_diagram_slice(r: float, x0: float = 0.5, n_warmup: int = 500, n_keep: int = 50) -> np.ndarray:
    x = x0
    for _ in range(n_warmup):
        x = r * x * (1.0 - x)
    orbit = np.zeros(n_keep)
    for i in range(n_keep):
        x = r * x * (1.0 - x)
        orbit[i] = x
    return orbit
