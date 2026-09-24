"""ABC-Rejection Sampling for Intractable Likelihood Simulation Models."""
import numpy as np
from typing import Callable


def abc_rejection(simulator: Callable, summary_stat: Callable, observed_stat: float,
                  epsilon: float, n_proposals: int = 1000) -> np.ndarray:
    """Accept parameter theta if |S(x_sim) - S_obs| < epsilon."""
    accepted = []
    for _ in range(n_proposals):
        theta = np.random.uniform(0.0, 10.0)
        sim_data = simulator(theta)
        stat = summary_stat(sim_data)
        if abs(stat - observed_stat) < epsilon:
            accepted.append(theta)
    return np.array(accepted)
