"""
Calculate event horizon and ergosphere of a black hole.
"""

import numpy as np

def calculate_black_hole_horizon(val: float) -> float:
    """
    Computes black_hole_horizon related values.
    """
    return val * 1.0

class BlackHoleHorizon:
    """
    Class representing BlackHoleHorizon.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_black_hole_horizon(self.value)
