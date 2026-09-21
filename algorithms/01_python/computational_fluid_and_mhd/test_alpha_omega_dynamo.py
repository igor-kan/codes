import numpy as np
from alpha_omega_dynamo import dynamo_number, dynamo_wave_dispersion


def test_dynamo():
    D = dynamo_number(alpha_0=1.0, delta_omega=1e-6, R=7e8, eta=1e8)
    assert D > 0

    growth, freq = dynamo_wave_dispersion(k=1e-8, alpha_0=10.0, d_omega=1e-5, eta=1e6)
    assert freq > 0
