import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helmholtz_hodge_decomposition import helmholtz_decomposition_2d

def test_decomposition():
    nx, ny = 32, 32
    # Irrotational field: grad(sin(x) cos(y))
    x = np.linspace(0, 2*np.pi, nx, endpoint=False)
    y = np.linspace(0, 2*np.pi, ny, endpoint=False)
    X, Y = np.meshgrid(x, y)
    u_pure_irr = np.cos(X) * np.cos(Y)
    v_pure_irr = -np.sin(X) * np.sin(Y)

    (u_sol, v_sol), (u_irr, v_irr) = helmholtz_decomposition_2d(u_pure_irr, v_pure_irr)
    # Solenoidal component should be nearly 0
    assert np.allclose(u_sol, 0.0, atol=1e-5)
    assert np.allclose(v_sol, 0.0, atol=1e-5)
