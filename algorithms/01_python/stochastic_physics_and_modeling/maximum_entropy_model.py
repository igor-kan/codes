"""
Maximum Entropy (MaxEnt) Discrete Distribution Estimator.
References: Gershenfeld - The Nature of Mathematical Modeling.
"""
import numpy as np
from scipy.optimize import minimize

def max_entropy_distribution(target_mean: float, states: np.ndarray) -> np.ndarray:
    """Find Boltzmann/Gibbs maximum entropy distribution P(s) = exp(-lambda s)/Z matching target mean."""
    states = np.asarray(states, dtype=float)
    
    def loss(lamb):
        z = np.sum(np.exp(-lamb * states))
        p = np.exp(-lamb * states) / z
        mean = np.sum(states * p)
        return (mean - target_mean)**2

    res = minimize(loss, [0.0], method='BFGS')
    lamb_opt = res.x[0]
    z = np.sum(np.exp(-lamb_opt * states))
    return np.exp(-lamb_opt * states) / z
