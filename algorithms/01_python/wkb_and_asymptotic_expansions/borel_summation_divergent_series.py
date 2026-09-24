"""Borel Transform and Resummation of Divergent Asymptotic Factorial Series."""
import numpy as np
import math


def borel_transform_coefficients(a_coeffs: list) -> list:
    """Borel transform B(t) = sum a_n / n! * t^n."""
    return [a_coeffs[n] / math.factorial(n) for n in range(len(a_coeffs))]
