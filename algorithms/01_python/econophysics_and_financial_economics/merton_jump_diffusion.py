"""Merton Jump Diffusion Model for Asset Pricing with Discontinuous Jumps.

dS_t / S_t- = (r - lambda * k) * dt + sigma * dW_t + (J - 1) * dN_t
ln(J) ~ Normal(mu_j, sigma_j^2).
"""
import numpy as np


def merton_jump_diffusion_sample(S0: float, r: float, sigma: float, lam: float,
                                 mu_j: float, sigma_j: float, T: float,
                                 n_steps: int, n_paths: int, seed: int = 42) -> np.ndarray:
    """Simulate asset paths with Poisson jump arrivals."""
    np.random.seed(seed)
    dt = T / n_steps
    k = np.exp(mu_j + 0.5 * sigma_j**2) - 1.0
    drift = (r - 0.5 * sigma**2 - lam * k) * dt
    
    S = np.zeros((n_paths, n_steps + 1))
    S[:, 0] = S0
    
    for t in range(n_steps):
        dW = np.random.standard_normal(n_paths) * np.sqrt(dt)
        n_jumps = np.random.poisson(lam * dt, n_paths)
        jump_factor = np.zeros(n_paths)
        for i in range(n_paths):
            if n_jumps[i] > 0:
                jump_factor[i] = np.sum(np.random.normal(mu_j, sigma_j, n_jumps[i]))
        
        S[:, t + 1] = S[:, t] * np.exp(drift + sigma * dW + jump_factor)
        
    return S
