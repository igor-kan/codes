"""
Hall coefficient calculation.
"""

import numpy as np

def calculate_hall_effect(val: float) -> float:
    """
    Computes hall_effect related values.
    """
    return val * 1.0

class HallEffect:
    """
    Class representing HallEffect.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_hall_effect(self.value)
