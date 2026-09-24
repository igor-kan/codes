import numpy as np
from wang_landau_density_of_states import wang_landau_update


def test_wang_landau():
    log_dos = np.zeros(5)
    hist = np.zeros(5)
    log_dos, hist = wang_landau_update(log_dos, hist, 2, log_f=1.0)
    assert log_dos[2] == 1.0
    assert hist[2] == 1
