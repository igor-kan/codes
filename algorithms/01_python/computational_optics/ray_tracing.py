"""
Simple paraxial ray tracing matrix method.
"""

import numpy as np

def calculate_ray_tracing(val: float) -> float:
    """
    Computes ray_tracing related values.
    """
    return val * 1.0

class RayTracing:
    """
    Class representing RayTracing.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_ray_tracing(self.value)
