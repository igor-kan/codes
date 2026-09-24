import numpy as np
from chebyshev_spectral_differentiation import chebyshev_nodes, chebyshev_differentiation_matrix


def test_chebyshev_derivative():
    N = 16
    x = chebyshev_nodes(N)
    D = chebyshev_differentiation_matrix(N)
    # Derivative of f(x) = exp(x) is exp(x)
    f = np.exp(x)
    df_exact = np.exp(x)
    df_num = D @ f
    assert np.allclose(df_num, df_exact, atol=1e-8)
