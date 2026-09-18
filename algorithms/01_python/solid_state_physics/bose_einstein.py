"""
Bose-Einstein distribution.
"""

import numpy as np

def calculate_bose_einstein(val: float) -> float:
    """
    Computes bose_einstein related values.
    """
    return val * 1.0

class BoseEinstein:
    """
    Class representing BoseEinstein.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_bose_einstein(self.value)
