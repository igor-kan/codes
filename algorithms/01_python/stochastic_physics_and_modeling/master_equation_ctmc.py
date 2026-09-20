"""
Continuous-Time Markov Chain Master Equation Solver.
References: Evans & Rosenthal - Probability and Random Processes.
"""
import numpy as np
from scipy.linalg import expm

def solve_ctmc_master_equation(p0: np.ndarray, Q_generator: np.ndarray, t: float) -> np.ndarray:
    """Solve dP/dt = P Q: P(t) = P(0) exp(Q t)."""
    return p0 @ expm(Q_generator * t)

def stationary_distribution_ctmc(Q_generator: np.ndarray) -> np.ndarray:
    """Compute stationary distribution pi Q = 0 with sum(pi) = 1."""
    n = Q_generator.shape[0]
    A = Q_generator.T.copy()
    A[-1, :] = 1.0  # Replace last equation with normalization
    b = np.zeros(n)
    b[-1] = 1.0
    return np.linalg.solve(A, b)
