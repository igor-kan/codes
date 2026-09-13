"""
Comprehensive Test Suite for Multilinear Algebra and Tensor Theory
Validates:
- Duality pairing vs row-column matrix multiplication
- Rank-1 outer products
- Transpose as adjoint / dual map: <T* omega, v> == <omega, T v>
- Symmetric-Antisymmetric canonical decomposition
- Fundamental Orthogonality Theorem: S_{ij} A^{ij} == 0
- Quadratic form invariance under antisymmetry: x^T T x == x^T S x
- 2D-by-vector, 2D-by-2D single and double contractions
- 4th-order elasticity tensor contractions
- Spectral decomposition, SVD, and Polar decomposition
- Sylvester's criterion, Cholesky factorization, and definiteness classification
- 3rd-order tensor HOSVD (Tucker decomposition) mode unfolding
"""

import numpy as np
import scipy.linalg as la
# import pytest optional


def test_duality_pairing_and_outer_product():
    v = np.array([3.0, -1.0, 4.0])
    omega = np.array([2.0, 5.0, -2.0])

    # Contraction: omega_i v^i
    pairing_scalar = np.dot(omega, v)
    assert np.isclose(pairing_scalar, -7.0)

    # Outer product: v^i omega_j
    outer = np.outer(v, omega)
    assert outer.shape == (3, 3)
    assert np.linalg.matrix_rank(outer) == 1
    # Check operator action: (v ⊗ omega) x == v * <omega, x>
    x = np.array([1.0, 2.0, 3.0])
    action_1 = outer @ x
    action_2 = v * np.dot(omega, x)
    assert np.allclose(action_1, action_2)


def test_transpose_as_dual_map():
    # <T* omega, v> == <omega, T v>
    np.random.seed(101)
    T = np.random.randn(4, 3)  # T: R^3 -> R^4
    v = np.random.randn(3)     # v in R^3
    omega = np.random.randn(4) # omega in (R^4)*

    Tv = T @ v                 # in R^4
    omega_Tv = np.dot(omega, Tv) # <omega, T v>

    T_star_omega = T.T @ omega # in (R^3)*
    T_star_omega_v = np.dot(T_star_omega, v) # <T* omega, v>

    assert np.isclose(omega_Tv, T_star_omega_v)


def test_symmetric_antisymmetric_decomposition_and_orthogonality():
    np.random.seed(202)
    for n in [3, 4, 5]:
        T = np.random.randn(n, n)
        S = 0.5 * (T + T.T)
        A = 0.5 * (T - T.T)

        # Exact decomposition
        assert np.allclose(T, S + A)
        # S is symmetric, A is antisymmetric
        assert np.allclose(S, S.T)
        assert np.allclose(A, -A.T)
        # Diagonal of A must be zero
        assert np.allclose(np.diag(A), 0.0)

        # Orthogonality Theorem: S_{ij} A^{ij} == 0
        double_contraction = np.sum(S * A)
        assert np.isclose(double_contraction, 0.0, atol=1e-14)


def test_quadratic_form_antisymmetric_nullity():
    np.random.seed(303)
    T = np.random.randn(4, 4)
    S = 0.5 * (T + T.T)
    A = 0.5 * (T - T.T)

    for _ in range(5):
        x = np.random.randn(4)
        q_full = x.T @ T @ x
        q_sym = x.T @ S @ x
        q_anti = x.T @ A @ x

        assert np.isclose(q_anti, 0.0, atol=1e-14)
        assert np.isclose(q_full, q_sym)


def test_tensor_contractions_einsum():
    np.random.seed(404)
    A = np.random.randn(3, 3)
    B = np.random.randn(3, 3)
    v = np.random.randn(3)

    # 2D by vector: A^i_j v^j
    assert np.allclose(np.einsum('ij,j->i', A, v), A @ v)

    # 2D by 2D single contraction (matrix multiplication): A^i_j B^j_k
    assert np.allclose(np.einsum('ij,jk->ik', A, B), A @ B)

    # 2D by 2D double contraction (Frobenius): A_{ij} B^{ij} == Tr(A B^T)
    frob_einsum = np.einsum('ij,ij->', A, B)
    frob_trace = np.trace(A @ B.T)
    assert np.isclose(frob_einsum, frob_trace)


