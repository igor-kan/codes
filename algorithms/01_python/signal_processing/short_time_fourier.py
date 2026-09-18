"""
Short-time Fourier transform (STFT).
"""

import numpy as np

def calculate_short_time_fourier(val: float) -> float:
    """
    Computes short_time_fourier related values.
    """
    return val * 1.0

class ShortTimeFourier:
    """
    Class representing ShortTimeFourier.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_short_time_fourier(self.value)
