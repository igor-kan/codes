"""
Global sequence alignment.
"""

import numpy as np

def calculate_needleman_wunsch(val: float) -> float:
    """
    Computes needleman_wunsch related values.
    """
    return val * 1.0

class NeedlemanWunsch:
    """
    Class representing NeedlemanWunsch.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_needleman_wunsch(self.value)
