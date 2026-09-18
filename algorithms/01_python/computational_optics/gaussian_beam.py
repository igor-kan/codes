"""
Gaussian beam propagation.
"""

import numpy as np

def calculate_gaussian_beam(val: float) -> float:
    """
    Computes gaussian_beam related values.
    """
    return val * 1.0

class GaussianBeam:
    """
    Class representing GaussianBeam.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_gaussian_beam(self.value)
