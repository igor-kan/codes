"""
Lempel-Ziv-Welch compression.
"""

import numpy as np

def calculate_lzw_compression(val: float) -> float:
    """
    Computes lzw_compression related values.
    """
    return val * 1.0

class LzwCompression:
    """
    Class representing LzwCompression.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_lzw_compression(self.value)
