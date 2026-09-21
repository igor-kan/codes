import numpy as np
from grad_shafranov_solver import solovev_poloidal_flux, magnetic_field_components


def test_solovev_flux():
    R0 = 3.0  # Major radius 3m
    kappa = 1.6  # Elongation
    psi_axis = solovev_poloidal_flux(np.array([R0]), np.array([0.0]), R0, kappa)
    assert np.isclose(psi_axis[0], 0.0)

    # At magnetic axis (R0, 0), poloidal field vanishes: B_R = B_Z = 0
    BR, BZ, Bphi = magnetic_field_components(R0, 0.0, R0, kappa)
    assert np.isclose(BR, 0.0)
    assert np.isclose(BZ, 0.0)
    assert np.isclose(Bphi, 2.0)
