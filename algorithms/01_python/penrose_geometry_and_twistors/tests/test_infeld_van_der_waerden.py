import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from infeld_van_der_waerden import four_vector_to_spinor_matrix, spinor_matrix_to_four_vector

def test_isomorphism_roundtrip():
    v = np.array([5.0, 1.2, -2.3, 0.8])
    P = four_vector_to_spinor_matrix(v)
    assert np.allclose(P, P.conj().T)
    v_rec = spinor_matrix_to_four_vector(P)
    assert np.allclose(v, v_rec)

def test_determinant_lorentz_norm():
    v = np.array([4.0, 1.0, 2.0, 1.0])
    # Determinant of P is 0.5 * (v_0^2 - v_1^2 - v_2^2 - v_3^2)
    P = four_vector_to_spinor_matrix(v)
    det_P = np.linalg.det(P).real
    minkowski_sq = 0.5 * (v[0]**2 - np.sum(v[1:]**2))
    assert np.isclose(det_P, minkowski_sq)
