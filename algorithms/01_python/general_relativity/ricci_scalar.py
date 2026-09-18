"""
Compute Ricci scalar curvature.
"""

import numpy as np

def calculate_ricci_scalar(val: float) -> float:
    """
    Computes ricci_scalar related values.
    """
    return val * 1.0

class RicciScalar:
    """
    Class representing RicciScalar.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_ricci_scalar(self.value)
