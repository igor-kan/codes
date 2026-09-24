"""Hawkes Self-Exciting Point Process for High-Frequency Order Book Bursts.

Conditional intensity: lambda(t) = mu + sum_{t_i < t} alpha * exp(-beta * (t - t_i)).
Branching ratio: eta = alpha / beta < 1 for subcritical stability.
"""
import numpy as np


def simulate_univariate_hawkes(mu: float, alpha: float, beta: float, T_max: float, seed: int = 42) -> np.ndarray:
    """Simulate event timestamps using Ogata's modified thinning algorithm."""
    if alpha >= beta:
        raise ValueError("Branching ratio alpha/beta must be < 1 for stationarity")
    np.random.seed(seed)
    t = 0.0
    history = []
    
    while t < T_max:
        # Upper bound on intensity
        lam_bar = mu + alpha * np.sum(np.exp(-beta * (t - np.array(history)))) if history else mu
        u = np.random.uniform(0, 1)
        w = -np.log(u) / lam_bar
        t = t + w
        if t >= T_max:
            break
        # Intensity at candidate time
        lam_cand = mu + alpha * np.sum(np.exp(-beta * (t - np.array(history))))
        d = np.random.uniform(0, 1)
        if d <= lam_cand / lam_bar:
            history.append(t)
            
    return np.array(history)
