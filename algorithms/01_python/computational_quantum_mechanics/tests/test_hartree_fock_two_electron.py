import numpy as np
from hartree_fock_two_electron import helium_scf_energy, optimal_helium_effective_charge


def test_helium_scf():
    zeta_opt = optimal_helium_effective_charge(Z=2.0)
    assert np.isclose(zeta_opt, 1.6875)
    E_min = helium_scf_energy(zeta_opt, Z=2.0)
    assert np.isclose(E_min, -2.84765625)
