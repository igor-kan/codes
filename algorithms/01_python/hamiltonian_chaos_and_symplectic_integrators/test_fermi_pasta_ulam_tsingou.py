import numpy as np
from fermi_pasta_ulam_tsingou import fput_forces, normal_mode_energies


def test_fput_linear_modes():
    # Linear lattice (alpha = 0)
    n = 8
    q = np.sin(np.arange(1, n + 1) * np.pi / (n + 1))
    p = np.zeros(n)
    E_k = normal_mode_energies(q, p)
    # Mode 1 holds virtually all energy
    assert E_k[0] > 0.99 * np.sum(E_k)
