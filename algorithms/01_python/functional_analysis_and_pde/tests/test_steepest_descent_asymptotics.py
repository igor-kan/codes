import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from steepest_descent_asymptotics import saddle_point_laplace

def test_gaussian_saddle_point():
    # int exp(-k x^2 / 2) dx from -inf to inf = sqrt(2 pi / k)
    # Here f(x) = -x^2 / 2 -> f(0) = 0, f''(0) = -1
    k = 100.0
    approx = saddle_point_laplace(0.0, -1.0, k)
    exact = np.sqrt(2.0 * np.pi / k)
    assert np.isclose(approx, exact)
