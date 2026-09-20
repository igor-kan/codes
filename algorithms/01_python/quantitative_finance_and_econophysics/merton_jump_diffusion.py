"""
Merton Jump Diffusion Process Simulation.
References: Jovanovic - Econophysics and Financial Economics.
"""
import numpy as np

def simulate_merton_jumps(S0, mu, sigma, lambda_jump, mu_jump, sigma_jump, dt, n_steps):
    """Simulate asset price under Merton's jump-diffusion model."""
    S = np.zeros(n_steps)
    S[0] = S0
    k_expected = np.exp(mu_jump + 0.5 * sigma_jump**2) - 1.0
    drift = (mu - lambda_jump * k_expected - 0.5 * sigma**2) * dt

    for i in range(1, n_steps):
        n_jumps = np.random.poisson(lambda_jump * dt)
        jump_factor = 0.0
        if n_jumps > 0:
            jump_factor = np.sum(np.random.normal(mu_jump, sigma_jump, size=n_jumps))
        diff = sigma * np.sqrt(dt) * np.random.normal()
        S[i] = S[i - 1] * np.exp(drift + diff + jump_factor)
    return S
