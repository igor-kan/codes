"""Langevin Stochastic Dynamics (Brownian Motion with Friction and Thermal Fluctuations).

m * dv/dt = -gamma * v + F_ext + sqrt(2 * gamma * k_B * T) * eta(t).
"""
import numpy as np


def langevin_simulate(x0: float, v0: float, gamma: float, T: float, mass: float,
                      dt: float, n_steps: int, seed: int = 42) -> tuple:
    """Simulate Langevin particle via velocity-Verlet BAOAB splitting."""
    np.random.seed(seed)
    k_B = 1.0
    sigma_v = np.sqrt(k_B * T / mass)
    c1 = np.exp(-gamma * dt / mass)
    c2 = np.sqrt(1.0 - c1**2) * sigma_v
    
    x = np.zeros(n_steps + 1)
    v = np.zeros(n_steps + 1)
    x[0] = x0
    v[0] = v0
    
    for t in range(n_steps):
        v_half = v[t]
        x[t + 1] = x[t] + 0.5 * dt * v_half
        v_bath = c1 * v_half + c2 * np.random.standard_normal()
        x[t + 1] += 0.5 * dt * v_bath
        v[t + 1] = v_bath
        
    return x, v
