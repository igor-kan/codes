import numpy as np
from black_scholes_pde_solver import black_scholes_call_analytic, black_scholes_fdm_call


def test_call_pricing():
    S0, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.2
    c_analytic = black_scholes_call_analytic(S0, K, T, r, sigma)
    c_fdm = black_scholes_fdm_call(S0, K, T, r, sigma, M=150, N=500, Smax=300.0)
    assert np.isclose(c_fdm, c_analytic, rtol=0.03)
