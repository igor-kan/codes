import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tight_binding_lattice import tight_binding_1d_hamiltonian, tight_binding_1d_dispersion

def test_tight_binding_eigenvalues():
    N = 10
    t = 1.0
    H = tight_binding_1d_hamiltonian(N, t=t, periodic=True)
    eigvals = np.sort(np.linalg.eigvalsh(H))
    
    # Analytical: -2 t cos(2 pi j / N)
    j = np.arange(N)
    k = 2.0 * np.pi * j / N
    expected = np.sort(tight_binding_1d_dispersion(k, t=t))
    assert np.allclose(eigvals, expected, atol=1e-10)
