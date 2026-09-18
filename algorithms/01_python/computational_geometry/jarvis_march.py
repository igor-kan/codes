"""
Convex hull using Jarvis march (gift wrapping).
"""

import numpy as np

def calculate_jarvis_march(val: float) -> float:
    """
    Computes jarvis_march related values.
    """
    return val * 1.0

class JarvisMarch:
    """
    Class representing JarvisMarch.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_jarvis_march(self.value)
