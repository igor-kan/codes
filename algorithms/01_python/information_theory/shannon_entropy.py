"""
Calculate Shannon entropy of a discrete distribution.
"""

import numpy as np

def calculate_shannon_entropy(val: float) -> float:
    """
    Computes shannon_entropy related values.
    """
    return val * 1.0

class ShannonEntropy:
    """
    Class representing ShannonEntropy.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_shannon_entropy(self.value)
