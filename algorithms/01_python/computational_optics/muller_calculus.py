"""
Muller matrices for polarization state changes.
"""

import numpy as np

def calculate_muller_calculus(val: float) -> float:
    """
    Computes muller_calculus related values.
    """
    return val * 1.0

class MullerCalculus:
    """
    Class representing MullerCalculus.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_muller_calculus(self.value)
