import numpy as np
from navier_stokes_2d_vorticity_streamfunction import solve_streamfunction_poisson_fft


def test_vorticity_stream():
    N = 32
    omega = np.random.randn(N, N)
    omega -= np.mean(omega)  # Zero net circulation
    psi = solve_streamfunction_poisson_fft(omega, 2.0 * np.pi, 2.0 * np.pi)
    assert psi.shape == (N, N)
