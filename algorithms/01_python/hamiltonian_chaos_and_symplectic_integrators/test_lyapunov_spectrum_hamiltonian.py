import numpy as np
from lyapunov_spectrum_hamiltonian import benettin_lyapunov_exponent


def test_regular_zero_lyapunov():
    # For a harmonic oscillator, the motion is regular, so Lyapunov exponent -> 0
    q0 = np.array([1.0])
    p0 = np.array([0.0])
    lam = benettin_lyapunov_exponent(
        q0, p0,
        force_fn=lambda q: -q,
        force_jacobian=lambda q: np.array([[-1.0]]),
        dt=0.01, n_steps=2000, renorm_steps=20
    )
    # Estimated Lyapunov exponent must be close to 0
    assert abs(lam) < 0.05
