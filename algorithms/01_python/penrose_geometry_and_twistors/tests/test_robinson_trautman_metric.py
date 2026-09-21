import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from robinson_trautman_metric import robinson_trautman_laplacian

def test_rt_curvature():
    # For a round sphere, K is a positive constant
    P = 1.0
    dP = 0.0
    d2P = 0.5 + 0.0j
    K = robinson_trautman_laplacian(P, dP, d2P)
    assert K > 0.0
