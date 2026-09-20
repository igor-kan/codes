import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cartan_subalgebra_calogero import calogero_lax_matrix, calogero_conserved_quantities

def test_calogero_trace():
    q = np.array([0.0, 1.0])
    p = np.array([2.0, -1.0])
    L = calogero_lax_matrix(q, p)
    invs = calogero_conserved_quantities(L)
    # Tr(L) = p1 + p2 = 1.0
    assert np.isclose(invs[0], 1.0)
