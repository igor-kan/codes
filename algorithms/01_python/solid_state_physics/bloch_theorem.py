"""
Bloch wave calculations in 1D.
"""

import numpy as np

def calculate_bloch_theorem(val: float) -> float:
    """
    Computes bloch_theorem related values.
    """
    return val * 1.0

class BlochTheorem:
    """
    Class representing BlochTheorem.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_bloch_theorem(self.value)
