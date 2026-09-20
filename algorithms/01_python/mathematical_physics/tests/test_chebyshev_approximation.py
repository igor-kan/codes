import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from chebyshev_approximation import ChebyshevApproximation

def test_chebyshev_exp():
    approx = ChebyshevApproximation(np.exp, -1.0, 1.0, n_terms=12)
    x = np.linspace(-1, 1, 100)
    y_approx = approx.evaluate(x)
    y_exact = np.exp(x)
    assert np.allclose(y_approx, y_exact, atol=1e-10)
