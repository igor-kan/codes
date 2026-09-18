"""
Jones vectors and matrices for polarization.
"""

import numpy as np

def calculate_jones_calculus(val: float) -> float:
    """
    Computes jones_calculus related values.
    """
    return val * 1.0

class JonesCalculus:
    """
    Class representing JonesCalculus.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_jones_calculus(self.value)
