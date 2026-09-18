"""
Finite Impulse Response (FIR) filter.
"""

import numpy as np

def calculate_fir_filter(val: float) -> float:
    """
    Computes fir_filter related values.
    """
    return val * 1.0

class FirFilter:
    """
    Class representing FirFilter.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_fir_filter(self.value)
