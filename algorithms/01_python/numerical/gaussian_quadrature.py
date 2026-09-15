"""Gauss-Legendre quadrature (Numerical Recipes 4.5)."""
import math

NODES = [
    0.0,
    -0.5384693101056831, 0.5384693101056831,
    -0.9061798459386640, 0.9061798459386640,
]
WEIGHTS = [
    0.5688888888888889,
    0.4786286704993665, 0.4786286704993665,
    0.2369268850561891, 0.2369268850561891,
]


def gaussian_quadrature(function, a, b):
    midpoint = 0.5 * (a + b)
    half = 0.5 * (b - a)
    total = 0.0
    for node, weight in zip(NODES, WEIGHTS):
        total += weight * function(midpoint + half * node)
    return total * half


if __name__ == "__main__":
    assert abs(gaussian_quadrature(lambda x: x * x, 0.0, 1.0) - 1.0 / 3.0) < 1e-12
    assert abs(gaussian_quadrature(lambda x: x ** 7, 0.0, 1.0) - 1.0 / 8.0) < 1e-12
    print("gaussian quadrature ok")
