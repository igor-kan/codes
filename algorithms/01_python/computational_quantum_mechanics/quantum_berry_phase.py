"""
Geometric Berry Phase for Spin-1/2 in Precessing Magnetic Field.
References: Izaac & Wang - Computational Quantum Mechanics.
"""
import numpy as np

def spin_half_berry_phase(solid_angle: float) -> float:
    """Geometric phase for spin-1/2 adiabatically tracing solid angle Omega: gamma = -0.5 * Omega."""
    return -0.5 * solid_angle
