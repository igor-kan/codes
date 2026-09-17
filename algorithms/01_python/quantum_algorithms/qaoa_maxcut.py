"""Quantum Approximate Optimization Algorithm (QAOA) for Max-Cut.

Constructs problem Hamiltonian H_C and transverse mixer H_B for combinatorial optimization.
"""

from typing import List, Tuple, Sequence
import numpy as np


class QAOAMaxCut:
    """QAOA cost function and Hamiltonian formulation."""

    def __init__(self, edges: List[Tuple[int, int]], num_nodes: int):
        self.edges = edges
        self.n = num_nodes

    def cut_value(self, bitstring: Sequence[int]) -> int:
        """Evaluate number of edges cut by partition."""
        cut = 0
        for u, v in self.edges:
            if bitstring[u] != bitstring[v]:
                cut += 1
        return cut
