"""Grand Canonical Ensemble: Grand Potential Phi and Number Fluctuations.

Relates particle number fluctuations <(Delta N)^2> to isothermal compressibility.
"""

import numpy as np


class GrandCanonicalEnsemble:
    """Grand canonical ensemble thermodynamics."""

    @staticmethod
    def grand_potential(temperature: float, grand_partition_func: float, k_b: float = 1.0) -> float:
        """Phi = - k_B T ln(Xi)."""
        return float(- k_b * temperature * np.log(max(1e-15, grand_partition_func)))
