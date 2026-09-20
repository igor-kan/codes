import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gauss_quadrature import integrate_gauss_legendre

def test_gauss_legendre_exact_polynomial():
    # 5-point Gauss-Legendre integrates polynomials of degree up to 2*5 - 1 = 9 exactly
    f = lambda x: x**8 - 3 * x**4 + 2
    # Integral on [-1, 1]: 2/9 - 6/5 + 4 = 2.0/9 - 1.2 + 4.0 = 3.022222...
    val = integrate_gauss_legendre(f, -1.0, 1.0, n=5)
    expected = 2.0 / 9.0 - 6.0 / 5.0 + 4.0
    assert np.isclose(val, expected, atol=1e-12)
