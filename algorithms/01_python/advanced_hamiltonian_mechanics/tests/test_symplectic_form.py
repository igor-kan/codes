import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from symplectic_form import standard_symplectic_matrix, is_symplectic_matrix, evaluate_symplectic_form

def test_j_matrix_symplectic():
    J = standard_symplectic_matrix(2)
    assert is_symplectic_matrix(J)
    # Anti-symmetry: omega(v, v) = 0
    v = np.array([1.0, 2.0, 3.0, 4.0])
    assert np.isclose(evaluate_symplectic_form(v, v), 0.0)
