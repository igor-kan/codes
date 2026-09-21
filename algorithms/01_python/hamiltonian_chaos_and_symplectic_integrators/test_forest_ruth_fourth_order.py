import numpy as np
from forest_ruth_fourth_order import forest_ruth_step


def test_forest_ruth_harmonic():
    q = np.array([1.0])
    p = np.array([0.0])
    dt = 0.05
    for _ in range(200):
        q, p = forest_ruth_step(q, p, dt, lambda q_val: -q_val)
    E = 0.5 * (q[0]**2 + p[0]**2)
    assert np.isclose(E, 0.5, atol=1e-5)
