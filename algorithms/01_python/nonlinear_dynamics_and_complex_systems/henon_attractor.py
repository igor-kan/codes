"""
Hénon 2D Discrete Chaotic Map: x_{n+1} = 1 - a x_n^2 + y_n, y_{n+1} = b x_n.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13.
"""
import numpy as np

def simulate_henon_map(n_steps: int, a: float = 1.4, b: float = 0.3,
                       x0: float = 0.1, y0: float = 0.1) -> np.ndarray:
    traj = np.zeros((n_steps, 2))
    x, y = x0, y0
    for i in range(n_steps):
        traj[i] = [x, y]
        x_next = 1.0 - a * (x**2) + y
        y_next = b * x
        x, y = x_next, y_next
    return traj
