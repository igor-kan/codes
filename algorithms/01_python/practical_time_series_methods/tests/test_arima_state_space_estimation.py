import numpy as np
from arima_state_space_estimation import ar1_recursive_forecast


def test_ar1_forecast():
    x = np.array([1.0, 2.0, 4.0])
    fc = ar1_recursive_forecast(x, phi=0.5, n_ahead=3)
    assert np.allclose(fc, [2.0, 1.0, 0.5])
