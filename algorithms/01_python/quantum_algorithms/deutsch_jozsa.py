"""Deutsch-Jozsa Quantum Algorithm.

Determines if boolean function f: {0, 1}^n -> {0, 1} is constant or balanced in a single quantum query.
"""

from typing import Callable, Sequence
import numpy as np


class DeutschJozsaAlgorithm:
    """Evaluates constant vs balanced oracle properties."""

    @staticmethod
    def classify_function(oracle_eval: Callable[[int], int], num_qubits: int) -> str:
        """Simulate single query quantum phase kickback."""
        # In Deutsch-Jozsa, constructive interference occurs at |0^n> iff f is constant
        dim = 2**num_qubits
        hadamard_amplitudes = np.ones(dim, dtype=np.float64) / np.sqrt(dim)
        # Apply phase (-1)^f(x)
        phased_state = np.array([((-1.0)**oracle_eval(x)) * hadamard_amplitudes[x] for x in range(dim)])
        # Inner product with |+^n>
        prob_all_zeros = abs(np.sum(phased_state) / np.sqrt(dim))**2
        return "constant" if prob_all_zeros > 0.99 else "balanced"
