"""
Run-length encoding on Burrows-Wheeler Transformed text.
"""

import numpy as np

def calculate_bwt_rle(val: float) -> float:
    """
    Computes bwt_rle related values.
    """
    return val * 1.0

class BwtRle:
    """
    Class representing BwtRle.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_bwt_rle(self.value)
