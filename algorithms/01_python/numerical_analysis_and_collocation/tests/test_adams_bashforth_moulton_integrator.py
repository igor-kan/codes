import numpy as np
from adams_bashforth_moulton_integrator import abm4_step


def test_abm4():
    # dy/dt = y, exact y(t) = exp(t)
    h = 0.05
    t = np.array([0.0, 0.05, 0.10, 0.15])
    y = np.exp(t)
    t_next, y_next = abm4_step(lambda t, y: y, t, y, h)
    assert np.isclose(y_next, np.exp(0.20), atol=1e-5)
