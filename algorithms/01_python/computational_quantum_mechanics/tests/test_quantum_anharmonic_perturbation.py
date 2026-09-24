import numpy as np
from quantum_anharmonic_perturbation import anharmonic_ground_energy


def test_anharmonic():
    assert np.isclose(anharmonic_ground_energy(0.0), 0.5)
    assert anharmonic_ground_energy(0.01) > 0.5
