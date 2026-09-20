import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sturm_liouville import SturmLiouvilleSolver

def test_particle_in_a_box():
    # -y'' = lambda y on [0, pi] -> lambda_n = n^2 = 1, 4, 9, 16...
    solver = SturmLiouvilleSolver(
        p_func=lambda x: np.ones_like(x),
        q_func=lambda x: np.zeros_like(x),
        w_func=lambda x: np.ones_like(x),
        a=0.0, b=np.pi, n_points=300
    )
    eigvals, eigfuncs = solver.solve_dirichlet(num_eigenvalues=3)
    assert np.isclose(eigvals[0], 1.0, atol=0.05)
    assert np.isclose(eigvals[1], 4.0, atol=0.1)
    assert np.isclose(eigvals[2], 9.0, atol=0.25)
