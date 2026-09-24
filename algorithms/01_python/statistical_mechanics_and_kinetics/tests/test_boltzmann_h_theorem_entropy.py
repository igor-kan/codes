import numpy as np
from boltzmann_h_theorem_entropy import boltzmann_h_function


def test_h_theorem():
    v = np.linspace(-5, 5, 501)
    # Maxwellian distribution minimizes H
    f_maxwell = np.exp(-v**2) / np.sqrt(np.pi)
    H_val = boltzmann_h_function(f_maxwell, v)
    assert not np.isnan(H_val)
