"""Horner's method for polynomial evaluation (Numerical Recipes 5.3)."""
def horner(coefficients, x):
    """Evaluate polynomial with lowest-order coefficient first."""
    result = 0.0
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def horner_with_derivative(coefficients, x):
    """Evaluate polynomial and its first derivative in one pass."""
    value = 0.0
    derivative = 0.0
    for coefficient in reversed(coefficients):
        derivative = derivative * x + value
        value = value * x + coefficient
    return value, derivative


if __name__ == "__main__":
    coefficients = [-1.0, 2.0, -6.0, 2.0]
    value, derivative = horner_with_derivative(coefficients, 3.0)
    assert abs(value - 5.0) < 1e-9
    assert abs(derivative - 20.0) < 1e-9
    assert abs(horner(coefficients, 3.0) - 5.0) < 1e-9
    print("horner ok")
