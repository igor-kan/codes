import numpy as np
from vortex_sheet_birkhoff_rott import vortex_sheet_velocity


def test_vortex_sheet():
    # 2 symmetric opposite vortices
    z = np.array([-1.0 + 0.0j, 1.0 + 0.0j])
    gammas = np.array([1.0, -1.0])
    vel = vortex_sheet_velocity(z, gammas, delta=0.1)

    # By symmetry, vertical velocity is equal for both (self-propelling dipoles)
    assert np.isclose(vel[0].imag, vel[1].imag)
