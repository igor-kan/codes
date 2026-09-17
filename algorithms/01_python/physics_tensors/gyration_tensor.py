"""Radius of Gyration Tensor S_{mn} in Polymer and Molecular Physics.

Calculates molecular shape descriptors: radius of gyration, asphericity, and acylindricity.
"""

from typing import Sequence, Tuple
import numpy as np


class GyrationTensor:
    """Gyration tensor S_{mn} for polymer conformations."""

    def __init__(self, coordinates: Sequence[Sequence[float]]):
        r = np.array(coordinates, dtype=np.float64)
        if r.ndim != 2 or r.shape[1] != 3:
            raise ValueError("Coordinates must be an N x 3 array")
        n = len(r)
        r_cm = np.mean(r, axis=0)
        dr = r - r_cm
        # S_{mn} = 1/N sum_i dr_{m,i} dr_{n,i}
        self.s = (dr.T @ dr) / n

    @property
    def principal_moments(self) -> np.ndarray:
        """Eigenvalues sorted descending: lambda_1 >= lambda_2 >= lambda_3."""
        evals = np.linalg.eigvalsh(self.s)
        return np.sort(evals)[::-1]

    @property
    def radius_of_gyration(self) -> float:
        """R_g = sqrt(lambda_1 + lambda_2 + lambda_3)."""
        return np.sqrt(max(0.0, float(np.trace(self.s))))

    def shape_descriptors(self) -> Tuple[float, float, float]:
        """Returns (asphericity b, acylindricity c, relative shape anisotropy kappa^2)."""
        l1, l2, l3 = self.principal_moments
        rg2 = l1 + l2 + l3
        b = l1 - 0.5 * (l2 + l3)
        c = l2 - l3
        kappa2 = (b**2 + 0.75 * c**2) / (rg2**2) if rg2 > 1e-15 else 0.0
        return b, c, kappa2
