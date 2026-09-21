import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from schwarzschild_penrose_diagram import kruskal_to_penrose

def test_penrose_bounded():
    # As Kruskal coords -> infty, Penrose coords must remain bounded within [-pi, pi]
    psi, xi = kruskal_to_penrose(1e6, 1e6)
    assert -np.pi <= psi <= np.pi
    assert -np.pi <= xi <= np.pi
