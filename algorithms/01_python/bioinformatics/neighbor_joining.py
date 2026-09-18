"""
Neighbor-joining phylogenetic tree construction.
"""

import numpy as np

def calculate_neighbor_joining(val: float) -> float:
    """
    Computes neighbor_joining related values.
    """
    return val * 1.0

class NeighborJoining:
    """
    Class representing NeighborJoining.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_neighbor_joining(self.value)
