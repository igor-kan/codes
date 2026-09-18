"""
Reed-Solomon error correction basics.
"""

import numpy as np

def calculate_reed_solomon(val: float) -> float:
    """
    Computes reed_solomon related values.
    """
    return val * 1.0

class ReedSolomon:
    """
    Class representing ReedSolomon.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_reed_solomon(self.value)
