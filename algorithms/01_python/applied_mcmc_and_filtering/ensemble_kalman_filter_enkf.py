"""Ensemble Kalman Filter (EnKF) Analysis Step with Perturbed Observations."""
import numpy as np


def enkf_analysis_step(ensemble: np.ndarray, obs_z: np.ndarray, H_matrix: np.ndarray, R_cov: np.ndarray) -> np.ndarray:
    """EnKF state update across N ensemble members."""
    n_dim, N_ens = ensemble.shape
    ens_mean = np.mean(ensemble, axis=1, keepdims=True)
    A = ensemble - ens_mean
    P = (A @ A.T) / (N_ens - 1)
    
    S = H_matrix @ P @ H_matrix.T + R_cov
    K = P @ H_matrix.T @ np.linalg.inv(S)
    
    # Perturbed observations
    d = np.zeros_like(ensemble)
    for j in range(N_ens):
        pert = np.random.multivariate_normal(np.zeros(len(obs_z)), R_cov)
        d[:, j] = ensemble[:, j] + K @ (obs_z + pert - H_matrix @ ensemble[:, j])
    return d
