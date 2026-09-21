"""
Van der Pol Nonlinear Relaxation Oscillator Limit Cycle.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13.
"""
def van_der_pol_derivatives(x: float, y: float, mu: float):
    """
    dx/dt = y
    dy/dt = mu (1 - x^2) y - x
    """
    return y, mu * (1.0 - x**2) * y - x
