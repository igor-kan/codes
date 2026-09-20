"""
Classical Hannay Angle for Slowly Modulated Integrable Systems.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def hannay_angle_circle(solid_angle: float) -> float:
    """Hannay angle for bead on precessing hoop: Delta theta_H = -Omega."""
    return -solid_angle
