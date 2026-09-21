"""
Euler-Maclaurin Summation Formula Connecting Discrete Sums to Integrals.
Reference: Mauch, Intro to Applied Mathematics; Chow.
"""
def euler_maclaurin_first_order(f_func, f_deriv_func, a: int, b: int) -> float:
    """
    sum_{k=a}^b f(k) approx int_a^b f(x) dx + 1/2(f(a) + f(b)) + 1/12(f'(b) - f'(a)).
    """
    # Composite trapezoidal rule as integral approx
    import numpy as np
    x = np.linspace(a, b, 1000)
    integral = np.trapz(f_func(x), x)
    correction1 = 0.5 * (f_func(a) + f_func(b))
    correction2 = (1.0 / 12.0) * (f_deriv_func(b) - f_deriv_func(a))
    return float(integral + correction1 + correction2)
