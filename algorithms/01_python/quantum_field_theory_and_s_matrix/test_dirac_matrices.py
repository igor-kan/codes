import numpy as np
from dirac_matrices import get_dirac_pauli_matrices, get_weyl_matrices, verify_clifford_algebra


def test_dirac_pauli_algebra():
    gammas = get_dirac_pauli_matrices()
    assert verify_clifford_algebra(gammas)
    # gamma5^2 = I
    assert np.allclose(gammas["g5"] @ gammas["g5"], np.eye(4, dtype=complex))


def test_weyl_algebra():
    gammas = get_weyl_matrices()
    assert verify_clifford_algebra(gammas)
    # In Weyl representation, gamma5 is diagonal diag(-I, +I)
    assert np.allclose(gammas["g5"][:2, :2], -np.eye(2, dtype=complex))
    assert np.allclose(gammas["g5"][2:, 2:], np.eye(2, dtype=complex))
