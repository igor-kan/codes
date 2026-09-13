"""
Multilinear Algebra, Tensor Contractions, and Decompositions.

Implements:
1. Dual space pairing & musical isomorphisms (raising/lowering indices via metric g_ij)
2. Tensor outer product (a (x) b)
3. Einstein summation and double Frobenius contraction (A : B = Tr(A^T B))
4. Sylvester's criterion for positive definiteness via leading principal minors
5. Eckart-Young-Mirsky low-rank SVD approximation
6. Higher-order Tucker HOSVD decomposition for 3D tensors
"""

import numpy as np
from typing import Tuple, List

def dual_pairing(alpha: np.ndarray, v: np.ndarray) -> float:
    """Natural bilinear pairing <alpha, v> between dual vector alpha in V* and v in V."""
    return float(np.dot(alpha, v))

def musical_lower(v: np.ndarray, g: np.ndarray) -> np.ndarray:
    """Flat operator (v^b)_i = g_ij v^j."""
    return np.dot(g, v)

def musical_raise(alpha: np.ndarray, g_inv: np.ndarray) -> np.ndarray:
    """Sharp operator (alpha^#)^i = g^(ij) alpha_j."""
    return np.dot(g_inv, alpha)

def tensor_outer_product(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Rank-1 tensor product T_ij = u_i * v_j."""
    return np.outer(u, v)

def frobenius_contraction(A: np.ndarray, B: np.ndarray) -> float:
    """Double contraction A : B = sum_ij A_ij * B_ij = Tr(A^T B)."""
    return float(np.tensordot(A, B, axes=((0, 1), (0, 1))))

def sylvester_criterion(A: np.ndarray) -> Tuple[bool, List[float]]:
    """Test positive definiteness via leading principal minors."""
    n = A.shape[0]
    minors = []
    is_pd = True
    for k in range(1, n + 1):
        sub = A[:k, :k]
        det_k = float(np.linalg.det(sub))
        minors.append(det_k)
        if det_k <= 0:
            is_pd = False
    return is_pd, minors

def eckart_young_svd(A: np.ndarray, rank_k: int) -> Tuple[np.ndarray, float]:
    """Best rank-k approximation under Frobenius and spectral norms."""
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    Uk = U[:, :rank_k]
    Sk = S[:rank_k]
    Vtk = Vt[:rank_k, :]
    Ak = Uk @ np.diag(Sk) @ Vtk
    error = float(np.linalg.norm(A - Ak, ord="fro"))
    return Ak, error

def hosvd_tucker(T: np.ndarray, ranks: Tuple[int, int, int]) -> Tuple[np.ndarray, List[np.ndarray]]:
    """Higher-Order SVD (HOSVD) decomposing 3D tensor into core and factor matrices."""
    # Unfold along mode 0, 1, 2
    U_factors = []
    for mode in range(3):
        # Transpose mode to front and reshape
        unfolded = np.rollaxis(T, mode, 0).reshape(T.shape[mode], -1)
        U, _, _ = np.linalg.svd(unfolded, full_matrices=False)
        U_factors.append(U[:, :ranks[mode]])
        
    # Compute core tensor: G = T x_1 U1^T x_2 U2^T x_3 U3^T
    core = T.copy()
    for mode in range(3):
        core = np.tensordot(core, U_factors[mode], axes=(0, 0))
    return core, U_factors

if __name__ == "__main__":
    print("=== MULTILINEAR ALGEBRA LABORATORY ===")
    A = np.array([[4, 2, 1], [2, 5, 3], [1, 3, 6]], dtype=float)
    is_pd, minors = sylvester_criterion(A)
    print(f"Matrix A positive definite: {is_pd}, Leading minors: {minors}")
    
    B = np.random.randn(10, 8)
    B_rank3, err = eckart_young_svd(B, 3)
    print(f"Eckart-Young Rank-3 Approximation Frobenius Error: {err:.4f}")
