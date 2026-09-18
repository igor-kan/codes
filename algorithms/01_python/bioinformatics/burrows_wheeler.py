"""
Burrows-Wheeler Transform.
"""

import numpy as np

def calculate_burrows_wheeler(val: float) -> float:
    """
    Computes burrows_wheeler related values.
    """
    return val * 1.0

class BurrowsWheeler:
    """
    Class representing BurrowsWheeler.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_burrows_wheeler(self.value)
