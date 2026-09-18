"""
Kronig-Penney model band structure.
"""

import numpy as np

def calculate_kronig_penney(val: float) -> float:
    """
    Computes kronig_penney related values.
    """
    return val * 1.0

class KronigPenney:
    """
    Class representing KronigPenney.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_kronig_penney(self.value)
