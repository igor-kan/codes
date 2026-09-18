"""
Curie-Weiss law for ferromagnetism.
"""

import numpy as np

def calculate_curie_weiss(val: float) -> float:
    """
    Computes curie_weiss related values.
    """
    return val * 1.0

class CurieWeiss:
    """
    Class representing CurieWeiss.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_curie_weiss(self.value)
