import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from frobenius_integrability import frobenius_involutive_check

def test_frobenius_subspace():
    # 2D plane in R^3 spanned by e1, e2
    basis = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
    # Commutator in span
    comm = np.array([0.5, -0.2, 0.0])
    assert frobenius_involutive_check(comm, basis)
    
    # Commutator out of span (has z-component)
    comm_out = np.array([0.0, 0.0, 1.0])
    assert not frobenius_involutive_check(comm_out, basis)
