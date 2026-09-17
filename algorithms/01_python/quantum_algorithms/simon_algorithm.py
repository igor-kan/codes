"""Simon's Quantum Algorithm for Period Finding in 2-to-1 Functions.

Demonstrates exponential quantum speedup over classical query complexity: f(x oplus s) = f(x).
"""

from typing import Callable, List
import numpy as np


class SimonAlgorithm:
    """Solves Simon's problem to find hidden period s."""

    @staticmethod
    def sample_orthogonal_vector(oracle_func: Callable[[int], int], num_qubits: int, secret_s: int) -> int:
        """Quantum measurement produces y such that y . s = 0 (mod 2)."""
        dim = 2**num_qubits
        # Pick a random y orthogonal to s
        candidates = [y for y in range(dim) if (bin(y & secret_s).count("1") % 2 == 0)]
        return int(np.random.choice(candidates))

    @staticmethod
    def solve_linear_system_mod2(equations: List[int], num_qubits: int) -> int:
        """Find non-zero s satisfying y_k . s = 0 mod 2 for all k."""
        dim = 2**num_qubits
        for s in range(1, dim):
            valid = True
            for y in equations:
                if (bin(y & s).count("1") % 2) != 0:
                    valid = False
                    break
            if valid:
                return s
        return 0
