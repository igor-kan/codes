"""
Cartan's structural equations for orthonormal tetrad and spin connection.
Reference: Penrose, The Road to Reality, Ch. 14.
"""
import numpy as np

def cartan_torsion(d_tetrad: np.ndarray, spin_conn: np.ndarray, tetrad: np.ndarray) -> np.ndarray:
    """
    First structural equation: T^a = d e^a + omega^a_b wedge e^b.
    For torsion-free Levi-Civita connection, T^a = 0.
    """
    # Wedge product contraction
    T = d_tetrad + np.einsum('abc,c->ab', spin_conn, tetrad)
    return T
