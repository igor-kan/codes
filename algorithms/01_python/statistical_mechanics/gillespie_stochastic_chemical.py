"""Gillespie Stochastic Simulation Algorithm (SSA) for Chemical Master Equations.

Simulates discrete, exact Markov jump processes in reaction networks.
"""

from typing import List, Tuple, Callable
import numpy as np


class GillespieAlgorithm:
    """Direct Gillespie SSA solver."""

    @staticmethod
    def step(state: np.ndarray, propensities: List[float],
             stoichiometry_matrix: np.ndarray) -> Tuple[float, np.ndarray]:
        """Draw next reaction time tau and firing channel mu."""
        a0 = sum(propensities)
        if a0 <= 0.0:
            return float('inf'), state
        # Time step tau = - ln(r1) / a0
        r1 = np.random.rand()
        tau = - np.log(max(1e-15, r1)) / a0
        # Choose reaction mu
        r2 = np.random.rand() * a0
        cumsum = 0.0
        mu = 0
        for idx, a in enumerate(propensities):
            cumsum += a
            if cumsum >= r2:
                mu = idx
                break
        new_state = state + stoichiometry_matrix[mu]
        return float(tau), new_state
