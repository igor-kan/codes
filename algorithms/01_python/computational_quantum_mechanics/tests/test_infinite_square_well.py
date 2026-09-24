import numpy as np
from infinite_square_well import well_energy_eigenvalue, well_eigenfunction


def test_orthonormality():
    L = 2.0
    x = np.linspace(0, L, 1000)
    dx = x[1] - x[0]
    psi1 = well_eigenfunction(1, L, x)
    psi2 = well_eigenfunction(2, L, x)
    assert np.isclose(np.sum(psi1**2) * dx, 1.0, atol=1e-3)
    assert np.isclose(np.sum(psi1 * psi2) * dx, 0.0, atol=1e-3)
    assert well_energy_eigenvalue(2, L) == 4.0 * well_energy_eigenvalue(1, L)
