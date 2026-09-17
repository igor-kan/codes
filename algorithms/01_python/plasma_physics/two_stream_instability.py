"""Electrostatic Two-Stream Plasma Instability Dispersion Relation.

Calculates maximum growth rate gamma_max = sqrt(3)/2^{4/3} omega_p for counter-streaming electron beams.
"""

import numpy as np


class TwoStreamInstability:
    """Two-stream beam instability."""

    @staticmethod
    def max_growth_rate(beam_plasma_frequency: float) -> float:
        """gamma_max = (sqrt(3) / 2^(4/3)) * omega_p approx 0.687 omega_p."""
        return float((np.sqrt(3.0) / (2.0**(4.0 / 3.0))) * beam_plasma_frequency)
