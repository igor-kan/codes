import numpy as np
from chebyshev_tau_poisson_solver import solve_chebyshev_poisson


def test_poisson():
    N = 32
    f = np.ones(N + 1)
    u = solve_chebyshev_poisson(f)
    assert np.isclose(u[0], 0.0)
    assert np.isclose(u[-1], 0.0)
