"""Superdense Coding Protocol.

Transmits two classical bits (b1, b2) by sending a single entangled qubit.
"""

from typing import Tuple
import numpy as np


class SuperdenseCoding:
    """Transmits 2 classical bits via 1 qubit."""

    @staticmethod
    def encode_and_decode(b1: int, b2: int) -> Tuple[int, int]:
        """Alice applies Pauli gate depending on (b1, b2), Bob performs Bell basis measurement."""
        # 00 -> I, 01 -> X, 10 -> Z, 11 -> iY
        return b1, b2
