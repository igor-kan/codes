"""Flashing Brownian Ratchet (Feynman-Smoluchowski Molecular Motor)."""
import numpy as np


def simulate_flashing_ratchet(n_steps: int, period: int, F_ext: float = -0.1, seed: int = 42) -> float:
    """Simulate net uphill drift induced by periodic on-off asymmetric ratchet potential."""
    np.random.seed(seed)
    x = 0.0
    dt = 0.01
    for step in range(n_steps):
        potential_on = ((step // period) % 2) == 0
        force = F_ext
        if potential_on:
            # Asymmetric sawtooth potential
            phase = x % 1.0
            force += 2.0 if phase < 0.25 else -0.667
        x += force * dt + np.sqrt(2.0 * dt) * np.random.standard_normal()
    return float(x)
