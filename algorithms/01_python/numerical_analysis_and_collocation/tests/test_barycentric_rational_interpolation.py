import numpy as np
from barycentric_rational_interpolation import floater_hormann_interpolate


def test_rational_interp():
    x_nodes = np.linspace(-1, 1, 11)
    y_nodes = 1.0 / (1.0 + 25.0 * x_nodes**2)  # Runge function
    x_test = np.linspace(-1, 1, 50)
    y_interp = floater_hormann_interpolate(x_nodes, y_nodes, x_test, d=3)
    assert len(y_interp) == 50
    assert not np.any(np.isnan(y_interp))
