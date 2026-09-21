import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lotka_volterra_dynamics import integrate_lotka_volterra

def test_equilibrium_fixed_point():
    # Fixed point: x* = gamma / delta, y* = alpha / beta
    alpha, beta = 1.0, 0.1
    delta, gamma = 0.02, 0.5
    x_star = gamma / delta  # 25.0
    y_star = alpha / beta   # 10.0
    traj = integrate_lotka_volterra(x_star, y_star, alpha, beta, delta, gamma, t_max=1.0)
    assert np.allclose(traj[:, 0], x_star, atol=1e-3)
    assert np.allclose(traj[:, 1], y_star, atol=1e-3)
