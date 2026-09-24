import numpy as np
from delta_potential_well import delta_well_bound_energy, delta_well_wavefunction


def test_delta_well():
    alpha = 2.0
    E = delta_well_bound_energy(alpha)
    assert np.isclose(E, -2.0)
    x = np.linspace(-10, 10, 2001)
    dx = x[1] - x[0]
    psi = delta_well_wavefunction(x, alpha)
    assert np.isclose(np.sum(psi**2) * dx, 1.0, atol=1e-3)
