"""
Poincare Surface of Section Intersection Detection.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13.
"""
import numpy as np
from typing import List

def find_poincare_intersections(trajectory: np.ndarray, plane_coord_idx: int, plane_val: float) -> np.ndarray:
    """
    Finds crossing points through plane x[plane_coord_idx] = plane_val with positive velocity.
    """
    vals = trajectory[:, plane_coord_idx] - plane_val
    crossings = []
    
    for i in range(len(vals) - 1):
        if vals[i] < 0 and vals[i+1] >= 0:
            # Linear interpolation
            frac = -vals[i] / (vals[i+1] - vals[i])
            pt = trajectory[i] + frac * (trajectory[i+1] - trajectory[i])
            crossings.append(pt)
            
    return np.array(crossings) if crossings else np.empty((0, trajectory.shape[1]))
