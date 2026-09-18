"""
Discrete Kalman filter state estimation.
"""

import numpy as np

def calculate_kalman_filter(val: float) -> float:
    """
    Computes kalman_filter related values.
    """
    return val * 1.0

class KalmanFilter:
    """
    Class representing KalmanFilter.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_kalman_filter(self.value)
