"""
Compute Einstein tensor.
"""

import numpy as np

def calculate_einstein_tensor(val: float) -> float:
    """
    Computes einstein_tensor related values.
    """
    return val * 1.0

class EinsteinTensor:
    """
    Class representing EinsteinTensor.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_einstein_tensor(self.value)
