import numpy as np
from quantum_density_matrix import density_matrix_purity, von_neumann_entropy


def test_pure_vs_mixed():
    rho_pure = np.array([[1.0, 0.0], [0.0, 0.0]])
    assert np.isclose(density_matrix_purity(rho_pure), 1.0)
    assert np.isclose(von_neumann_entropy(rho_pure), 0.0)
    rho_mixed = np.array([[0.5, 0.0], [0.0, 0.5]])
    assert np.isclose(density_matrix_purity(rho_mixed), 0.5)
    assert np.isclose(von_neumann_entropy(rho_mixed), np.log(2.0))
