"""
Shannon-Fano coding.
"""

import numpy as np

def calculate_shannon_fano(val: float) -> float:
    """
    Computes shannon_fano related values.
    """
    return val * 1.0

class ShannonFano:
    """
    Class representing ShannonFano.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_shannon_fano(self.value)
