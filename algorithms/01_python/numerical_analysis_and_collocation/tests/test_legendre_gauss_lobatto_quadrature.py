import numpy as np
from legendre_gauss_lobatto_quadrature import lgl_nodes_weights


def test_lgl_exact_polynomial():
    x, w = lgl_nodes_weights(4)
    # Exact integral of x^6 over [-1, 1] is 2/7
    poly = x**6
    integral = np.sum(w * poly)
    assert np.isclose(integral, 2.0 / 7.0, atol=1e-12)
