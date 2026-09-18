"""
Calculate molecular dipole moment.
"""

import numpy as np

def calculate_dipole_moment(val: float) -> float:
    """
    Computes dipole_moment related values.
    """
    return val * 1.0

class DipoleMoment:
    """
    Class representing DipoleMoment.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_dipole_moment(self.value)
