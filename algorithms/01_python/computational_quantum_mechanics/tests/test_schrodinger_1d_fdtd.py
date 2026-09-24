import numpy as np
from schrodinger_1d_fdtd import split_operator_step


def test_unitary_norm_conservation():
    n = 256
    dx = 0.1
    x = (np.arange(n) - n / 2) * dx
    V = 0.5 * (x**2)
    psi0 = np.exp(-0.5 * x**2).astype(complex)
    norm0 = np.sum(np.abs(psi0)**2) * dx
    psi0 /= np.sqrt(norm0)

    psi = psi0.copy()
    for _ in range(30):
        psi = split_operator_step(psi, V, dx, dt=0.01)

    norm_final = np.sum(np.abs(psi)**2) * dx
    assert np.isclose(norm_final, 1.0, atol=1e-10)
