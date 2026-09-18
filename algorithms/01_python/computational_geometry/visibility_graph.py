"""
Visibility graph for path planning.
"""

import numpy as np

def calculate_visibility_graph(val: float) -> float:
    """
    Computes visibility_graph related values.
    """
    return val * 1.0

class VisibilityGraph:
    """
    Class representing VisibilityGraph.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_visibility_graph(self.value)
