import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from neighbor_joining_tree import compute_q_matrix, find_nj_pair

def test_q_matrix_symmetry():
    D = np.array([
        [0.0, 5.0, 9.0, 9.0],
        [5.0, 0.0, 10.0, 10.0],
        [9.0, 10.0, 0.0, 8.0],
        [9.0, 10.0, 8.0, 0.0]
    ])
    Q = compute_q_matrix(D)
    assert np.allclose(Q, Q.T)
    pair = find_nj_pair(D)
    assert pair == (0, 1)
