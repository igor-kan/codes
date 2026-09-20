"""
Biot-Savart Law for Vortex Filaments and Induced Flow.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6, Ch. 3).
"""
import numpy as np

def vortex_ring_induced_velocity(circulation: float, radius: float, z: float) -> float:
    """Induced axial velocity at distance z along axis of a circular vortex ring of radius R: v_z = Gamma R^2 / (2 (R^2 + z^2)^(3/2))."""
    return float(circulation * (radius**2) / (2.0 * (radius**2 + z**2)**1.5))
