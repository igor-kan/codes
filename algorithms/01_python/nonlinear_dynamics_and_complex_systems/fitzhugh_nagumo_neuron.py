"""
FitzHugh-Nagumo Model of Neuronal Excitability and Action Potentials.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13.
"""
import numpy as np

def step_fitzhugh_nagumo(v: float, w: float, I_ext: float,
                          dt: float = 0.05, a: float = 0.7, b: float = 0.8, tau: float = 12.5):
    """
    dv/dt = v - v^3/3 - w + I
    dw/dt = (v + a - b w) / tau
    """
    dv = v - (v**3) / 3.0 - w + I_ext
    dw = (v + a - b * w) / tau
    return v + dt * dv, w + dt * dw