def test_fourth_order_elasticity_contractions():
    # Hooke's Law: sigma_{ij} = C_{ijkl} epsilon_{kl}
    # Isotropic elasticity tensor: C_{ijkl} = lambda delta_{ij} delta_{kl} + mu (delta_{ik} delta_{jl} + delta_{il} delta_{jk})
    lam = 1.5
    mu = 2.5
    delta = np.eye(3)
    
    C = np.zeros((3, 3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    C[i, j, k, l] = lam * delta[i, j] * delta[k, l] + mu * (delta[i, k] * delta[j, l] + delta[i, l] * delta[j, k])

    # Symmetries of C: minor and major
    assert np.allclose(C, np.transpose(C, (1, 0, 2, 3))) # C_{jikl} = C_{ijkl}
    assert np.allclose(C, np.transpose(C, (0, 1, 3, 2))) # C_{ijlk} = C_{ijkl}
    assert np.allclose(C, np.transpose(C, (2, 3, 0, 1))) # C_{klij} = C_{ijkl}

    # Contract with symmetric strain tensor
    eps_sym = np.array([[1.0, 0.2, -0.1], [0.2, 0.5, 0.0], [-0.1, 0.0, -0.4]])
    sigma = np.einsum('ijkl,kl->ij', C, eps_sym)
    # sigma must be symmetric
    assert np.allclose(sigma, sigma.T)


def test_matrix_decompositions():
    np.random.seed(505)
    # 1. Spectral Theorem
    M = np.random.randn(3, 3)
    S = M + M.T
    eigenvals, Q = np.linalg.eigh(S)
    assert np.allclose(Q @ np.diag(eigenvals) @ Q.T, S)
    assert np.allclose(Q.T @ Q, np.eye(3))

    # 2. SVD
    X = np.random.randn(4, 3)
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    assert np.allclose(U @ np.diag(s) @ Vt, X)

    # 3. Polar Decomposition: X_sq = R @ P
    X_sq = np.random.randn(3, 3)
    R, P = la.polar(X_sq)
    assert np.allclose(R.T @ R, np.eye(3))
    assert np.allclose(P, P.T)
    assert np.all(np.linalg.eigvalsh(P) >= 0)
    assert np.allclose(X_sq, R @ P)


def test_sylvester_criterion_and_cholesky():
    # Construct a known positive definite matrix
    np.random.seed(606)
    B = np.random.randn(4, 4)
    A_pd = B.T @ B + 0.5 * np.eye(4)

    # Check eigenvalues > 0
    eigvals = np.linalg.eigvalsh(A_pd)
    assert np.all(eigvals > 0)

    # Sylvester's Criterion: all leading principal minors > 0
    for k in range(1, 5):
        minor = np.linalg.det(A_pd[:k, :k])
        assert minor > 0

    # Cholesky decomposition exists
    L = np.linalg.cholesky(A_pd)
    assert np.allclose(L @ L.T, A_pd)
    assert np.all(np.diag(L) > 0)


def test_hosvd_tucker_3rd_order():
    # Construct 3rd order tensor (3 x 4 x 5)
    np.random.seed(707)
    T = np.random.randn(3, 4, 5)

    # Unfoldings (matricizations)
    T_1 = T.reshape(3, -1)
    T_2 = np.transpose(T, (1, 0, 2)).reshape(4, -1)
    T_3 = np.transpose(T, (2, 0, 1)).reshape(5, -1)

    # Factor matrices from SVD of unfoldings
    U1, _, _ = np.linalg.svd(T_1, full_matrices=False)
    U2, _, _ = np.linalg.svd(T_2, full_matrices=False)
    U3, _, _ = np.linalg.svd(T_3, full_matrices=False)

    # Core tensor: G = T x_1 U1^T x_2 U2^T x_3 U3^T
    G = np.einsum('ijk,ia,jb,kc->abc', T, U1, U2, U3)

    # Reconstruction: T_recon = G x_1 U1 x_2 U2 x_3 U3
    T_recon = np.einsum('abc,ia,jb,kc->ijk', G, U1, U2, U3)
    assert np.allclose(T, T_recon)


if __name__ == "__main__":
    test_duality_pairing_and_outer_product()
    test_transpose_as_dual_map()
    test_symmetric_antisymmetric_decomposition_and_orthogonality()
    test_quadratic_form_antisymmetric_nullity()
    test_tensor_contractions_einsum()
    test_fourth_order_elasticity_contractions()
    test_matrix_decompositions()
    test_sylvester_criterion_and_cholesky()
    test_hosvd_tucker_3rd_order()
    print("All 9 multilinear algebra and tensor validation tests passed successfully!")
