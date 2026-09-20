import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from adaptive_runge_kutta import adaptive_rk45_integrate

def test_oscillator_rk45():
    # Harmonic oscillator: [q, p], dq/dt = p, dp/dt = -q
    def derivs(t, y):
        return np.array([y[1], -y[0]])
    ts, ys = adaptive_rk45_integrate(derivs, [1.0, 0.0], (0.0, 2.0 * np.pi), tol=1e-7)
    assert np.isclose(ys[-1, 0], 1.0, atol=1e-4)
    assert np.isclose(ys[-1, 1], 0.0, atol=1e-4)
