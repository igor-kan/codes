"""Elasticity 4th-Rank Stiffness Tensor C_{ijkl} and Voigt Matrix Notation.

Represents generalized Hooke's law sigma_{ij} = C_{ijkl} varepsilon_{kl} for anisotropic and isotropic media.
"""

from typing import Sequence, Tuple
import numpy as np


class ElasticityStiffnessTensor:
    """Rank-4 elasticity tensor C_{ijkl} with major and minor symmetries."""

    VOIGT_MAP = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]

    def __init__(self, c_4d: np.ndarray):
        self.c = np.array(c_4d, dtype=np.float64)
        if self.c.shape != (3, 3, 3, 3):
            raise ValueError("Stiffness tensor must be 3x3x3x3")

    @classmethod
    def isotropic(cls, youngs_modulus: float, poissons_ratio: float) -> 'ElasticityStiffnessTensor':
        """Isotropic elasticity with Lame parameters lambda and mu."""
        e = youngs_modulus
        nu = poissons_ratio
        lam = e * nu / ((1.0 + nu) * (1.0 - 2.0 * nu))
        mu = e / (2.0 * (1.0 + nu))

        c = np.zeros((3, 3, 3, 3), dtype=np.float64)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        c[i, j, k, l] = (
                            lam * (1.0 if i == j and k == l else 0.0) +
                            mu * ((1.0 if i == k and j == l else 0.0) + (1.0 if i == l and j == k else 0.0))
                        )
        return cls(c)

    def to_voigt_6x6(self) -> np.ndarray:
        """Convert C_{ijkl} to 6x6 Voigt matrix C_{alpha beta}."""
        c_voigt = np.zeros((6, 6), dtype=np.float64)
        for a, (i, j) in enumerate(self.VOIGT_MAP):
            for b, (k, l) in enumerate(self.VOIGT_MAP):
                c_voigt[a, b] = self.c[i, j, k, l]
        return c_voigt

    def stress_from_strain(self, strain_3x3: Sequence[Sequence[float]]) -> np.ndarray:
        """sigma_{ij} = C_{ijkl} varepsilon_{kl}."""
        eps = np.array(strain_3x3, dtype=np.float64)
        return np.einsum('ijkl,kl->ij', self.c, eps)
