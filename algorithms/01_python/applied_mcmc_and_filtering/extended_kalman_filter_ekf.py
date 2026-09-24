"""Extended Kalman Filter (EKF) First-Order Nonlinear Measurement Update."""
import numpy as np


def ekf_update(x_prior: np.ndarray, P_prior: np.ndarray, z: np.ndarray,
               h_fn, H_jacobian: np.ndarray, R: np.ndarray) -> tuple:
    """Perform EKF measurement update."""
    y = z - h_fn(x_prior)
    S = H_jacobian @ P_prior @ H_jacobian.T + R
    K = P_prior @ H_jacobian.T @ np.linalg.inv(S)
    x_post = x_prior + K @ y
    P_post = (np.eye(len(x_prior)) - K @ H_jacobian) @ P_prior
    return x_post, P_post
