import numpy as np
from garch_volatility_forecasting import garch11_filter


def test_garch_variance():
    returns = np.random.normal(0, 0.01, 1000)
    omega, alpha, beta = 1e-5, 0.1, 0.8
    sigma2 = garch11_filter(returns, omega, alpha, beta)
    assert len(sigma2) == 1000
    assert np.all(sigma2 > 0)
    uncond_var = omega / (1.0 - alpha - beta)
    assert np.isclose(np.mean(sigma2), uncond_var, rtol=0.3)
