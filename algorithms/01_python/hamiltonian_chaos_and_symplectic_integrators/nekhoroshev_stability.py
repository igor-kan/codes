"""Nekhoroshev Theorem Exponential Stability Time Estimate.

For steep, quasi-integrable Hamiltonian systems:
||I(t) - I(0)|| < R_0 * epsilon^b  for all  t <= T_0 * exp((epsilon_0 / epsilon)^a),
providing exponentially long stability times for Solar System planetary orbits.
"""
import numpy as np


def nekhoroshev_stability_time(epsilon: float, a_exponent: float = 0.25,
                               epsilon_0: float = 0.1, T_0: float = 1.0) -> float:
    """Estimate stability timescale in log10(T)."""
    if epsilon <= 0:
        raise ValueError("Perturbation parameter epsilon must be positive")
    ratio = epsilon_0 / epsilon
    exponent = ratio**a_exponent
    # Return log10(T) to prevent overflow
    return float(np.log10(T_0) + exponent / np.log(10.0))
