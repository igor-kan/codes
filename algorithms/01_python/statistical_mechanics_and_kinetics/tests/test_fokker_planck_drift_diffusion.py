import numpy as np
from fokker_planck_drift_diffusion import fokker_planck_step


def test_fokker():
    x = np.linspace(-5, 5, 201)
    dx = x[1] - x[0]
    P = np.exp(-x**2) / np.sqrt(np.pi)
    drift = -x  # Ornstein-Uhlenbeck drift
    P_next = fokker_planck_step(P, drift, D=1.0, dx=dx, dt=1e-4)
    assert np.isclose(np.sum(P_next) * dx, 1.0, atol=1e-3)
