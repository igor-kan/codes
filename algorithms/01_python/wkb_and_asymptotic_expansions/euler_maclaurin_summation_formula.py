"""Euler-Maclaurin Summation Formula Connecting Discrete Sums and Integrals."""
from scipy.integrate import quad


def euler_maclaurin_leading(f, f_prime, a: int, b: int) -> float:
    """sum_{k=a}^b f(k) approx int_a^b f(x) dx + 0.5*(f(a) + f(b)) + 1/12*(f'(b) - f'(a))."""
    integral, _ = quad(f, a, b)
    return float(integral + 0.5 * (f(a) + f(b)) + (1.0 / 12.0) * (f_prime(b) - f_prime(a)))
