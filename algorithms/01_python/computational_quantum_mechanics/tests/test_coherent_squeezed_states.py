import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from coherent_squeezed_states import coherent_state_fock, quadrature_variances

def test_coherent_state_poisson():
    alpha = 2.0
    c = coherent_state_fock(alpha, n_max=40)
    probs = np.abs(c)**2
    mean_n = np.sum(np.arange(len(probs)) * probs)
    # Mean photon number is |alpha|^2 = 4.0
    assert np.isclose(mean_n, 4.0, atol=1e-3)
