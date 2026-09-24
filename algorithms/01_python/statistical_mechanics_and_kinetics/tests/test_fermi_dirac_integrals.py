import numpy as np
from fermi_dirac_integrals import fermi_dirac_occupancy, sommerfeld_chemical_potential


def test_fermi():
    E = np.array([0.5, 1.0, 1.5])
    f = fermi_dirac_occupancy(E, mu=1.0, T=0.1)
    assert f[1] == 0.5
    assert f[0] > 0.5 > f[2]
