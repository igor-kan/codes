import numpy as np
from allen_cahn_phase_field_pseudospectral import allen_cahn_free_energy


def test_free_energy():
    x = np.linspace(-1, 1, 100)
    dx = x[1] - x[0]
    u = np.ones_like(x)  # Minimum of potential (u = 1)
    F = allen_cahn_free_energy(u, dx, eps=0.05)
    assert np.isclose(F, 0.0)
