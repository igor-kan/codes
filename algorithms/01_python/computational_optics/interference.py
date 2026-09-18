"""
Two-slit interference pattern.
"""

import numpy as np

def calculate_interference(val: float) -> float:
    """
    Computes interference related values.
    """
    return val * 1.0

class Interference:
    """
    Class representing Interference.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_interference(self.value)
