"""
Chan's output-sensitive convex hull algorithm.
"""

import numpy as np

def calculate_chan_algorithm(val: float) -> float:
    """
    Computes chan_algorithm related values.
    """
    return val * 1.0

class ChanAlgorithm:
    """
    Class representing ChanAlgorithm.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_chan_algorithm(self.value)
