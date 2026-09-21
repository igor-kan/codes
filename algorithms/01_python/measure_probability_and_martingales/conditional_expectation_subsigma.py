"""
Conditional Expectation E[X | G] for Partition-Generated Sub-Sigma Algebras.
Reference: Evans & Rosenthal, Probability and Statistics.
"""
import numpy as np
from typing import List

def conditional_expectation_partition(X: np.ndarray, partition_indices: List[List[int]]) -> np.ndarray:
    """Computes discrete conditional expectation on each atom of the partition."""
    E_X = np.zeros_like(X, dtype=float)
    for atom in partition_indices:
        mean_val = np.mean(X[atom])
        E_X[atom] = mean_val
    return E_X
