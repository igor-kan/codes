import numpy as np
from chirikov_standard_map import standard_map_step, standard_map_orbit


def test_standard_map_invariants():
    # When K = 0, momentum is conserved: p_next = p
    th0, p0 = 1.0, 2.0
    th1, p1 = standard_map_step(th0, p0, K=0.0)
    assert np.isclose(p1, p0)

    # Orbit runs without error
    thetas, ps = standard_map_orbit(0.5, 0.5, K=0.97, n_iterations=100)
    assert len(thetas) == 100
    assert np.all(thetas >= 0.0) and np.all(thetas <= 2.0 * np.pi)
