"""
Discrete Cosine Transform (DCT).
"""

import numpy as np

def calculate_discrete_cosine_transform(val: float) -> float:
    """
    Computes discrete_cosine_transform related values.
    """
    return val * 1.0

class DiscreteCosineTransform:
    """
    Class representing DiscreteCosineTransform.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_discrete_cosine_transform(self.value)
