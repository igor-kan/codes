import numpy as np
from saint_venant_torsion import circular_torsion, elliptical_torsion


def test_torsion():
    G = 80.0e9  # Steel shear modulus 80 GPa
    R = 0.05    # 5 cm radius
    T = 5000.0  # 5 kNm

    C_circ, th_circ, tau_circ = circular_torsion(R, G, T)
    C_ell, th_ell, tau_ell = elliptical_torsion(R, R, G, T)

    # Elliptical with a = b = R must match circular exactly
    assert np.isclose(C_circ, C_ell)
    assert np.isclose(th_circ, th_ell)
    assert np.isclose(tau_circ, tau_ell)
