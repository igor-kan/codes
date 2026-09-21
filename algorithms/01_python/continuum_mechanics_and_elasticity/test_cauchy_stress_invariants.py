import numpy as np
from cauchy_stress_invariants import stress_invariants, principal_stresses, deviatoric_stress


def test_hydrostatic_stress():
    p = 10.0
    sigma = -p * np.eye(3)
    inv = stress_invariants(sigma)
    assert np.isclose(inv["I1"], -30.0)

    s, J2, J3 = deviatoric_stress(sigma)
    assert np.allclose(s, np.zeros((3, 3)))
    assert np.isclose(J2, 0.0)
    assert np.isclose(J3, 0.0)


def test_pure_shear():
    tau = 5.0
    sigma = np.array([[0, tau, 0], [tau, 0, 0], [0, 0, 0]], dtype=float)
    s1, s2, s3 = principal_stresses(sigma)
    assert np.isclose(s1, tau)
    assert np.isclose(s2, 0.0)
    assert np.isclose(s3, -tau)
