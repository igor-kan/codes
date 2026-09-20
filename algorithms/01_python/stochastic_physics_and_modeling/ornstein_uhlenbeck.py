"""
Ornstein-Uhlenbeck Process Exact Simulation and MLE Calibration.
References: Evans & Rosenthal - Probability and Random Processes.
"""
import numpy as np

def simulate_ornstein_uhlenbeck(theta: float, mu: float, sigma: float, x0: float, dt: float, n_steps: int):
    """Exact discrete simulation of dX_t = theta (mu - X_t) dt + sigma dW_t."""
    x = np.zeros(n_steps)
    x[0] = x0
    exp_factor = np.exp(-theta * dt)
    var_factor = (sigma**2 / (2.0 * theta)) * (1.0 - np.exp(-2.0 * theta * dt))
    std_factor = np.sqrt(var_factor)

    for i in range(1, n_steps):
        mean = x[i - 1] * exp_factor + mu * (1.0 - exp_factor)
        x[i] = mean + std_factor * np.random.normal()
    return x
