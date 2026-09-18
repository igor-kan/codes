"""
Infinite Impulse Response (IIR) filter.
"""

import numpy as np

def calculate_iir_filter(val: float) -> float:
    """
    Computes iir_filter related values.
    """
    return val * 1.0

class IirFilter:
    """
    Class representing IirFilter.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_iir_filter(self.value)
