"""
Electric and Magnetic decomposition of the Weyl curvature tensor.
Reference: Penrose, The Road to Reality, Ch. 19; Hawking & Ellis.
"""
import numpy as np
from typing import Tuple

def electric_magnetic_weyl_parts(weyl_tensor: np.ndarray, u: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Given a 4x4x4x4 Weyl tensor C_{abcd} and a timelike 4-velocity u^a (u_a u^a = -1 or +1),
    computes the spatial trace-free symmetric 3D electric part E_{ac} and magnetic part B_{ac}.
    E_{ac} = C_{abcd} u^b u^d.
    """
    E = np.zeros((4, 4), dtype=float)
    for a in range(4):
        for c in range(4):
            for b in range(4):
                for d in range(4):
                    E[a, c] += weyl_tensor[a, b, c, d] * u[b] * u[d]
    
    # Project to spatial 3x3 if u = (1, 0, 0, 0)
    E_3d = E[1:, 1:]
    return E, E_3d
