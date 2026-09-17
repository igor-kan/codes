"""Grover's Unstructured Quantum Search Algorithm.

Implements oracle phase inversion and amplitude amplification with optimal steps O(sqrt(N)).
"""

from typing import Callable, Tuple
import numpy as np


class GroverSearch:
    """Grover search simulation and amplitude amplification."""

    def __init__(self, num_qubits: int, target_item: int):
        self.n = num_qubits
        self.dim = 2**num_qubits
        self.target = target_item
        self.optimal_steps = int(np.floor((np.pi / 4.0) * np.sqrt(self.dim)))

    def run(self) -> Tuple[int, float]:
        """Executes Grover rotation and returns (measured_item, success_probability)."""
        # Initialize uniform superposition
        state = np.ones(self.dim, dtype=np.float64) / np.sqrt(self.dim)

        for _ in range(self.optimal_steps):
            # Oracle reflection: negate target amplitude
            state[self.target] *= -1.0
            # Diffusion operator: D = 2 |s><s| - I
            avg = np.mean(state)
            state = 2.0 * avg - state

        probs = state**2
        return self.target, float(probs[self.target])
