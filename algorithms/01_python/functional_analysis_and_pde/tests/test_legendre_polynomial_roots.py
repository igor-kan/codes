import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from legendre_polynomial_roots import gauss_legendre_nodes_weights

def test_gauss_legendre_quadrature():
    nodes, weights = gauss_legendre_nodes_weights(5)
    # Sum of weights must equal interval length 2.0
    assert np.isclose(np.sum(weights), 2.0)
    # Exact integral of x^4 from -1 to 1 is 2/5 = 0.4
    val = np.sum(weights * (nodes**4))
    assert np.isclose(val, 0.4)
