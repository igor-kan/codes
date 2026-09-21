"""Poincaré Recurrence Theorem and Discrete Phase Space Recurrence Tracker.

Tracks recurrence of bounded trajectories into an initial epsilon-neighborhood in phase space.
"""
import numpy as np


def find_poincare_recurrence(trajectory: np.ndarray, epsilon: float = 0.05) -> int:
    """Find the first return step k > 0 such that ||traj[k] - traj[0]|| < epsilon.

    Returns -1 if recurrence not observed within trajectory length.
    """
    x0 = trajectory[0]
    for step in range(1, len(trajectory)):
        dist = np.linalg.norm(trajectory[step] - x0)
        if dist < epsilon:
            return step
    return -1
