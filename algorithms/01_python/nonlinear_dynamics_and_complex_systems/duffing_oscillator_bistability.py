"""
Duffing Driven Nonlinear Oscillator with Cubic Stiffness.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13.
"""
import numpy as np

def duffing_derivatives(x: float, v: float, t: float, delta: float, alpha: float, beta: float, gamma: float, omega: float):
    """
    dx/dt = v
    dv/dt = - delta v - alpha x - beta x^3 + gamma cos(omega t)
    """
    dv = -delta * v - alpha * x - beta * (x**3) + gamma * np.cos(omega * t)
    return v, dv
