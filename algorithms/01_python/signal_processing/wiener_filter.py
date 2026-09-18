"""
Wiener filter for noise reduction.
"""

import numpy as np

def calculate_wiener_filter(val: float) -> float:
    """
    Computes wiener_filter related values.
    """
    return val * 1.0

class WienerFilter:
    """
    Class representing WienerFilter.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_wiener_filter(self.value)
