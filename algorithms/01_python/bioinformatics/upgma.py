"""
Unweighted Pair Group Method with Arithmetic Mean.
"""

import numpy as np

def calculate_upgma(val: float) -> float:
    """
    Computes upgma related values.
    """
    return val * 1.0

class Upgma:
    """
    Class representing Upgma.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_upgma(self.value)
