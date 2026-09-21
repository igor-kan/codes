"""
Poincaré-Lindstedt Method for Nonlinear Oscillators without Secular Terms.
Reference: Mauch, Intro to Applied Mathematics, Ch. 28; Nayfeh, Perturbation Methods.
"""
def duffing_corrected_frequency(omega0: float, epsilon: float, amplitude: float) -> float:
    """
    For x'' + omega0^2 x + epsilon x^3 = 0:
    omega = omega0 * (1 + 3/8 epsilon A^2 / omega0^2).
    """
    return float(omega0 * (1.0 + (3.0 / 8.0) * epsilon * (amplitude**2) / (omega0**2)))
