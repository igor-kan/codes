"""
Orthogonal range searching.
"""

import numpy as np

def calculate_range_tree(val: float) -> float:
    """
    Computes range_tree related values.
    """
    return val * 1.0

class RangeTree:
    """
    Class representing RangeTree.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_range_tree(self.value)
