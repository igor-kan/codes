"""
Local sequence alignment.
"""

import numpy as np

def calculate_smith_waterman(val: float) -> float:
    """
    Computes smith_waterman related values.
    """
    return val * 1.0

class SmithWaterman:
    """
    Class representing SmithWaterman.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_smith_waterman(self.value)
