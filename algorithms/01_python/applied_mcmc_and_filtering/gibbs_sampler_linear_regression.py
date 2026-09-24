"""Gibbs Sampler for Bayesian Gaussian Linear Regression with Conjugate Priors."""
import numpy as np


def gibbs_regression_step(X: np.ndarray, y: np.ndarray, sigma2: float) -> np.ndarray:
    """Sample regression coefficients beta ~ Normal((X^T X)^(-1) X^T y, sigma^2 (X^T X)^(-1))."""
    XtX = X.T @ X
    XtX_inv = np.linalg.inv(XtX)
    beta_hat = XtX_inv @ X.T @ y
    cov = sigma2 * XtX_inv
    return np.random.multivariate_normal(beta_hat, cov)
