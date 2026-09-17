"""Steane [[7, 1, 3]] CSS Quantum Stabilizer Code.

Encodes 1 logical qubit into 7 physical qubits using classical Hamming [7, 4, 3] parity check matrix.
"""

from typing import Sequence
import numpy as np


class SteaneCode7Qubit:
    """CSS stabilizer generators and syndrome decoding."""

    # 6 stabilizer generators: 3 X-type and 3 Z-type
    HAMMING_PARITY = np.array([
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ], dtype=np.int32)

    @classmethod
    def syndrome_to_error_location(cls, syndrome_3bit: Sequence[int]) -> int:
        """Syndrome (s1, s2, s3) gives binary address of corrupted qubit (1-indexed)."""
        syn = np.array(syndrome_3bit, dtype=int)
        return int(syn[0] * 1 + syn[1] * 2 + syn[2] * 4)
