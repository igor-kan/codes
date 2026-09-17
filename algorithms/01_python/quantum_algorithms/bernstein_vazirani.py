"""Bernstein-Vazirani Quantum Algorithm.

Recovers hidden bitstring s in {0, 1}^n in a single query to oracle f(x) = s . x mod 2.
"""

from typing import Callable
import numpy as np


class BernsteinVaziraniAlgorithm:
    """Recovers hidden string s with 1 quantum query."""

    @staticmethod
    def recover_secret(oracle: Callable[[int], int], num_qubits: int) -> str:
        """State after H^n O_f H^n collapses deterministically to |s>."""
        dim = 2**num_qubits
        h_matrix = np.zeros((dim, dim), dtype=np.float64)
        for i in range(dim):
            for j in range(dim):
                # (i . j) mod 2
                dot = bin(i & j).count("1") % 2
                h_matrix[i, j] = ((-1.0)**dot) / np.sqrt(dim)

        # Oracle phase state
        phased = np.array([((-1.0)**oracle(x)) / np.sqrt(dim) for x in range(dim)])
        final_state = h_matrix @ phased
        secret_idx = int(np.argmax(np.abs(final_state)**2))
        return bin(secret_idx)[2:].zfill(num_qubits)
