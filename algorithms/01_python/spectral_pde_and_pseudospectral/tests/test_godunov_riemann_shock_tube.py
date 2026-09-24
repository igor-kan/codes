import numpy as np
from godunov_riemann_shock_tube import sod_initial_conditions


def test_sod_init():
    x = np.linspace(0, 1, 100)
    rho, u, P = sod_initial_conditions(x)
    assert rho[0] == 1.0 and rho[-1] == 0.125
    assert P[0] == 1.0 and P[-1] == 0.1
