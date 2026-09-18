"""
Construct stress-energy tensor for perfect fluid.
"""

import numpy as np

def calculate_stress_energy_tensor(val: float) -> float:
    """
    Computes stress_energy_tensor related values.
    """
    return val * 1.0

class StressEnergyTensor:
    """
    Class representing StressEnergyTensor.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_stress_energy_tensor(self.value)
