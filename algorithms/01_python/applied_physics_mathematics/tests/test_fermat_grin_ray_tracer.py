import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fermat_grin_ray_tracer import trace_ray_grin

def test_straight_ray_in_uniform_medium():
    n_func = lambda x, y: 1.5
    grad_n_func = lambda x, y: (0.0, 0.0)
    traj = trace_ray_grin(n_func, grad_n_func, (0.0, 0.0), 0.0, steps=10, ds=0.1)
    # y must remain 0
    assert np.allclose(traj[:, 1], 0.0)
