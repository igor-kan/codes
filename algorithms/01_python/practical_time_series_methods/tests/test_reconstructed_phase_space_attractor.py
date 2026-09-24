import numpy as np
from reconstructed_phase_space_attractor import time_delay_embedding


def test_embedding():
    x = np.sin(np.linspace(0, 10, 100))
    Y = time_delay_embedding(x, delay=5, dimension=3)
    assert Y.shape == (90, 3)
