"""
Solve TOV equation for neutron stars.
"""

import numpy as np

def calculate_tolman_oppenheimer_volkoff(val: float) -> float:
    """
    Computes tolman_oppenheimer_volkoff related values.
    """
    return val * 1.0

class TolmanOppenheimerVolkoff:
    """
    Class representing TolmanOppenheimerVolkoff.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_tolman_oppenheimer_volkoff(self.value)
