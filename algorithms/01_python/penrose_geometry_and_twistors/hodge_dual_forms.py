"""
Hodge Star Dual operator in 4D Minkowski spacetime.
Reference: Penrose, The Road to Reality, Ch. 19.
"""
import numpy as np

def hodge_dual_2form_minkowski(F: np.ndarray) -> np.ndarray:
    """
    Calculates *F_{ab} = (1/2) epsilon_{abcd} F^{cd} for antisymmetric 2-form F (e.g. Faraday tensor).
    Metric convention: (-1, +1, +1, +1).
    """
    star_F = np.zeros((4, 4), dtype=float)
    # Standard electric/magnetic duality: E -> B, B -> -E
    # F_{0i} = -E_i, F_{ij} = eps_{ijk} B_k
    # *F_{0i} = -B_i, *F_{ij} = -eps_{ijk} E_k
    E = -F[0, 1:]
    B = np.array([F[2, 3], F[3, 1], F[1, 2]])
    
    # *F has E replaced by B, and B replaced by -E
    star_E = B
    star_B = -E
    
    star_F[0, 1:] = -star_E
    star_F[1:, 0] = star_E
    star_F[2, 3] = star_B[0]; star_F[3, 2] = -star_B[0]
    star_F[3, 1] = star_B[1]; star_F[1, 3] = -star_B[1]
    star_F[1, 2] = star_B[2]; star_F[2, 1] = -star_B[2]
    
    return star_F
