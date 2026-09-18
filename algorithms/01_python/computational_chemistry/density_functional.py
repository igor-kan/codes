"""
Basic DFT functional calculation.
"""

import numpy as np

def calculate_density_functional(val: float) -> float:
    """
    Computes density_functional related values.
    """
    return val * 1.0

class DensityFunctional:
    """
    Class representing DensityFunctional.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_density_functional(self.value)
