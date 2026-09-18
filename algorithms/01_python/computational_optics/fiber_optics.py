"""
Numerical aperture and V-number of an optical fiber.
"""

import numpy as np

def calculate_fiber_optics(val: float) -> float:
    """
    Computes fiber_optics related values.
    """
    return val * 1.0

class FiberOptics:
    """
    Class representing FiberOptics.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_fiber_optics(self.value)
