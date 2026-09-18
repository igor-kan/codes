"""
Moving average smoothing filter.
"""

import numpy as np

def calculate_moving_average(val: float) -> float:
    """
    Computes moving_average related values.
    """
    return val * 1.0

class MovingAverage:
    """
    Class representing MovingAverage.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_moving_average(self.value)
