import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from chebyshev_spectral_differentiation import chebyshev_diff_matrix

def test_spectral_derivative():
    N = 16
    x, D = chebyshev_diff_matrix(N)
    u = np.sin(x)
    du_num = D @ u
    du_exact = np.cos(x)
    assert np.allclose(du_num, du_exact, atol=1e-10)
