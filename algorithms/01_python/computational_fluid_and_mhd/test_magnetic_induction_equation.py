import numpy as np
from magnetic_induction_equation import magnetic_reynolds_number, magnetic_diffusion_time, simulate_magnetic_diffusion_1d


def test_magnetic_diffusion():
    L = 1.0
    eta = 0.05
    assert magnetic_reynolds_number(10.0, L, eta) == 200.0
    assert magnetic_diffusion_time(L, eta) == 20.0

    # Test diffusion decay
    nx = 51
    dx = L / (nx - 1)
    dt = 0.4 * (dx**2) / eta
    x = np.linspace(0, L, nx)
    B_init = np.sin(np.pi * x)
    B_final = simulate_magnetic_diffusion_1d(B_init, dx, dt, eta, 50)
    assert np.all(B_final <= B_init + 1e-12)
    assert np.max(B_final) < np.max(B_init)
