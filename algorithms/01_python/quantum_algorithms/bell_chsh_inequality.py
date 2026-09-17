"""Clauser-Horne-Shimony-Holt (CHSH) Bell Inequality Violation.

Calculates quantum correlation S = <AB> - <AB'> + <A'B> + <A'B'> = 2 sqrt(2) > 2 (Tsirelson bound).
"""

import numpy as np


class BellCHSHInequality:
    """Evaluates classical vs quantum CHSH correlators."""

    @staticmethod
    def quantum_tsirelson_bound() -> float:
        """Maximum quantum violation S = 2 * sqrt(2) approx 2.8284."""
        return float(2.0 * np.sqrt(2.0))

    @staticmethod
    def classical_local_hidden_variable_bound() -> float:
        """Bell-CHSH inequality classical bound: |S| <= 2."""
        return 2.0
