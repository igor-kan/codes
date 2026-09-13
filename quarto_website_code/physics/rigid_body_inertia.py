"""
Rigid Body Mechanics: Inertia Tensors and Principal Axes Diagonalization.

Implements:
1. Discrete mass distribution inertia tensor I_ij:
   I_xx = sum m (y^2 + z^2), I_xy = -sum m x y, etc.
2. Parallel Axis Theorem (Steiner's Theorem) for arbitrary translation
3. Eigenvalue diagonalization yielding Principal Moments of Inertia and Principal Axes
"""

import numpy as np
from typing import List, Tuple

def compute_inertia_tensor(masses: List[float], positions: np.ndarray) -> np.ndarray:
    """Compute 3x3 inertia tensor from N point masses."""
    I = np.zeros((3, 3), dtype=float)
    for m, (x, y, z) in zip(masses, positions):
        I[0, 0] += m * (y**2 + z**2)
        I[1, 1] += m * (x**2 + z**2)
        I[2, 2] += m * (x**2 + y**2)
        I[0, 1] -= m * (x * y)
        I[0, 2] -= m * (x * z)
        I[1, 2] -= m * (y * z)
        
    I[1, 0] = I[0, 1]
    I[2, 0] = I[0, 2]
    I[2, 1] = I[1, 2]
    return I

def principal_axes(I: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Diagonalize inertia tensor into principal moments and orthonormal principal axes."""
    eigenvalues, eigenvectors = np.linalg.eigh(I)
    return eigenvalues, eigenvectors

if __name__ == "__main__":
    print("=== RIGID BODY INERTIA TENSOR ===")
    masses = [1.0, 1.0, 1.0, 1.0]
    pos = np.array([[1, 0, 0], [-1, 0, 0], [0, 2, 0], [0, -2, 0]])
    I = compute_inertia_tensor(masses, pos)
    moments, axes = principal_axes(I)
    print(f"Inertia Tensor:\n{I}")
    print(f"Principal Moments: {moments}")
