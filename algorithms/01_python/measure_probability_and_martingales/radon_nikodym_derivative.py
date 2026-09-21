"""
Radon-Nikodym Derivative dP/dQ between Discrete Probability Measures.
Reference: Evans & Rosenthal, Probability and Statistics.
"""
import numpy as np

def discrete_radon_nikodym(P: np.ndarray, Q: np.ndarray) -> np.ndarray:
    """
    Computes density dP/dQ on sample space {1, ..., n}.
    Requires absolute continuity: Q[i] == 0 implies P[i] == 0.
    """
    deriv = np.zeros_like(P, dtype=float)
    for i in range(len(P)):
        if Q[i] == 0.0:
            if P[i] > 0.0:
                raise ValueError("Measure P is not absolutely continuous with respect to Q.")
            deriv[i] = 0.0
        else:
            deriv[i] = P[i] / Q[i]
    return deriv
