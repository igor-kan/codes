"""
Ferragina-Manzini index for fast string matching.
"""

import numpy as np

def calculate_fm_index(val: float) -> float:
    """
    Computes fm_index related values.
    """
    return val * 1.0

class FmIndex:
    """
    Class representing FmIndex.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_fm_index(self.value)
