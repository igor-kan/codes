"""
Gillespie Stochastic Simulation Algorithm (SSA).
References: Gershenfeld - The Nature of Mathematical Modeling.
"""
import numpy as np

def gillespie_step(state: np.ndarray, propensity_func, stoich_matrix: np.ndarray):
    """
    Execute single Gillespie SSA step.
    propensity_func: returns 1D array of propensities a_j for each reaction.
    stoich_matrix: matrix of shape (n_reactions, n_species).
    """
    a = propensity_func(state)
    a0 = np.sum(a)
    if a0 <= 0:
        return state, float('inf')

    # Draw time to next reaction: tau ~ Exp(a0)
    r1 = np.random.uniform(0.0, 1.0)
    tau = -np.log(r1) / a0

    # Draw reaction index j with probability a_j / a0
    r2 = np.random.uniform(0.0, 1.0) * a0
    cumsum_a = np.cumsum(a)
    reaction_idx = np.searchsorted(cumsum_a, r2)
    reaction_idx = min(reaction_idx, len(a) - 1)

    # Update state
    new_state = state + stoich_matrix[reaction_idx]
    return new_state, tau
