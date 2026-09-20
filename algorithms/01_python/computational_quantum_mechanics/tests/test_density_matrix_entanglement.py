import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from density_matrix_entanglement import partial_trace_b, von_neumann_entropy

def test_bell_state_entropy():
    # Bell state |Phi+> = (|00> + |11>) / sqrt(2)
    psi = np.array([1.0, 0.0, 0.0, 1.0]) / np.sqrt(2.0)
    rho_ab = np.outer(psi, psi)
    
    rho_a = partial_trace_b(rho_ab, 2, 2)
    # Reduced density matrix is 0.5 * I_2, S(rho_a) = 1 bit
    assert np.allclose(rho_a, 0.5 * np.eye(2))
    entropy = von_neumann_entropy(rho_a)
    assert np.isclose(entropy, 1.0)
