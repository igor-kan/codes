"""
Rayleigh-Ritz Variational Method for Quantum Hamiltonians.
References: Landau & Lifshitz - Quantum Mechanics (Vol. 3, Ch. 3).
"""
import numpy as np

def solve_variational_1d(h_diag, v_matrix_func, n_basis=10):
    """
    Solve H |psi> = E |psi> using an orthonormal basis |n>.
    h_diag: diagonal unperturbed energies H0_nn
    v_matrix_func: function(i, j) returning <i|V|j> matrix element
    """
    H = np.diag(h_diag[:n_basis])
    for i in range(n_basis):
        for j in range(n_basis):
            H[i, j] += v_matrix_func(i, j)
            
    eigvals, eigvecs = np.linalg.eigh(H)
    return eigvals, eigvecs
