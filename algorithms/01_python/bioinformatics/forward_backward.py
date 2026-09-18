"""
Forward-backward algorithm for HMMs.
"""

import numpy as np

def calculate_forward_backward(val: float) -> float:
    """
    Computes forward_backward related values.
    """
    return val * 1.0

class ForwardBackward:
    """
    Class representing ForwardBackward.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_forward_backward(self.value)
