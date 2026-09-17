"""Toric and Surface Code Stabilizer Measurements on 2D Lattices.

Implements star operators A_s = prod X_i and face/plaquette operators B_p = prod Z_j.
"""

from typing import Sequence
import numpy as np


class SurfaceCodePlaquette:
    """Square lattice surface code stabilizers."""

    @staticmethod
    def star_operator_eigenvalue(x_spins: Sequence[int]) -> int:
        """A_s = prod_{i in star} X_i in {+1, -1}."""
        prod = 1
        for s in x_spins:
            prod *= s
        return prod

    @staticmethod
    def face_operator_eigenvalue(z_spins: Sequence[int]) -> int:
        """B_p = prod_{j in face} Z_j in {+1, -1}."""
        prod = 1
        for s in z_spins:
            prod *= s
        return prod
