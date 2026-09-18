"""
Nussinov RNA folding algorithm.
"""

import numpy as np

def calculate_nussinov(val: float) -> float:
    """
    Computes nussinov related values.
    """
    return val * 1.0

class Nussinov:
    """
    Class representing Nussinov.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_nussinov(self.value)
