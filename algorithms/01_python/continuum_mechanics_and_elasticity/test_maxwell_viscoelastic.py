import numpy as np
from maxwell_viscoelastic import maxwell_stress_relaxation, maxwell_deborah_number


def test_maxwell_relaxation():
    E = 2.0e6
    eta = 1.0e6
    eps_0 = 0.05

    # At t=0, stress is instantaneous Hookean E * eps_0
    sig_0 = maxwell_stress_relaxation(0.0, eps_0, E, eta)
    assert np.isclose(sig_0, E * eps_0)

    # At t -> inf, stress fully relaxes to 0
    sig_inf = maxwell_stress_relaxation(100.0, eps_0, E, eta)
    assert np.isclose(sig_inf, 0.0, atol=1e-6)
