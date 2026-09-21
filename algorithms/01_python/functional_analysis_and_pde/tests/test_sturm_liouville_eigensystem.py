import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sturm_liouville_eigensystem import sturm_liouville_fd_eigenvalues

def test_particle_in_a_box_eigenvalues():
    # -y'' = lambda y with y(0)=y(1)=0 -> lambda_n = (n pi)^2
    p = lambda x: 1.0
    q = lambda x: 0.0
    w = lambda x: 1.0
    eigs = sturm_liouville_fd_eigenvalues(p, q, w, x_span=(0.0, 1.0), n_pts=300, n_eigs=3)
    expected = [(n * np.pi)**2 for n in range(1, 4)]
    assert np.allclose(eigs, expected, rtol=1e-2)
