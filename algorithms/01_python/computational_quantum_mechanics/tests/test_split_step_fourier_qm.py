import numpy as np
from split_step_fourier_qm import split_step_propagate_1d


def test_split_step():
    x = np.linspace(-10, 10, 512)
    psi0 = np.exp(-0.5 * x**2).astype(complex)
    psi0 /= np.sqrt(np.sum(np.abs(psi0)**2) * (x[1] - x[0]))
    V = 0.5 * x**2
    psi_final = split_step_propagate_1d(psi0, x, V, dt=0.01, n_steps=20)
    norm = np.sum(np.abs(psi_final)**2) * (x[1] - x[0])
    assert np.isclose(norm, 1.0, atol=1e-8)
