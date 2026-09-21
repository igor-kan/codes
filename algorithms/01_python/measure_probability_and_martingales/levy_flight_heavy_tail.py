"""
Lévy Stable Flight Simulation via Mantegna's Algorithm.
Reference: Evans & Rosenthal; Mantegna (1994).
"""
import numpy as np
import math

def simulate_levy_steps(alpha: float, n_steps: int, seed: int = 42) -> np.ndarray:
    """Simulates 1D heavy-tailed increments for stability index 0 < alpha <= 2."""
    rng = np.random.default_rng(seed)
    sigma = (math.gamma(1.0 + alpha) * np.sin(np.pi * alpha / 2.0) /
             (math.gamma((1.0 + alpha) / 2.0) * alpha * 2.0**((alpha - 1.0) / 2.0)))**(1.0 / alpha)
             
    u = rng.normal(0.0, sigma, size=n_steps)
    v = rng.normal(0.0, 1.0, size=n_steps)
    step = u / (np.abs(v)**(1.0 / alpha))
    return step
