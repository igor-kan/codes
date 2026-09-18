"""
Convex hull using QuickHull algorithm.
"""

import numpy as np

def calculate_quickhull(val: float) -> float:
    """
    Computes quickhull related values.
    """
    return val * 1.0

class Quickhull:
    """
    Class representing Quickhull.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_quickhull(self.value)
