"""
Memory-efficient global alignment.
"""

import numpy as np

def calculate_hirschberg(val: float) -> float:
    """
    Computes hirschberg related values.
    """
    return val * 1.0

class Hirschberg:
    """
    Class representing Hirschberg.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_hirschberg(self.value)
