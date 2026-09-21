"""
Petrov algebraic classification of the Weyl tensor via eigenvalues of complex Q matrix.
Reference: Penrose, The Road to Reality, Ch. 22 & 31.
"""
import numpy as np

def classify_petrov_type(eigenvalues: np.ndarray) -> str:
    """
    Classify Petrov type based on multiplicities of the 3 eigenvalues of Q (Tr(Q) = 0):
    - Type I: 3 distinct eigenvalues
    - Type II: 2 equal eigenvalues, 1 distinct (minimal polynomial deg 3)
    - Type D: 2 equal eigenvalues, diagonalizable (degenerate Type I)
    - Type III: 3 equal eigenvalues (all 0), nilpotent order 3
    - Type N: all 0, nilpotent order 2 (radiation / gravitational plane wave)
    - Type O: Q = 0 (conformally flat)
    """
    l1, l2, l3 = np.sort_complex(eigenvalues)
    if np.allclose([l1, l2, l3], 0.0, atol=1e-8):
        return "Type O or N/III"
    
    diff12 = abs(l1 - l2) < 1e-6
    diff23 = abs(l2 - l3) < 1e-6
    diff13 = abs(l1 - l3) < 1e-6
    
    if diff12 and diff23:
        return "Type III or D/II degenerate"
    elif diff12 or diff23 or diff13:
        return "Type D or Type II"
    else:
        return "Type I (General algebraically non-degenerate)"
