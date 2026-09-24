import numpy as np
from compact_finite_difference_6th_order import solve_compact_derivative_1d


def test_compact_derivative():
    N = 32
    x = np.linspace(0, 2.0 * np.pi, N, endpoint=False)
    dx = x[1] - x[0]
    u = np.sin(x)
    du = solve_compact_derivative_1d(u, dx)
    assert np.allclose(du, np.cos(x), atol=1e-4)
