import numpy as np
from potts_model_cluster_wolff import wolff_potts_step


def test_wolff():
    lattice = np.zeros((8, 8), dtype=int)
    lattice = wolff_potts_step(lattice, q=3, beta=2.0)
    assert lattice.shape == (8, 8)
