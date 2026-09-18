"""
Inverse Fast Fourier Transform.
"""

import numpy as np

def calculate_inverse_fft(val: float) -> float:
    """
    Computes inverse_fft related values.
    """
    return val * 1.0

class InverseFft:
    """
    Class representing InverseFft.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_inverse_fft(self.value)
