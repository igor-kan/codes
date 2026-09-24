import numpy as np
from gauss_newton_marquardt_fitting import levenberg_marquardt_fit


def test_lm_fit():
    # Fit y = a * x + b
    x_data = np.array([1.0, 2.0, 3.0, 4.0])
    y_data = np.array([3.0, 5.0, 7.0, 9.0])
    
    def r(p):
        return (p[0] * x_data + p[1]) - y_data
    def J(p):
        return np.column_stack([x_data, np.ones_like(x_data)])
        
    p_opt = levenberg_marquardt_fit(r, J, np.array([0.0, 0.0]))
    assert np.allclose(p_opt, [2.0, 1.0], atol=1e-4)
