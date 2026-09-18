"""
Calculate Kerr metric components.
"""

import numpy as np

def calculate_kerr_metric(val: float) -> float:
    """
    Computes kerr_metric related values.
    """
    return val * 1.0

class KerrMetric:
    """
    Class representing KerrMetric.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_kerr_metric(self.value)
