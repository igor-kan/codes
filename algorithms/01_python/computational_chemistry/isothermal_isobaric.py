"""
NPT ensemble barostat integration.
"""

import numpy as np

def calculate_isothermal_isobaric(val: float) -> float:
    """
    Computes isothermal_isobaric related values.
    """
    return val * 1.0

class IsothermalIsobaric:
    """
    Class representing IsothermalIsobaric.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_isothermal_isobaric(self.value)
