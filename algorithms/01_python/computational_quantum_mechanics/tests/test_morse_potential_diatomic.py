import numpy as np
from morse_potential_diatomic import morse_potential, morse_energy_level


def test_morse():
    De = 10.0
    a = 1.0
    re = 2.0
    V_min = morse_potential(np.array([re]), De, a, re)[0]
    assert np.isclose(V_min, 0.0)
    E0 = morse_energy_level(0, omega0=1.0, D_e=De)
    E1 = morse_energy_level(1, omega0=1.0, D_e=De)
    assert E1 > E0
