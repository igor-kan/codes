import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from two_spinor_formalism import spinor_inner_product, spinor_to_null_vector

def test_spinor_antisymmetry():
    k = np.array([1.0 + 2.0j, -0.5 + 1.0j])
    eta = np.array([0.2 - 0.1j, 3.0 + 0.0j])
    s1 = spinor_inner_product(k, eta)
    s2 = spinor_inner_product(eta, k)
    assert np.isclose(s1, -s2)
    assert np.isclose(spinor_inner_product(k, k), 0.0)

def test_null_vector_norm():
    # A vector formed from a spinor must be null: (v^0)^2 - (v^1)^2 - (v^2)^2 - (v^3)^2 = 0
    k = np.array([1.0 + 1.0j, 2.0 - 0.5j])
    v = spinor_to_null_vector(k)
    minkowski_norm = v[0]**2 - (v[1]**2 + v[2]**2 + v[3]**2)
    assert np.isclose(minkowski_norm, 0.0, atol=1e-12)
