"""
Discrete wavelet transform (Haar).
"""

import numpy as np

def calculate_wavelet_transform(val: float) -> float:
    """
    Computes wavelet_transform related values.
    """
    return val * 1.0

class WaveletTransform:
    """
    Class representing WaveletTransform.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_wavelet_transform(self.value)
