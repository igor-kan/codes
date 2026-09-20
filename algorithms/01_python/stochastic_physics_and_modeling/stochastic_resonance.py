"""
Stochastic Resonance in a Bistable Double-Well Potential.
References: Gershenfeld - The Nature of Mathematical Modeling.
"""
import numpy as np

def bistable_stochastic_step(x: float, A: float, omega: float, t: float, D: float, dt: float) -> float:
    """
    Bistable system: dx/dt = x - x^3 + A cos(omega t) + sqrt(2D) xi(t).
    """
    drift = x - x**3 + A * np.cos(omega * t)
    noise = np.sqrt(2.0 * D * dt) * np.random.normal()
    return x + drift * dt + noise
