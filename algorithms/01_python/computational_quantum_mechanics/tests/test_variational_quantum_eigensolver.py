import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from variational_quantum_eigensolver import solve_variational_1d

def test_anharmonic_oscillator_perturbation():
    # H = (n + 0.5) + lambda x^4
    # First order perturbation for ground state: E0 approx 0.5 + 3/4 lambda
    lam = 0.05
    n_basis = 8
    h0 = np.arange(n_basis) + 0.5
    
    # <0|x^4|0> = 3/4
    def v_elem(i, j):
        if i == 0 and j == 0:
            return lam * 0.75
        return 0.0

    eigvals, _ = solve_variational_1d(h0, v_elem, n_basis=n_basis)
    assert np.isclose(eigvals[0], 0.5 + lam * 0.75)
