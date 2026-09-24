import numpy as np
from pauli_spin_matrices import SIGMA_X, SIGMA_Y, SIGMA_Z, larmor_spin_precession


def test_pauli_algebra():
    comm = SIGMA_X @ SIGMA_Y - SIGMA_Y @ SIGMA_X
    assert np.allclose(comm, 2j * SIGMA_Z)
    psi_x = np.array([1.0, 1.0]) / np.sqrt(2.0)
    psi_t = larmor_spin_precession(psi_x, B0=1.0, gyromagnetic_ratio=np.pi, t=1.0)
    assert np.isclose(np.sum(np.abs(psi_t)**2), 1.0)
