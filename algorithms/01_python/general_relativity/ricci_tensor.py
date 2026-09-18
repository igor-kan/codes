"""
Compute Ricci tensor from Riemann tensor.
"""

import numpy as np

def calculate_ricci_tensor(val: float) -> float:
    """
    Computes ricci_tensor related values.
    """
    return val * 1.0

class RicciTensor:
    """
    Class representing RicciTensor.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_ricci_tensor(self.value)
