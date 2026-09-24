import numpy as np
from helmholtz_green_function_boundary import helmholtz_2d_green_function


def test_helmholtz():
    r = np.array([1.0, 2.0])
    G = helmholtz_2d_green_function(r, k=2.0)
    assert len(G) == 2
    assert not np.any(np.isnan(G))
