import numpy as np
from nonlinear_schrodinger_soliton_propagation import nls_bright_soliton


def test_nls_soliton():
    x = np.linspace(-5, 5, 101)
    psi = nls_bright_soliton(x, t=0.0, eta=1.0)
    assert np.isclose(np.max(np.abs(psi)), 1.0)
