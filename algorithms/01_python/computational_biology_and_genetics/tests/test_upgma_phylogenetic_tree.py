import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from upgma_phylogenetic_tree import upgma_step

def test_upgma_step():
    D = np.array([
        [0.0, 2.0, 4.0],
        [2.0, 0.0, 4.0],
        [4.0, 4.0, 0.0]
    ])
    clusters = [[0], [1], [2]]
    D_new, new_c, pair, dist = upgma_step(D, clusters)
    assert pair == (0, 1)
    assert dist == 2.0
    assert len(new_c) == 2
