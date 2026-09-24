import numpy as np
from gibbs_sampler_linear_regression import gibbs_regression_step


def test_gibbs_step():
    X = np.eye(2)
    y = np.array([1.0, 2.0])
    b = gibbs_regression_step(X, y, sigma2=0.01)
    assert np.allclose(b, [1.0, 2.0], atol=0.5)
