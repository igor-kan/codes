import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from orthogonal_polynomials import legendre_p, associated_legendre_p

def test_legendre_orthogonality():
    x = np.linspace(-1, 1, 1000)
    p0 = legendre_p(0, x)
    p1 = legendre_p(1, x)
    p2 = legendre_p(2, x)
    
    # Exact P_2(x) = 0.5 * (3x^2 - 1)
    assert np.allclose(p2, 0.5 * (3 * x**2 - 1))
    
    # Orthogonality int_{-1}^1 P_0 P_1 dx = 0, int P_1 P_2 dx = 0
    assert np.abs(np.trapezoid(p0 * p1, x)) < 1e-10
    assert np.abs(np.trapezoid(p1 * p2, x)) < 1e-10
    
    # Normalization int_{-1}^1 P_2^2 dx = 2 / (2*2 + 1) = 2/5 = 0.4
    norm2 = np.trapezoid(p2**2, x)
    assert np.isclose(norm2, 0.4, atol=1e-3)

def test_associated_legendre():
    x = np.linspace(-0.99, 0.99, 100)
    # P_1^1(x) = -sqrt(1 - x^2)
    p11 = associated_legendre_p(1, 1, x)
    assert np.allclose(p11, -np.sqrt(1 - x**2))
