"""
Compute Riemann curvature tensor.
"""

import numpy as np

def calculate_riemann_tensor(val: float) -> float:
    """
    Computes riemann_tensor related values.
    """
    return val * 1.0

class RiemannTensor:
    """
    Class representing RiemannTensor.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_riemann_tensor(self.value)
