"""
Analytic signal via Hilbert transform.
"""

import numpy as np

def calculate_hilbert_transform(val: float) -> float:
    """
    Computes hilbert_transform related values.
    """
    return val * 1.0

class HilbertTransform:
    """
    Class representing HilbertTransform.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_hilbert_transform(self.value)
