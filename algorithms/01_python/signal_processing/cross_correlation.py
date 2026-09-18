"""
Cross-correlation of two signals.
"""

import numpy as np

def calculate_cross_correlation(val: float) -> float:
    """
    Computes cross_correlation related values.
    """
    return val * 1.0

class CrossCorrelation:
    """
    Class representing CrossCorrelation.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_cross_correlation(self.value)
