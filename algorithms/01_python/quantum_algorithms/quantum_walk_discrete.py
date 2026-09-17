"""Discrete-Time Quantum Random Walk on a 1D Line with Hadamard Coin.

Demonstrates ballistic wavepacket spreading: standard deviation sigma proportional to t.
"""

from typing import Tuple
import numpy as np


class DiscreteQuantumWalk1D:
    """Discrete quantum walk with Hadamard coin operator."""

    def __init__(self, steps: int):
        self.steps = steps
        self.num_positions = 2 * steps + 1
        self.zero_idx = steps
        # State: psi[pos, coin] where coin in {0: left, 1: right}
        self.psi = np.zeros((self.num_positions, 2), dtype=np.complex128)
        # Initial symmetric state
        self.psi[self.zero_idx, 0] = 1.0 / np.sqrt(2.0)
        self.psi[self.zero_idx, 1] = 1.0j / np.sqrt(2.0)

    def run(self) -> np.ndarray:
        """Simulate walk for specified steps."""
        h_coin = (1.0 / np.sqrt(2.0)) * np.array([[1.0, 1.0], [1.0, -1.0]])

        for _ in range(self.steps):
            # Coin flip
            coin_flipped = self.psi @ h_coin.T
            # Shift operator: left (coin 0) moves pos-1, right (coin 1) moves pos+1
            next_psi = np.zeros_like(self.psi)
            next_psi[:-1, 0] += coin_flipped[1:, 0]
            next_psi[1:, 1] += coin_flipped[:-1, 1]
            self.psi = next_psi

        # Total probability distribution
        return np.sum(np.abs(self.psi)**2, axis=1)
