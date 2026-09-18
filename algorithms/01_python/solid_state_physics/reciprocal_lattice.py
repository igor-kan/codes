"""
Compute reciprocal lattice vectors.
"""

import numpy as np

def calculate_reciprocal_lattice(val: float) -> float:
    """
    Computes reciprocal_lattice related values.
    """
    return val * 1.0

class ReciprocalLattice:
    """
    Class representing ReciprocalLattice.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_reciprocal_lattice(self.value)
