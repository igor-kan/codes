"""
Lévy Flight Anomalous Diffusion Generator.
References: Gershenfeld - The Nature of Mathematical Modeling.
"""
import numpy as np

def sample_levy_stable(alpha: float, size: int = 1000):
    """Sample symmetric alpha-stable distribution using Chambers-Mallows-Stuck method."""
    u = np.random.uniform(-0.5 * np.pi, 0.5 * np.pi, size)
    w = np.random.exponential(1.0, size)
    x = np.sin(alpha * u) / (np.cos(u)**(1.0 / alpha)) * (np.cos((1.0 - alpha) * u) / w)**((1.0 - alpha) / alpha)
    return x

def levy_flight_walk(alpha: float, n_steps: int):
    """Generate 2D Lévy flight path."""
    steps = sample_levy_stable(alpha, n_steps)
    angles = np.random.uniform(0.0, 2.0 * np.pi, n_steps)
    dx = steps * np.cos(angles)
    dy = steps * np.sin(angles)
    return np.cumsum(dx), np.cumsum(dy)
