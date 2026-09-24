import numpy as np
from crank_nicolson_heat_diffusion import crank_nicolson_1d


def test_crank_nicolson():
    x = np.linspace(0, np.pi, 50)
    u0 = np.sin(x)
    u_final = crank_nicolson_1d(u0, alpha=1.0, dx=x[1]-x[0], dt=0.001, n_steps=10)
    # Energy decays
    assert np.max(u_final) < np.max(u0)
