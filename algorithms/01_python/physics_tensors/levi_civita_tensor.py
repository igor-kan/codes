"""Levi-Civita Completely Antisymmetric Permutation Tensor and Hodge Star.

Implements epsilon_{ijk}, epsilon_{mu nu rho sigma}, tensor densities, and Hodge duals.
"""

from typing import Sequence
import numpy as np


class LeviCivitaTensor:
    """Levi-Civita tensor and Hodge star operator."""

    @staticmethod
    def symbol_3d() -> np.ndarray:
        """Standard 3D permutation symbol epsilon_{ijk}."""
        eps = np.zeros((3, 3, 3), dtype=np.float64)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if (i, j, k) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
                        eps[i, j, k] = 1.0
                    elif (i, j, k) in [(0, 2, 1), (2, 1, 0), (1, 0, 2)]:
                        eps[i, j, k] = -1.0
        return eps

    @staticmethod
    def symbol_4d() -> np.ndarray:
        """Standard 4D permutation symbol epsilon_{mu nu rho sigma} with eps[0,1,2,3] = 1."""
        eps = np.zeros((4, 4, 4, 4), dtype=np.float64)
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        p = [i, j, k, l]
                        if len(set(p)) == 4:
                            inv_count = 0
                            for a in range(4):
                                for b in range(a + 1, 4):
                                    if p[a] > p[b]:
                                        inv_count += 1
                            eps[i, j, k, l] = 1.0 if inv_count % 2 == 0 else -1.0
        return eps

    @classmethod
    def curved_spacetime_tensor(cls, det_g: float) -> np.ndarray:
        """Covariant Levi-Civita tensor: E_{mu nu rho sigma} = sqrt(|det g|) * eps_{mu nu rho sigma}."""
        if det_g == 0.0:
            raise ValueError("Metric determinant must be non-zero")
        return np.sqrt(abs(det_g)) * cls.symbol_4d()

    @classmethod
    def hodge_star_2form_4d(cls, f_cov: np.ndarray, metric: np.ndarray) -> np.ndarray:
        """Compute Hodge dual 2-form *F_{mu nu} = 1/2 E_{mu nu rho sigma} g^{rho a} g^{sigma b} F_{ab}."""
        det_g = float(np.linalg.det(metric))
        e_cov = cls.curved_spacetime_tensor(det_g)
        inv_g = np.linalg.inv(metric)
        f_up = inv_g @ f_cov @ inv_g
        return 0.5 * np.einsum('mnrs,rs->mn', e_cov, f_up)
