import numpy as np
from fourier_collocation_burgers_pde import burgers_spectral_rhs


def test_burgers_rhs():
    N = 64
    x = np.linspace(0, 2.0 * np.pi, N, endpoint=False)
    u = np.sin(x)
    rhs = burgers_spectral_rhs(u, nu=0.01)
    assert len(rhs) == N
    assert not np.any(np.isnan(rhs))
