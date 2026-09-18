"""
Calculate Schwarzschild metric components.
"""

import numpy as np

def calculate_schwarzschild_metric(val: float) -> float:
    """
    Computes schwarzschild_metric related values.
    """
    return val * 1.0

class SchwarzschildMetric:
    """
    Class representing SchwarzschildMetric.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_schwarzschild_metric(self.value)
