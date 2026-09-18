"""
k-d tree construction and nearest neighbor search.
"""

import numpy as np

def calculate_kd_tree(val: float) -> float:
    """
    Computes kd_tree related values.
    """
    return val * 1.0

class KdTree:
    """
    Class representing KdTree.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_kd_tree(self.value)
