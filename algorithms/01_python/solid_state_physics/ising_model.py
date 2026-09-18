"""
1D Ising model transfer matrix.
"""

import numpy as np

def calculate_ising_model(val: float) -> float:
    """
    Computes ising_model related values.
    """
    return val * 1.0

class IsingModel:
    """
    Class representing IsingModel.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_ising_model(self.value)
