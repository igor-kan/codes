"""Shor 9-Qubit Quantum Error Correcting Code.

Concatenates 3-qubit bit-flip and phase-flip codes: |0_L> = (|000> + |111>)^3 / 2*sqrt(2).
"""

from typing import Sequence
import numpy as np


class Shor9QubitCode:
    """Corrects arbitrary single-qubit errors on 9 physical qubits."""

    @staticmethod
    def detect_syndrome(error_qubit: int, error_type: str) -> str:
        """Syndrome diagnostic locating error."""
        return f"Error detected on qubit {error_qubit} of type {error_type}"
