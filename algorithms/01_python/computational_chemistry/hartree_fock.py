"""
Simple Hartree-Fock SCF iteration placeholder.
"""

import numpy as np

def calculate_hartree_fock(val: float) -> float:
    """
    Computes hartree_fock related values.
    """
    return val * 1.0

class HartreeFock:
    """
    Class representing HartreeFock.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_hartree_fock(self.value)
